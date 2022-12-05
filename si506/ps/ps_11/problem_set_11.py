# PROBLEM SET 11
import copy
import csv
import json
import requests
import sys

import five_oh_six as utl

CACHE_FILEPATH = './stu-cache.json'
SWAPI_ENDPOINT = 'https://swapi.py4e.com/api'
SWAPI_CATEGORIES = f"{SWAPI_ENDPOINT}/"
SWAPI_PEOPLE = f"{SWAPI_ENDPOINT}/people/"
SWAPI_PLANETS = f"{SWAPI_ENDPOINT}/planets/"
SWAPI_SPECIES = f"{SWAPI_ENDPOINT}/species/"
SWAPI_STARSHIPS = f"{SWAPI_ENDPOINT}/starships/"
SWAPI_VEHICLES = f"{SWAPI_ENDPOINT}/vehicles/"

def board_passengers(starship, passengers):
    """Assigns < passengers > to the passed in < starship > but limits boarding to less than
    or equal to the starship's "max_passengers" value. The passengers list (in whole or in part)
    is then mapped (i.e., assigned) to the passed in starship's 'passengers_on_board' key. After
    boarding the passengers the starship is returned to the caller.

    WARN: The number of passengers permitted to board a starship is limited by the starship's
    "max_passengers" value. If the number of passengers attempting to board exceeds the starship's
    "max_passengers" value only the first n passengers (where `n` = "max_passengers") are
    permitted to board the vessel.

        Parameters:
            starship (dict): Representation of a starship.
            passengers (list): passengers to transport aboard starship.

        Returns:
            dict: starship with assigned passengers.
    """
    # pass
    # if len(passengers) > starship['max_passengers']:
    #     starship['passengers_on_board'] = passengers.slice(0, starship['max_passengers'])
    # else:
    #     starship['passengers_on_board'] = passengers
    # return starship

    if starship['max_passengers'] >= len(passengers):
        starship['passengers_on_board'] = passengers
    else:
        starship['passengers_on_board'] = []
        for i in range(starship['max_passengers']):
            starship['passengers_on_board'].append(passengers[i])
    return starship


def convert_gravity_value(value):
    """Convert a planet's "gravity" value to a float. Removes the "standard" unit of measure if
    it exists in the string (case-insensitive check). Delegates to the function
    < convert_to_float > the task of casting the < value > to a float.

    If an exception is encountered the < value > is passed to < convert_to_none > in an attempt
    to convert the < value > to None if the < value > matches a < NONE_VALUES > item. The return
    value of < convert_to_none > is then returned to the caller.

    Parameters:
        value (obj): string to be converted.

    Returns:
        float: if value successfully converted; otherwise returns value unchanged.
    """

    try:
        return utl.convert_to_float(value.strip().lower().replace('standard', ''))
    except:
        return utl.convert_to_none(value)


def create_droid(data):
    """Returns a new dictionary representation of a droid from the passed in < data >,
    converting string values to the appropriate type whenever possible.

    Type conversions:
        height -> height_cm (str to float)
        mass -> mass_kg (str to float)
        equipment -> equipment (str to list)

    Key order:
        url
        name
        model
        manufacturer
        create_year
        height_cm
        mass_kg
        equipment
        instructions

    Parameters:
        data (dict): source data.

    Returns:
        dict: new dictionary.
    """

    return {
        'url': utl.convert_to_none(data.get('url')),
        'name': utl.convert_to_none(data.get('name')),
        'model': utl.convert_to_none(data.get('model')),
        'manufacturer': utl.convert_to_none(data.get('manufacturer')),
        'create_year': utl.convert_to_none(data.get('create_year')),
        'height_cm': utl.convert_to_float(data.get('height')),
        'mass_kg': utl.convert_to_float(data.get('mass')),
        'equipment': utl.convert_to_list(data.get('equipment'), delimiter='|'),
        'instructions': utl.convert_to_none(data.get('instructions'))
    }


