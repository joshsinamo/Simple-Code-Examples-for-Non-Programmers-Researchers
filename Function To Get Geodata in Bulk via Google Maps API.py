import requests


def get_complete_geodata(address_or_zipcode, country_code, api_key):

    results = None
    base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?" \
               "fields=formatted_address%2Cname%2Copening_hours%2Cgeometry%2Ctypes"
    endpoint = f"{base_url}&input={address_or_zipcode}&" \
               f"inputtype=textquery&" \
               f"components=country:{country_code}&" \
               f"key={api_key}"

    r = requests.get(endpoint)
    if r.status_code not in range(200, 299):
        return None

    try:
        results = r.json()

    except:
        pass

    return results


if __name__ == "__main__":

    #EXAMPLE
    api_code = "INSERT YOUR API CODE HERE"
    example = get_complete_geodata(
        "San Antonio Marriott Rivercenter on the River Walk", "us", api_code)
    print(example)

    #OUTPUT:
    #{'candidates': [{'formatted_address': '101 Bowie St, San Antonio, TX 78205, United States', 'geometry': {'location': {'lat': 29.4231416, 'lng': -98.4836327}, 'viewport': {'northeast': {'lat': 29.42446832989272, 'lng': -98.48237607010728}, 'southwest': {'lat': 29.42176867010728, 'lng': -98.48507572989271}}}, 'name': 'San Antonio Marriott Rivercenter on the River Walk', 'types': ['lodging', 'point_of_interest', 'establishment']}, {'formatted_address': '889 E Market St, San Antonio, TX 78205, United States', 'geometry': {'location': {'lat': 29.4223461, 'lng': -98.48450419999999}, 'viewport': {'northeast': {'lat': 29.42365817989272, 'lng': -98.48323137010728}, 'southwest': {'lat': 29.42095852010728, 'lng': -98.48593102989273}}}, 'name': 'San Antonio Marriott Riverwalk', 'types': ['lodging', 'point_of_interest', 'establishment']}], 'status': 'OK'}

