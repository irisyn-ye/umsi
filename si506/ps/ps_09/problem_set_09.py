import requests
import json
import pprint


# HELPER FUNCTION. DO NOT ALTER
def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)


# HELPER FUNCTION. DO NOT ALTER
def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file
        ensure_ascii (str): if False non-ASCII characters are printed as is;
                            otherwise non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to
                      encoded JSON

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)

# HELPER FUNCTION. DO NOT ALTER
def get_character_info(person, characteristics):
    """
    Creates a dictionary representing a person by extracting
    the key-value pairs from the SWAPI representation of the person
    (i.e., the JSON object retrieved from the SWAPI API)

    Since there are multiple key-value pairs in the < person > dictionary
    retrieved from the SWAPI API, the function simplifies the < person >
    dictionary by only keeping the key-value pairs that have the key in
    < characteristics >.

    Parameters:
        person (dict): a dictionary containing information about a person
        characteristics (list): a list of strings representing a person's
        characteristics

    Returns:
        dict: a dictionary containing information about a person
    """

    return {key: person[key] for key in person.keys() if key in characteristics}

def get_swapi_resource(url, params=None):
    """
    Initiates an HTTP GET request to the SWAPI service in order
    to return a representation of a resource. If < params > is not
    included in the function call then do not include params in the
    request. Return a dictionary representation of the response.

    Parameters:
        url (str): a URL that specifies the resource.
        params (dict): an optional dictionary of querystring arguments.
        The default value is None.

    Returns:
        dict: dictionary representation of the decoded JSON.
    """
    if params:
        return requests.get(url, params).json()
    else:
        return requests.get(url).json()


def request_resource_details(base_url, category=None, params=None):
    """
    If provided, appends the resource < category > to the < base_url > to restrict the type of
    resource to be returned from SWAPI. If < params > are provided further qualifies the request
    by passing a dictionary of one or more querystring name-value pairs together with the (modified)
    < base_url > to the function < get_swapi_resource > which requests the resource.

    Parameters:
        base_url (str): The base URL to SWAPI
        category (str): The type of resource to fetch information for
                        (The possible categories include 'planets', 'people', 'starships', 'species', 'films', and 'vehicles.')
        params (dict): Dictionary of querystring arguments. The default value is None

    Returns:
        dict: dictionary representation of the resource retrieved from SWAPI.
    """
    complete_url = base_url
    categories = ['planets', 'people', 'starships', 'species', 'films', 'vehicles']
    if category in categories:
        complete_url = f"{base_url}/{category}"
        resource_info = get_swapi_resource(complete_url, params)
    return resource_info


def resolve_dict_url(resource, key_name):
    """
    Replaces the URL inside a dictionary with a dictionary representation of the data returned by
    the URL.

    Parameters:
        resource (dict): A dictionary that contains the URLs that have to be replaced with a
                         dictionary.
        key_name (str): The key that contains the URL that has to be resolved

    Returns:
        None
    """
    result = None
    resolve_url = resource[key_name]
    if type(resolve_url) == list:
        result = []
        for url in resolve_url:
            result.append(get_swapi_resource(url))
    else:
        result = get_swapi_resource(resolve_url)
    resource[key_name] = result


def get_darth_vader_info(base_url):
    """
    Retrieves all information about the Sith Lord, Darth Vader. Returns a dictionary comprising
    three key-value pairs:

    1. 'leader' (dict): representation of Darth Vader
    2. 'ships' (dict): representation of Darth Vader's ships
    3. 'planet' (dict): representation of the planet Bespin

    Parameters:
        base_url (str): Resource URL used to retrieve the resource.

    Returns:
        dict: leader, ships, and planet key-value pairs
    """
    vader_ships_info = []
    all_vader_info = {}
    vader_ships = ['Executor', 'TIE']
    vader_info = request_resource_details(base_url, 'people', {'search': 'Darth Vader'})['results'][0]
    for vader_ship in vader_ships:
        vader_ships_info.append(request_resource_details(base_url, 'starships', {'search': vader_ship})['results'][0])
    
    bespin_info = request_resource_details(base_url, 'planets', {'search': 'Bespin'})['results'][0]
    all_vader_info['leader'] = vader_info
    all_vader_info['ships'] = vader_ships_info
    all_vader_info['planet'] = bespin_info
    return all_vader_info


def fetch_boarding_order(passenger):
    """
    Returns the value of the 'boarding_order' key in the 'passenger' dict passed to it as an argument.

    Parameters:
        passenger (dict): A dictionary representation of a passenger.

    Returns:
        int: An integer value corresponding to the 'boarding_order' key
        in the 'passenger' dictionary.
    """
    return passenger['boarding_order']


def sort_boarding_order(boarding_order):
    """
    Accepts a list of dictionaries containing the name of each passenger and their boarding order.
    Sorts the passengers in ascending order according to their boarding order and returns the
    sorted list.

    Parameters:
        boarding_order (list): List of dictionaries containing the name and boarding order of each
                               passenger.

    Returns:
        list: List of dictionaries sorted according to the value of their
              'boarding_order' keys.
    """
    # for info in boarding_order:
    #     sorted(info, key=fetch_boarding_order)
    return sorted(boarding_order, key=fetch_boarding_order)


