import re
import time
from collections import Counter
from multiprocessing import Process, Manager
from random import shuffle, choice
from tkinter import messagebox
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from tldextract import tldextract


# Convert csv to list
# filename = absolute path (in str) to your filename
def csv_to_list(filename):
    with open(str(filename), 'r') as file:
        data = [line.rstrip('\n') for line in file]

    return data


class Crawler:
    def __init__(self, seed_address, depth, within_domain, n_bots, bot_adresses,
                 edges_fname, nodes_fname, filter_address,
                 sample_size, min_inlinks, query=None):

        self.seed_address   = seed_address
        self.within_domain  = within_domain
        self.n_bots         = n_bots
        self.bot_adresses   = bot_adresses
        self.edges_fname    = edges_fname
        self.nodes_fname    = nodes_fname
        self.filter_address = filter_address
        self.sample_size    = sample_size
        self.min_inlinks    = min_inlinks
        self.query          = query

        self.depth = depth
        self.current_depth = 1

        self.jobs = []
        self.main_manager = Manager()
        self.edges_dict = self.main_manager.dict()
        self.nodes_dict = self.main_manager.dict()

        self.seeds = csv_to_list(self.seed_address)

    def start_crawl(self):

        start_time = time.time()

        if self.filter_address is not None:
            with open(self.filter_address) as f:
                self.query = f.read()

        scrambled_seeds = self.split_seeds(self.seeds, self.n_bots)

        while self.current_depth <= self.depth:
            branch_manager = Manager()
            next_source    = branch_manager.list()

            for subList, index in zip(scrambled_seeds,
                                      list(range(1, self.n_bots + 1))):
                p = Process(target=self.web_crawler,
                            args=(subList,
                                  self.bot_adresses[index], next_source))

                p.start()
                self.jobs.append(p)

            for proc in self.jobs:
                proc.join()

            scrambled_seeds = self.split_seeds(
                self.seeds_pps_sampler(
                    self.freq_is_ok(next_source, self.min_inlinks),
                    self.sample_size),
                self.n_bots)

            self.current_depth += 1

        self.save_files()
        end_time = time.time()

        messagebox.showinfo(message="Your crawl has finished!\n"
                                    f"Elapsed time = "
                                    f"{end_time - start_time}")

    # Get all links inside a webpage
    # driver = webdriver (chrome)
    # seed   = string of webpage link
    @staticmethod
    def get_links(driver, seed):
        links_list = []
        try:
            # open the webpage
            driver.get(seed)

            # get all links inside that webpage
            links_list = [str(link.get_attribute("href")) for link in
                          driver.find_elements(By.PARTIAL_LINK_TEXT, "")]

        # if website can't be opened, print the error
        except Exception as e:
            print(e.args)

        return links_list

    # Get all TEXT content inside a webpage in string
    # driver = webdriver (chrome)
    # target = website which text content to be extracted
    @staticmethod
    def get_contents(driver, target):
        content = "ERROR"
        if "://" in str(target):
            try:
                driver.get(target)
                content = driver.find_element(By.TAG_NAME, "body").text

            except Exception as e:
                print(e.args)

        return content

    # Check whether the edge respect the domestic out-link restriction (if any)
    # tldSource    = tuple of top domain & suffix name
    # target       = string of target link
    # within_domain = user input from tkinter on whether
    #                 they want domestic out-links
    @staticmethod
    def direction_is_ok(source, target, within_domain):
        # if we don't want any domestic out-links
        if not within_domain:

            tld_target = (tldextract.extract(target))
            tld_source = (tldextract.extract(source))

            # check whether website name and website suffix (.com, .edu, etc)
            # are the same
            return tld_target.domain.lower() != tld_source.domain.lower() or \
                tld_target.suffix.lower() != tld_source.suffix.lower()

        # if we want domestic out-links
        # WARNING: THIS WILL MAKE THE PROCESS EXPONENTIALLY LARGER
        else:
            return True

    # this turns a string query to search for content
    # contentsList = string in each website visited
    # filename      = from GUI, csv file of a query
    @staticmethod
    def content_is_ok(content, query=None):
        # Changing string query to evaluable pythonic statement
        # For example :  "('word1' and 'word2') or 'word3'"
        #             :  will be ('word1' in content and 'word2' in content)
        #             :           or 'word3' in content
        if (query is not None
            and eval(re.sub(r"([a-zA-Z0-9]\')", r"\1 in content", query))) \
                or query is None:

            return True

        # if query doesn't match
        else:
            return False

    # Return list of potential seeds which has at least min_count in-links
    # next_source : manager.list() object (with list of potential seeds)
    # min_count   : desired number of minimum in-links for potential sources
    @staticmethod
    def freq_is_ok(next_source, min_count):

        return [k for k, v in Counter(next_source).items() if v >= min_count]

    # Saving output in csv format; ready for most network analysis software
    #   such as Gephi, Cytoscape, U.C.I.N.E.T, etc.
    # edges_dict      = dictionary of all directed edges (or relationship)
    # nodes_dict      = dictionary of all nodes and their contents
    # edges_filename  = .csv filename to save for edges_dict
    # nodes_filename  = .csv filename to save for nodes_dict

    # def save_files(edges_dict, nodes_dict, edges_filename, nodes_filename):
    def save_files(self):
        edges_file = pd.DataFrame(dict(self.edges_dict), index=[0]).T.reset_index()
        nodes_file = pd.DataFrame(dict(self.nodes_dict)).T.reset_index()

        edges_file.columns = ["source", "target", "weight"]
        nodes_file.columns = ["site", "depth", "content"]

        edges_file.to_csv(self.edges_fname + '.csv', index=False, sep=',')
        nodes_file.to_csv(self.nodes_fname + '.csv', index=False, sep=',')

        del edges_file
        del nodes_file

    # Splitting seed links to n split (depending on # of parallel process)
    #   and minimize difference in length between sets using generator
    # seed_list  = list of sources to be crawled
    # n_split    = number of parallel process
    @staticmethod
    def split_seeds(seed_list, n_split):
        container = seed_list
        shuffle(container)

        for i in range(0, n_split):
            yield container[i::n_split]

    @staticmethod
    def seeds_pps_sampler(candidates, count):
        # not ['ALL', ]
        if count is not None:
            if 0 < count < 1:
                k = int(len(candidates) * count) + 1

            else:
                k = count
        else:
            return list(set(candidates))

        container = []
        for i in range(k):
            selected_item = choice(candidates)
            container.append(selected_item)
            candidates = [x for x in candidates if x != selected_item]

        return container

    # Main function for web crawling
    # sources        = list of seed links
    # depth        = how deep recursively the crawl will be
    # driver       = webdriver bot
    # within_domain = whether it'll crawl out-links within the same domain
    # edges_dict    = dictionary for edges to be shared between main processes
    # nodes_dict    = dictionary for nodes to be shared between main processes
    # next_source   = list of potential targets to be shared between sub-procs
    # filter_address = File address of the filter file (string)
    def web_crawler(self, sources, bot_address, next_source):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-notifications")

        driver = webdriver.Chrome(service=Service(bot_address),
                                  options=chrome_options)
        # get contents for all initial seed links
        if self.current_depth == 1:
            for source in sources:
                initial_content = self.get_contents(driver, source)
                self.nodes_dict[source] = [[0], initial_content]

        for source in sources:

            # get toplevel domain & suffix name
            # tld_source = (tldextract.extract(seed))
            for target in self.get_links(driver, source):

                if (source, target) in self.edges_dict:
                    # add weight if the edge is already exist in the edges dict
                    self.edges_dict[(source, target)] += 1

                else:
                    # check whether the node is a domestic out-links
                    # and whether it aligns with the crawling parameter
                    if self.direction_is_ok(source, target, self.within_domain):
                        potential_content = self.get_contents(driver, target)

                        # check whether the content fit with query
                        if self.content_is_ok(potential_content, self.query):
                            self.edges_dict[(source, target)] = 1

                            # check whether there's duplicate of target
                            if target not in next_source:
                                next_source.append(target)

                            # check whether there's duplicate of node
                            if target not in self.nodes_dict:
                                self.nodes_dict[target] = [[self.current_depth],
                                                           potential_content]
                            else:
                                self.nodes_dict[target][0].append(self.current_depth)


if __name__ == "__main__":

    seed_address1   = "ADDRESS OF FILE CONTAINING SEEDS"
    depth1          = 2
    within_domain1  = False
    n_bots1         = 1
    edges_filename1 = "edges.csv"
    nodes_filename1 = "nodes.csv"
    filter_address1 = None
    query1          = None
    sample_size1     = 100
    min_inlinks1     = 3

    bot_addresses1 = ["CHROME DRIVER 1", ".... CHROME DRIVER N"]

    crawl1 = Crawler(seed_address1, depth1, within_domain1, n_bots1,
                     bot_addresses1,
                     edges_filename1, nodes_filename1, filter_address1,
                     sample_size1, min_inlinks1, query1)

    crawl1.start_crawl()