def create_person(data, planets=None, species=None):
    """Returns a new dictionary representation of a person from the passed in < data >,
    converting string values to the appropriate type whenever possible.

    If an optional Wookieepedia-sourced < planets > and/or < species > list is provided, the task of retrieving the appropriate nested dictionary (filters on the passed in homeworld planet name) is delegated to the function < get_mandalorian_data >.

    If < planets > and/or < species > list is not provided, the task of retrieving
    the appropriate nested dictionary (filters on the passed in homeworld/planet or species name) is delegated to the function < get_swapi_resource >.

    Before the homeworld and species data is mapped (e.g. assigned) to the person's "homeworld"
    and "species" keys, the functions < create_planet > and < create_species > are called
    in order to provide new dictionary representations of the person's homeworld and species.

    Type conversions:
        height -> height_cm (str to float)
        mass -> mass_kg (str to float)
        homeworld -> homeworld (str to dict)
        species -> species (str to dict)

    Key order:
        url
        name
        birth_year
        height_cm
        mass_kg
        homeworld
        species
        force_sensitive

    Parameters:
        data (dict): source data.
        planets (list): optional supplemental planetary data.

    Returns:
        dict: new dictionary.
    """
    # pass
    # Get, combine, clean data, and instantiate Planet instance
    if planets:
        planet_update = create_planet(get_mandalorian_data(planets, data['homeworld']))
    else:
        if data['homeworld']:
            try:
                planet_update = create_planet(get_swapi_resource(SWAPI_PLANETS, {'search': data['homeworld']})['results'][0])
            except:
                planet_update = create_planet(get_swapi_resource(data['homeworld']))
        else:
            planet_update = None

    if species:
        species_update = create_species(get_mandalorian_data(species, data['species']))
    else:
        if data['species']:
            try:
                species_update = create_species(get_swapi_resource(SWAPI_SPECIES, {'search': data['species']})['results'][0])
            except:
                species_update = create_species(get_swapi_resource(data['species']))
        else:
            species_update = None


    return {
        'url': utl.convert_to_none(data.get('url')),
        'name': utl.convert_to_none(data.get('name')),
        'birth_year': utl.convert_to_none(data.get('birth_year')),
        'height_cm': utl.convert_to_float(data.get('height')),
        'mass_kg': utl.convert_to_float(data.get('mass')),
        'homeworld': planet_update,
        'species': species_update,
        'force_sensitive': utl.convert_to_none(data.get('force_sensitive'))
    }


def create_planet(data):
    """Returns a new dictionary representation of a planet from the passed in < data >,
    converting string values to the appropriate type whenever possible.

    Type conversions:
        suns -> suns (str->int)
        moons -> moons (str->int)
        orbital_period -> orbital_period_days (str to float)
        diameter -> diameter_km (str to int)
        gravity -> gravity_std (str to float)
        climate -> climate (str to list)
        terrain -> terrain (str to list)
        population -> population (str->int)

    Key order:
        url
        name
        region
        sector
        suns
        moons
        orbital_period_days
        diameter_km
        gravity_std
        climate
        terrain
        population

    Parameters:
        data (dict): source data.

    Returns:
        dict: new dictionary.
    """
    # pass
    return {
        'url': utl.convert_to_none(data.get('url')),
        'name': utl.convert_to_none(data.get('name')),
        'region': utl.convert_to_none(data.get('region')),
        'sector': utl.convert_to_none(data.get('sector')),
        'suns': utl.convert_to_int(data.get('suns')),
        'moons': utl.convert_to_int(data.get('moons')),
        'orbital_period_days': utl.convert_to_float(data.get('orbital_period')),
        'diameter_km': utl.convert_to_int(data.get('diameter')),
        'gravity_std': convert_gravity_value(data.get('gravity')),
        'climate': utl.convert_to_list(data.get('climate'), delimiter=', '),
        'terrain': utl.convert_to_list(data.get('terrain'), delimiter=', '),
        'population': utl.convert_to_int(data.get('population'))
    }