def main():
    """Program entry point.

    Parameters:
        None

    Returns:
        None
    """
    pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)
    # Use pp.pprint() to print dictionaries in a cleaner way.

    # Problem 1.2
    base_url = 'https://swapi.py4e.com/api'
    films_url = base_url + '/films'
    film_params = {'search': 'empire strikes back'}
    response = get_swapi_resource(films_url, film_params)
    film_details = response['results'][0]
    # print(film_details)

    # Problem 02
    planets_name = ['Hoth', 'Dagobah']
    planet_details = {}
    for planet_name in planets_name: 
        planet_details[planet_name] = request_resource_details(base_url, 'planets', {'search': planet_name})['results'][0]


    # Problem 03
    characteristics = ['name', 'height', 'mass', 'birth_year', 'homeworld', 'species']
    people_names = ['Luke', 'Yoda']
    people_details = {}
    
    for people_name in people_names:
        person = request_resource_details(base_url, 'people', {'search': people_name})['results'][0]
        people_details[people_name] = get_character_info(person, characteristics)
    # print(people_details)

    planet_details[planets_name[0]]['current_residents'] = [people_details[people_names[0]]]
    planet_details[planets_name[1]]['current_residents'] = [people_details[people_names[1]]]

    # Problem 04
    people_names.remove('Luke')
    people_names.remove('Yoda')
    # people_names.extend(['Han', 'Leia', 'C-3PO', 'R2-D2', 'Chewbacca'])
    people_names.extend(['Luke', 'Yoda', 'Han', 'Leia', 'C-3PO', 'R2-D2', 'Chewbacca'])
    # print(people_names)
    
    for people_name in people_names:
        person = request_resource_details(base_url, 'people', {'search': people_name})['results'][0]
        people_details[people_name] = get_character_info(person, characteristics)
    # print(people_details)

    species_order = {}
    for key, people_info in people_details.items():
        resolve_dict_url(people_info, 'species')
        species_name = people_info['species'][0]['name']
        if species_name not in species_order.keys():
            species_order[species_name] = [people_info]
        else:
            species_order[species_name].append(people_info)
    
    species_count = []
    for species_order_key in species_order.keys():
        # species_count_obj = (species_order_key, len(species_order[species_order_key]))
        species_count.append((species_order_key, len(species_order[species_order_key])))
    # print(species_count)
    # Problem 05
    starship_info = {}
    starship_names = ['X-Wing', 'Millennium Falcon']
    rebels = ['Luke', 'R2-D2', 'Han', 'Chewbacca', 'Leia', 'C-3PO']

    for starship_name in starship_names:
        starship_details = request_resource_details(base_url, 'starships', {'search': starship_name})['results'][0]
        starship_info[starship_name] = starship_details

    x_wing = starship_info[starship_names[0]]
    x_wing['crew_members'] = {'pilot': people_details[rebels[0]], 'astromech_droid': people_details[rebels[1]]}
    # x_wing['crew_members'] = {
    #     'pilot': people_details[rebels[0]],
    #     'astromech_droid': people_details[rebels[1]]
    # }
    # print(x_wing)

    millennium_falcon = starship_info[starship_names[1]]
    millennium_falcon['passengers_on_board'] = []
    millennium_falcon['crew_members'] = {'pilot': people_details[rebels[2]], 'copilot': people_details[rebels[3]]}
    # millennium_falcon['crew_members'] = {
    #     'pilot': people_details[rebels[2]],
    #     'copilot': people_details[rebels[3]]
    # }
    # print(people_details)
    for i in range(4, len(rebels)):
        millennium_falcon['passengers_on_board'].append(people_details[rebels[i]])
    
    write_json('starship_info.json', starship_info)

    # Problem 06
    residents_count = []
    planet_details['Hoth']['current_residents'] = []
    planet_details['Dagobah']['current_residents'].append(people_details['Luke'])
    planet_details['Dagobah']['current_residents'].append(people_details['R2-D2'])

    planet_details['Dagobah']['starships'] = [starship_info['X-Wing']]

    for planet_detail_key in planet_details.keys():
        residents_count.append((planet_detail_key, len(planet_details[planet_detail_key]['current_residents'])))

    # Problem 07
    all_vader_info = get_darth_vader_info(base_url)

    planet_details['Dagobah']['current_residents'].clear()
    planet_details['Dagobah']['starships'].clear()

    all_vader_info['planet']['current_residents'] = [people_details['Luke'], people_details['R2-D2']]
    all_vader_info['planet']['starships'] = starship_info['X-Wing']

    write_json('all_vader_info.json', all_vader_info)

    # Problem 08
    boarding_order = read_json('passengers_list.json')
    sorted_boarding_order = sort_boarding_order(boarding_order)
    write_json('sorted_boarding_order.json', sorted_boarding_order)

    # print(sorted_boarding_order)

if __name__ == "__main__":
    main()