# "pip install arcgis" in terminal
# if you do not have "arcgis" package installed already
from arcgis.geocoding import geocode
from arcgis.gis import GIS


if __name__ == "__main__":

    # Sample run to get geocode of an address:
    ARCGIS_API_KEY  = "INSERT YOUR API KEY HERE"
    gis             = GIS(api_key=ARCGIS_API_KEY)
    sample_location = "San Antonio Marriott Rivercenter on the River Walk"
    example         = geocode(address=sample_location)

    print(example)

    # OUTPUT:
    """
    [{'address': 'Marriott-San Antonio River Center',
      'location': {'x': -98.48347999999999, 'y': 29.423240000000078},
      'score': 81.21,
      'attributes': {'Loc_name': 'World', 'Status': 'M', 'Score': 81.21,
                     'Match_addr': 'Marriott-San Antonio River Center',
                     'LongLabel': 'Marriott-San Antonio River Center, 101 Bowie St, San Antonio, TX, 78205, USA',
                     'ShortLabel': 'Marriott-San Antonio River Center',
                     'Addr_type': 'POI', 'Type': 'Hotel',
                     'PlaceName': 'Marriott-San Antonio River Center',
                     'Place_addr': '101 Bowie St, San Antonio, Texas, 78205',
                     'Phone': '(210) 223-1000',
                     'URL': 'https://www.marriott.com/hotels/travel/satrc-san-antonio-marriott-rivercenter/?scid=bb1a189a-fec3-4d19-a255-54ba596febe2&y_source=1_NzQ4MDg1LTcxNS1sb2NhdGlvbi5nb29nbGVfd2Vic2l0ZV9vdmVycmlkZQ%3D%3D',
                     'Rank': 19, 'AddBldg': '', 'AddNum': '101',
                     'AddNumFrom': '', 'AddNumTo': '', 'AddRange': '',
                     'Side': '', 'StPreDir': '', 'StPreType': '',
                     'StName': 'Bowie', 'StType': 'St', 'StDir': '',
                     'BldgType': '', 'BldgName': '', 'LevelType': '',
                     'LevelName': '', 'UnitType': '', 'UnitName': '',
                     'SubAddr': '', 'StAddr': '101 Bowie St', 'Block': '',
                     'Sector': '', 'Nbrhd': 'Downtown', 'District': '',
                     'City': 'San Antonio',
                     'MetroArea': 'San Antonio Metro Area',
                     'Subregion': 'Bexar County', 'Region': 'Texas',
                     'RegionAbbr': 'TX', 'Territory': '', 'Zone': '',
                     'Postal': '78205', 'PostalExt': '', 'Country': 'USA',
                     'CntryName': 'United States', 'LangCode': 'ENG',
                     'Distance': 0, 'X': -98.48347999999999,
                     'Y': 29.423240000000078, 'DisplayX': -98.48347999999999,
                     'DisplayY': 29.423240000000078, 'Xmin': -98.48847999999998,
                     'Xmax': -98.47847999999999, 'Ymin': 29.41824000000008,
                     'Ymax': 29.428240000000077, 'ExInfo': 'ON THE RIVER WALK'},
      'extent': {'xmin': -98.48847999999998, 'ymin': 29.41824000000008,
                 'xmax': -98.47847999999999, 'ymax': 29.428240000000077}},
     {'address': 'The Bar At Marriott River Center',
      'location': {'x': -98.48426999999998, 'y': 29.42257200000006},
      'score': 76.67,
      'attributes': {'Loc_name': 'World', 'Status': 'M', 'Score': 76.67,
                     'Match_addr': 'The Bar At Marriott River Center',
                     'LongLabel': 'The Bar At Marriott River Center, 889 E Market St, San Antonio, TX, 78205, USA',
                     'ShortLabel': 'The Bar At Marriott River Center',
                     'Addr_type': 'POI', 'Type': 'Bar or Pub',
                     'PlaceName': 'The Bar At Marriott River Center',
                     'Place_addr': '889 E Market St, San Antonio, Texas, 78205',
                     'Phone': '(210) 224-4555', 'URL': '', 'Rank': 19,
                     'AddBldg': '', 'AddNum': '889', 'AddNumFrom': '',
                     'AddNumTo': '', 'AddRange': '', 'Side': '',
                     'StPreDir': 'E', 'StPreType': '', 'StName': 'Market',
                     'StType': 'St', 'StDir': '', 'BldgType': '',
                     'BldgName': '', 'LevelType': '', 'LevelName': '',
                     'UnitType': '', 'UnitName': '', 'SubAddr': '',
                     'StAddr': '889 E Market St', 'Block': '', 'Sector': '',
                     'Nbrhd': '', 'District': '', 'City': 'San Antonio',
                     'MetroArea': '', 'Subregion': 'Bexar County',
                     'Region': 'Texas', 'RegionAbbr': 'TX', 'Territory': '',
                     'Zone': '', 'Postal': '78205', 'PostalExt': '',
                     'Country': 'USA', 'CntryName': 'United States',
                     'LangCode': 'ENG', 'Distance': 0, 'X': -98.48426999999998,
                     'Y': 29.42257200000006, 'DisplayX': -98.48426999999998,
                     'DisplayY': 29.42257200000006, 'Xmin': -98.48526999999999,
                     'Xmax': -98.48326999999998, 'Ymin': 29.421572000000058,
                     'Ymax': 29.42357200000006, 'ExInfo': 'ON THE RIVER WALK'},
      'extent': {'xmin': -98.48526999999999, 'ymin': 29.421572000000058,
                 'xmax': -98.48326999999998, 'ymax': 29.42357200000006}},
     {'address': 'Marriott Dr, San Antonio, Texas, 78229',
      'location': {'x': -98.57130937362916, 'y': 29.518210625402528},
      'score': 75.92,
      'attributes': {'Loc_name': 'World', 'Status': 'T', 'Score': 75.92,
                     'Match_addr': 'Marriott Dr, San Antonio, Texas, 78229',
                     'LongLabel': 'Marriott Dr, San Antonio, TX, 78229, USA',
                     'ShortLabel': 'Marriott Dr', 'Addr_type': 'StreetName',
                     'Type': '', 'PlaceName': '',
                     'Place_addr': 'Marriott Dr, San Antonio, Texas, 78229',
                     'Phone': '', 'URL': '', 'Rank': 20, 'AddBldg': '',
                     'AddNum': '', 'AddNumFrom': '', 'AddNumTo': '',
                     'AddRange': '', 'Side': '', 'StPreDir': '',
                     'StPreType': '', 'StName': 'Marriott', 'StType': 'Dr',
                     'StDir': '', 'BldgType': '', 'BldgName': '',
                     'LevelType': '', 'LevelName': '', 'UnitType': '',
                     'UnitName': '', 'SubAddr': '', 'StAddr': 'Marriott Dr',
                     'Block': '', 'Sector': '', 'Nbrhd': '', 'District': '',
                     'City': 'San Antonio',
                     'MetroArea': 'San Antonio Metro Area',
                     'Subregion': 'Bexar County', 'Region': 'Texas',
                     'RegionAbbr': 'TX', 'Territory': '', 'Zone': '',
                     'Postal': '78229', 'PostalExt': '', 'Country': 'USA',
                     'CntryName': 'United States', 'LangCode': 'ENG',
                     'Distance': 0, 'X': -98.57130937362916,
                     'Y': 29.518210625402528, 'DisplayX': -98.57130937362916,
                     'DisplayY': 29.518210625402528, 'Xmin': -98.57230937362917,
                     'Xmax': -98.57030937362916, 'Ymin': 29.517210625402527,
                     'Ymax': 29.51921062540253, 'ExInfo': 'ON THE RIVER WALK'},
      'extent': {'xmin': -98.57230937362917, 'ymin': 29.517210625402527,
                 'xmax': -98.57030937362916, 'ymax': 29.51921062540253}},
     {'address': 'Marriott Pkwy, San Antonio, Texas, 78261',
      'location': {'x': -98.40563513574433, 'y': 29.663618488278363},
      'score': 75.92,
      'attributes': {'Loc_name': 'World', 'Status': 'T', 'Score': 75.92,
                     'Match_addr': 'Marriott Pkwy, San Antonio, Texas, 78261',
                     'LongLabel': 'Marriott Pkwy, San Antonio, TX, 78261, USA',
                     'ShortLabel': 'Marriott Pkwy', 'Addr_type': 'StreetName',
                     'Type': '', 'PlaceName': '',
                     'Place_addr': 'Marriott Pkwy, San Antonio, Texas, 78261',
                     'Phone': '', 'URL': '', 'Rank': 20, 'AddBldg': '',
                     'AddNum': '', 'AddNumFrom': '', 'AddNumTo': '',
                     'AddRange': '', 'Side': '', 'StPreDir': '',
                     'StPreType': '', 'StName': 'Marriott', 'StType': 'Pkwy',
                     'StDir': '', 'BldgType': '', 'BldgName': '',
                     'LevelType': '', 'LevelName': '', 'UnitType': '',
                     'UnitName': '', 'SubAddr': '', 'StAddr': 'Marriott Pkwy',
                     'Block': '', 'Sector': '', 'Nbrhd': '', 'District': '',
                     'City': 'San Antonio',
                     'MetroArea': 'San Antonio Metro Area',
                     'Subregion': 'Bexar County', 'Region': 'Texas',
                     'RegionAbbr': 'TX', 'Territory': '', 'Zone': '',
                     'Postal': '78261', 'PostalExt': '', 'Country': 'USA',
                     'CntryName': 'United States', 'LangCode': 'ENG',
                     'Distance': 0, 'X': -98.40563513574433,
                     'Y': 29.663618488278363, 'DisplayX': -98.40563513574433,
                     'DisplayY': 29.663618488278363, 'Xmin': -98.40663513574434,
                     'Xmax': -98.40463513574433, 'Ymin': 29.662618488278362,
                     'Ymax': 29.664618488278364, 'ExInfo': 'ON THE RIVER WALK'},
      'extent': {'xmin': -98.40663513574434, 'ymin': 29.662618488278362,
                 'xmax': -98.40463513574433, 'ymax': 29.664618488278364}}]
    """