def create_species(data):
    """Returns a new dictionary representation of a species from the passed in
    < data >, converting string values to the appropriate type whenever possible.

    Type conversions:
        average_lifespan -> average_lifespan (str to int)
        average_height -> average_height_cm (str to float)

    Key order:
        url
        name
        classification
        designation
        average_lifespan
        average_height_cm
        language

    Parameters:
        data (dict): source data.

    Returns:
        dict: new dictionary.
    """

    return {
        'url': utl.convert_to_none(data.get('url')),
        'name': utl.convert_to_none(data.get('name')),
        'classification': utl.convert_to_none(data.get('classification')),
        'designation': utl.convert_to_none(data.get('designation')),
        'average_lifespan': utl.convert_to_int(data.get('average_lifespan')),
        'average_height_cm': utl.convert_to_float(data.get('average_height')),
        'language': utl.convert_to_none(data.get('language'))
    }


def create_starship(data):
    """Returns a new starship dictionary from the passed in < data >, converting string
    values to the appropriate type whenever possible.

    Assigning crews and passengers consitute separate
    operations.

    Type conversions:
        length -> length_m (str to float)
        max_atmosphering_speed -> max_atmosphering_speed (str to int)
        hyperdrive_rating -> hyperdrive_rating (str to float)
        MGLT -> MGLT (str to int)
        crew -> crew_size (str to int)
        passengers -> max_passengers (str to int)
        armament -> armament (str to list)
        cargo_capacity -> cargo_capacity_kg (str to int)

    Key order:
        url
        name
        model
        starship_class
        manufacturer
        length_m
        max_atmosphering_speed
        hyperdrive_rating
        top_speed_mglt
        armament
        crew_size
        crew_members
        max_passengers
        passengers_on_board
        cargo_capacity_kg
        consumables

    Parameters:
        data (dict): source data.

    Returns:
        dict: new dictionary.
    """

    return {
        'url': utl.convert_to_none(data.get('url')),
        'name': utl.convert_to_none(data.get('name')),
        'model': utl.convert_to_none(data.get('model')),
        'starship_class': utl.convert_to_none(data.get('starship_class')),
        'manufacturer': utl.convert_to_none(data.get('manufacturer')),
        'length_m': utl.convert_to_float(data.get('length')),
        'max_atmosphering_speed': utl.convert_to_int(data.get('max_atmosphering_speed')),
        'hyperdrive_rating': utl.convert_to_float(data.get('hyperdrive_rating')),
        'top_speed_mglt': utl.convert_to_int(data.get('MGLT')),
        'armament': utl.convert_to_list(data.get('armament'), delimiter='|'),
        'crew_size': utl.convert_to_int(data.get('crew')),
        'crew_members': utl.convert_to_none(data.get('crew_members')),
        'max_passengers': utl.convert_to_int(data.get('passengers')),
        'passengers_on_board': utl.convert_to_none(data.get('passengers_on_board')),
        'cargo_capacity_kg': utl.convert_to_int(data.get('cargo_capacity')),
        'consumables': utl.convert_to_none(data.get('consumables')),
    }


def create_vehicle(data):
    """Returns a new vehicle dictionary from the passed in < data >, converting string
    values to the appropriate type whenever possible.

    Assigning crews and passengers consitute separate
    operations.

    Type conversions:
        length -> length_m (str to float)
        max_atmosphering_speed -> max_atmosphering_speed (str to int)
        hyperdrive_rating -> hyperdrive_rating (str to float)
        MGLT -> MGLT (str to int)
        crew -> crew_size (str to int)
        passengers -> max_passengers (str to int)
        armament -> armament (str to list)
        cargo_capacity -> cargo_capacity_kg (str to int)

    Key order:
        url
        name
        model
        vehicle_class
        manufacturer
        length_m
        max_atmosphering_speed
        armament
        crew_size
        crew_members
        passengers
        passengers_on_board
        cargo_capacity_kg
        consumables

    Parameters:
        data (dict): source data.

    Returns:
        dict: new dictionary.
    """

    return {
        'url': utl.convert_to_none(data.get('url')),
        'name': utl.convert_to_none(data.get('name')),
        'model': utl.convert_to_none(data.get('model')),
        'vehicle_class': utl.convert_to_none(data.get('vehicle_class')),
        'manufacturer': utl.convert_to_none(data.get('manufacturer')),
        'length_m': utl.convert_to_float(data.get('length')),
        'max_atmosphering_speed': utl.convert_to_int(data.get('max_atmosphering_speed')),
        'armament': utl.convert_to_list(data.get('armament'), delimiter='|'),
        'crew_size': utl.convert_to_int(data.get('crew')),
        'crew_members': utl.convert_to_none(data.get('crew_members')),
        'max_passengers': utl.convert_to_int(data.get('passengers')),
        'passengers_on_board': utl.convert_to_none(data.get('passengers_on_board')),
        'cargo_capacity_kg': utl.convert_to_int(data.get('cargo_capacity')),
        'consumables': utl.convert_to_none(data.get('consumables')),
    }


