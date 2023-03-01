from nltk import FreqDist, word_tokenize, pos_tag
from collections import defaultdict
import pandas as pd

# ---------- IF NLTK HASN'T BEEN INSTALLED IN COMPUTER YET, RUN THIS -----------
# INSTALL nltk and ssl FIRST (either via pip, conda, homebrew, etc.) and then
# RUN THE FOLLOWING ........
# ..............................................................................
# import ssl
# import nltk

# try:
#    _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#    ssl._create_default_https_context = _create_unverified_https_context

# nltk.download()

# ------------------------------------------------------------------------------


# PURPOSE:
# This word_tagger function can be used to split a string of texts into words,
# tag the words with part-of-speech tags
# (e.g., "and" is a coordinating conjunction word),
# and then assess for each of these tags what the words used
# as well as having the frequency of how many times those words
# are used for those tags. Tokenizing words is a common NLP strategy
# and may be helpful for research teams interested in assessing open-ended
# responses beyond via manual coding, especially when having a large quantity
# of data to review.

# content = String object
# source  = The source of where the content was generated from; can be anything.

def word_tagger(source, content):
    # The meaning of these columns are available here:
    # https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    columns = ["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS",
               "MD", "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$",
               "RB", "RBR","RBS", "RP", "SYM", "TO", "UH", "VB", "VBD", "VBG",
               "VBN", "VBP", "VBZ", "WDT", "WP", "WP$", "WRB"]

    # A. TOKENIZE:
    # 1. Transform the content to all have lowercase
    # 2. Tokenize the sentences into words
    # 3. Assign tags to the words (please check the link above about
    #      the meaning of the tags)
    # 4. Create a frequency distribution list of those tags
    # 5. Turn #4 into a dictionary

    text_dict = dict(FreqDist(pos_tag(word_tokenize(content.lower()))))

    # B. Create an empty dictionary
    output = {}

    # C. Iterate over items in A and reverse the key-value pair in A to value
    #      as key and key as value
    for k, v in text_dict.items():
        output[v] = output.get(v, [])
        output[v].append(k)

    # D. Iterate over keys in dictionary "output" and then set the tags
    #       as the key and the words as values and the frequency
    #       as top level 'key'
    for i in output.keys():
        d = defaultdict(list)
        for v, k in output[i]:
            d[k].append(v)
        output[i] = dict(d)
        del d

    # E. Turn output into dataframe, transpose, and then sort the index
    f = pd.DataFrame(output).T.sort_index()

    # F. Drop columns with tags not present in the "column" variable previously
    #       instantiated (row 33). Then, set the source parameter as the index
    df = f[f.columns.intersection(columns)]
    df = df.dropna(how="all")
    df['index'] = source

    # Combine the lists containing words inside DataFrame into
    #    a single text with semicolon separator
    df = df.applymap(lambda x:
                     x if not isinstance(x, list)
                     else ';'.join(x) if len(x) else '')
    df['frequency'] = df.index

    print(df)
    df.to_csv("testdata.csv")


if __name__ == "__main__":
    # SAMPLE RUN

    print(word_tagger(
        "https://www.paho.org/en/topics/tobacco-control",

        "Tobacco Control team works to help reduce the burden of disease, "
        "death, and economic consequences caused by tobacco use and exposure "
        "to second-hand smoke in the Americas Region. Tobacco is the single "
        "most preventable cause of death in the world today. As tobacco use "
        "continues to rise in many parts of the world, it becomes increasingly "
        "more important that governments work jointly with civil society to "
        "implement the mandates of the WHO Framework Convention on Tobacco "
        "Control to protect their citizens from tobacco and educate them "
        "about the dangers associated with its use."))