def get_mandalorian_data(mandalorian_data, filter):
    """Attempts to retrieve a Wookieepedia sourced dictionary representation of a
    Star Wars entity (e.g., droid, person, planet, species, starship, or vehicle)
    from the < mandalorian_data > list using the passed in filter value. The function performs
    a case-insensitive comparison of each nested dictionary's "name" value against the
    passed in < filter > value. If a match is obtained the dictionary is returned to the
    caller; otherwise None is returned.

    Parameters:
        mandalorian_data (list): Wookieepedia-sourced data stored in a list of nested dictionaries.
        filter (str): name value used to match on a dictionary's "name" value.

    Returns
        dict|None: Wookieepedia-sourced data dictionary if match on the filter is obtained;
                   otherwise returns None.
    """
    for mandalorian_data_obj in mandalorian_data:
        if mandalorian_data_obj['name'].lower() == filter.lower():
            return mandalorian_data_obj
        # else:
    return None


def get_swapi_resource(url, params=None, timeout=10):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provided the response object body is returned in the form on an "envelope" with the data
    payload of one or more SWAPI entities to be found in ['results'] list; otherwise, response
    object body is returned as a single dictionary representation of the SWAPI entity.

    Parameters:
        url (str): a uniform resource locator that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds.

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    # WARN: deep copying required to guard against mutating cache objects
    key = utl.create_cache_key(url, params)
    if key in utl.cache.keys():
        return copy.deepcopy(utl.cache[key]) # recursive copy of objects
    else:
        resource = utl.get_resource(url, params, timeout)
        utl.cache[key] = copy.deepcopy(resource) # recursive copy of objects
        return resource


def update_planets_visited(data, planet_name):
    """Adds new planet name to the key ['planets_visited'] in the data dictionary. If the
    key ['planets_visited'] is not in the data dictionary keys, the key is added to the dictionary.
    If the name of the planets is not already stored in the value of ['planets_visited'] then the planet's
    name is added to the list.

    Parameters:
        data (dict): dictionary representation of a starship.
        planet_name (str): name of a planet.

    Returns:
        dict: dictionary with the 'planets_visited' key updated.
    """
    if 'planets_visited' not in data.keys():
        data['planets_visited'] = [planet_name]
    else:
        data['planets_visited'].append(planet_name)
    return data


def main():
    """Entry point for program.

    Parameters:
        None

    Returns:
        None
    """
    # PROBLEM 01
    # Problem 1.2
    mandalorian_people = utl.read_csv_to_dicts('mandalorian_people.csv')

    # Problem 1.3
    mandalorian_starships = utl.read_json('mandalorian_starships.json')
    mandalorian_planets = utl.read_json('mandalorian_planets.json')
    mandalorian_droids = utl.read_json('mandalorian_droids.json')
    mandalorian_vehicles = utl.read_json('mandalorian_vehicles.json')

    # PROBLEM 02
    # Problem 2.1.5 Test convert_to_none(), convert_to_int(), convert_to_float(), convert_to_list()

    # print(f"\n2.1.1 convert_to_none -> None = {utl.convert_to_none(' N/A ')}")
    # print(f"\n2.1.1 convert_to_none -> None = {utl.convert_to_none('')}")
    # print(f"\n2.1.1 convert_to_none -> no change = {utl.convert_to_none('Yoda ')}")
    # print(f"\n2.1.1 convert_to_none -> no change = {utl.convert_to_none(5.5)}")
    # print(f"\n2.1.1 convert_to_none -> no change = {utl.convert_to_none((1, 2, 3))}")

    # print(f"\n2.1.2 convert_to_int -> int = {utl.convert_to_int('506 ')}")
    # print(f"\n2.1.2 convert_to_int -> None = {utl.convert_to_int(' unknown')}")
    # print(f"\n2.1.2 convert_to_int -> no change = {utl.convert_to_int([506, 507])}")

    # print(f"\n2.1.3 convert_to_float -> float = {utl.convert_to_float('4.0')}")
    # print(f"\n2.1.3 convert_to_float -> None = {utl.convert_to_float('n/a')}")
    # print(f"\n2.1.3 convert_to_float -> no change = {utl.convert_to_int([618, 664])}")

    # print(f"\n2.1.4 convert_to_list -> list = {utl.convert_to_list('Diag, Hatcher, North Quad', ', ')}")
    # print(f"\n2.1.4 convert_to_list -> None = {utl.convert_to_list('n/a')}")
    # print(f"\n2.1.4 convert_to_list -> no change = {utl.convert_to_list([506, 507], ', ')}")

    # Problem 2.2.1
    # print(f"\n2.2.1 convert_gravity_value -> float = {convert_gravity_value('1 standard')}")
    # print(f"\n2.2.1 convert_gravity_value -> None = {convert_gravity_value('N/A')}")
    # print(f"\n2.2.1 convert_gravity_value -> float = {convert_gravity_value('0.98')}")

    # PROBLEM 3
    # Problem 3.1.1 Call get_mandalorian_data()
    mandalorian_nevarro = get_mandalorian_data(mandalorian_planets, 'nevarro')
    mandalorian_arvala_7 = get_mandalorian_data(mandalorian_planets, 'ARVALA-7')

    # Problem 3.1.2 Write to file
    utl.write_json('stu-mandalorian_nevarro.json', mandalorian_nevarro)
    utl.write_json('stu-mandalorian_arvala_7.json', mandalorian_arvala_7)
    # print(mandalorian_nevarro)

    # Problem 3.2.1  Call create_planet
    swapi_tatooine = get_swapi_resource(SWAPI_PLANETS, {'search': 'Tatooine'})['results'][0]
    tatooine = create_planet(swapi_tatooine)
    # print(swapi_tatooine)

    # Problem 3.2.2 Write to file
    utl.write_json('stu-tatooine.json', tatooine)

    # PROBLEM 4
    # Problem 4.1.1 Call create_droid
    mandalorian_ig_11 = get_mandalorian_data(mandalorian_droids, 'ig-11')
    ig_11 = create_droid(mandalorian_ig_11)

    # Problem 4.1.2 Write to file
    utl.write_json('stu-ig_11.json', ig_11)

    # Problem 4.2.1 Call create_species
    swapi_human_species = get_swapi_resource(SWAPI_SPECIES, {'search': 'Human'})['results'][0]
    human_species = create_species(swapi_human_species)

    # Problem 4.2.2 Write to file
    utl.write_json('stu-human_species.json', human_species)

    # Problem 4.3.1 Test < create_person >
    mandalorian_din_djarin = get_mandalorian_data(mandalorian_people, 'Din Djarin')
    mando = create_person(mandalorian_din_djarin, mandalorian_planets)
    # print(mandalorian_din_djarin['species'])
    # print(get_swapi_resource(SWAPI_SPECIES, {'search': mandalorian_din_djarin['species']})['results'][0])

    # Problem 4.3.2 Write to file
    utl.write_json('stu-mando.json',mando)

    # PROBLEM 5
    # Problem 5.1.1 Call create_starship
    razor_crest = create_starship(get_mandalorian_data(mandalorian_starships, 'Razor Crest'))
    # print(razor_crest)
    # Problem 5.1.2  Write to file
    utl.write_json('stu-razor_crest.json', razor_crest)

    # Problem 5.2.1 Call create_vehicle
    swapi_sand_crawler = get_swapi_resource(SWAPI_VEHICLES, {'search': 'sand crawler'})['results'][0]
    sand_crawler = create_vehicle(swapi_sand_crawler)

    # Problem 5.2.2 Write to file
    utl.write_json('stu-sand_crawler.json', sand_crawler)

    # Problem 5.3.1 Call  board_passengers
    razor_crest = board_passengers(razor_crest, ['mando'])
    # print(razor_crest)

    # print(f"\n5.3.1 razor crest passengers on board = {razor_crest['passengers_on_board']}")

    # PROBLEM 6
    # 6.1.1 Call update_planets_visited
    update_planets_visited(razor_crest, mandalorian_nevarro['name'])
    # print(mandalorian_nevarro.keys())

    # print(f"\n6.1.1 razor crest visited planets = {razor_crest['planets_visited']}")

    # 6.2 Get Greef Karga
    greef_karga = create_person(get_mandalorian_data(mandalorian_people, 'greef karga'))
    # print(greef_karga)
    # print(get_mandalorian_data(mandalorian_people, 'greef karga'))

    # 6.2.1 Write to file
    utl.write_json('stu-greef_karga.json', greef_karga)

    # 6.3 Update planets_visited with Arvala-7
    update_planets_visited(razor_crest, 'Arvala-7')

    # print(f"\n6.3 razor crest visited planets = {razor_crest['planets_visited']}")

    # PROBLEM 7

    # 7.1.1 Get Kuiil
    ugnaught_species = [{
        "url": "https://starwars.fandom.com/wiki/Ugnaught",
        "name": "Ugnaught",
        "classification": "porcine humanoids",
        "designation": "sentient",
        "average_lifespan": 200,
        "average_height_cm": "Unkown",
        "language": "Ugnaught"
    }]

    kuiil = create_person(get_mandalorian_data(mandalorian_people, 'kuiil'), mandalorian_planets, ugnaught_species)
    utl.write_json('stu-kuiil.json', kuiil)

    # 7.2.1 Get Grogu
    grogu = create_person(get_mandalorian_data(mandalorian_people, 'grogu'))
    utl.write_json('stu-grogu.json', grogu)
    # print(grogu)

    # 7.2.2 Get hovering pram
    hovering_pram = create_vehicle(get_mandalorian_data(mandalorian_vehicles, 'Hovering Pram'))
    hovering_pram = board_passengers(hovering_pram, [grogu])
    utl.write_json('stu-grogu_hovering_pram.json', hovering_pram)
    # print(hovering_pram)

    # 7.3 Reprogram IG-11
    new_instructions = 'Protect Grogu and assist the Mandalorian'
    ig_11.update({'instructions': new_instructions})

    # Problem 7.3.1 Write to file
    utl.write_json('stu-ig_11_reprogrammed.json', ig_11)

    # PROBLEM 08
    # Problem 8.1 Update razor crest planets
    razor_crest = update_planets_visited(razor_crest, 'Sorgan')

    # print(f"\n8.1 razor crest visited planets = {razor_crest['planets_visited']}")

    # Problem 8.2 Get Cara
    cara_dune = create_person(get_mandalorian_data(mandalorian_people, 'Carasynthia Dune'))
    utl.write_json('stu-cara_dune.json', cara_dune)

    # Problem 8.3.1 Get Gideon
    gideon = create_person(get_mandalorian_data(mandalorian_people, 'gideon'))
    imperial_transport = create_starship(get_mandalorian_data(mandalorian_starships, 'imperial transport'))
    imperial_transport = board_passengers(imperial_transport, [gideon])
    utl.write_json('stu-gideon_imperial_transport.json', imperial_transport)

    # Problem 8.4 Update razor crest passengers
    board_passengers(razor_crest, [mando, grogu, cara_dune, ig_11])

    # PROBLEM 09
    # Problem 9.1 Test use of lambda
    board_passengers(razor_crest, [mando, grogu])
    razor_crest = update_planets_visited(razor_crest, 'Tattooine')

    # print(f"\n9.1 razor crest visited planets = {razor_crest['planets_visited']}")

    # Problem 9.2
    razor_crest['planets_visited'].sort(key=lambda x: x)
    # razor_crest['planets_visited'].sort(key=lambda razor_crest['planets_visited']: razor_crest['planets_visited'][0])
    utl.write_json('stu-razor_crest_departs.json', razor_crest)

    # PERSIST CACHE (DO NOT COMMENT OUT)
    utl.write_json(CACHE_FILEPATH, utl.cache)


if __name__ == '__main__':
    main()