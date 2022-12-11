import copy
import five_oh_six as utl

# Cache
cache = utl.create_cache(utl.CACHE_FILEPATH)


def assign_crew_members(crew_size, crew_positions, personnel):
    """Returns a dictionary of crew members mapped (i.e., assigned) by position and limited in
    size by the < crew_size > value.

    The < crew_positions > and < personnel > lists must contain the same number of elements. The
    individual < crew_positions > and < personnel > elements are then paired by index position and
    stored in a dictionary structured as follows:

    {< crew_position[0] >: < personnel[0] >, < crew_position[1] >: < personnel[1] >, ...}

    WARN: The number of crew positions/members is limited by the < crew size > value. No additional
    crew positions/members are permitted to be assigned to the crew members dictionary even if
    passed to the function. Crew positions/members are assigned to the dictionary as key-value pairs
    by index position (0, 1, ...).

    A single line dictionary comprehension is employed to create the new crew members dictionary.

    Parameters:
        crew_size (int): max crew members permitted
        crew_positions (list): crew positions (e.g., 'pilot', 'copilot', etc.)
        personnel (list): flight crew to be assigned to the crew positions

    Returns:
        dict: crew members by position
    """

    # crew_assignment = {}
    # for i in range(crew_size):
    #     crew_assignment[crew_positions[i]] = personnel[i]
    return {crew_positions[i]: personnel[i] for i in range(crew_size)}


def board_passengers(max_passengers, passengers):
    """Returns a list of passengers that are permitted to board a starship or other vehicle. The
    size of the list is governed by the < max_passengers > value.

    WARN: The number of passengers permitted to board a starship or other vehicle is limited by the
    provided < max_passengers > value. If the number of passengers attempting to board exceeds
    < max_passengers > only the first < n > passengers (where `n` = "max_passengers") are permitted
    to board the vessel.

    Parameters:
        max_passengers (int): max number of passengers permitted to board a vessel
        passengers (list): passengers seeking permission to board

    Returns:
        dict: passengers to board
    """

    if max_passengers >= len(passengers):
        return passengers
    else:
        return passengers[:max_passengers]


def calculate_articles_mean_word_count(articles):
    """Calculates the mean (e.g., average) "word_count" of the passed in list of < articles >.
    Excludes from the calculation any article with a word count of zero (0) or < None >. Word counts
    are summed and then divided by the number of non-zero/non-< None > "word_count" articles. The
    resulting mean value is rounded to the second (2nd) decimal place and returned to the caller.

    The function maintains a count of the number of articles evaluated and a count of the total
    words accumulated from each article's "word_count" key-value pair.

    The function checks the truth value of each article's "word_count" before attempting to
    increment the count. If the truth vallue of the "word_count" is < False > the article is
    excluded from the count.

    Parameters:
        articles (list): nested dictionary representations of New York Times articles

    Returns:
        float: mean word count rounded to the second (2nd) decimal place
    """

    total_word_count = 0
    article_count = 0
    for article in articles:
        if article['word_count'] != 0 and article['word_count']:
            total_word_count += article['word_count']
            article_count += 1
            mean_word_count = round(float(total_word_count / article_count), 2)
    return mean_word_count


def convert_episode_values(episodes):
    """Converts select string values to either int, float, list, or None in the passed in list of
    nested dictionaries. The function delegates to the < utl.convert_to_* > functions the task of
    converting the specified strings to either int, float, or list (or None if utl.convert_to_none
    is eventually called).

    The truth value of each nested < episode > dictionary's value is first checked; if < False > the
    expression is negated to permit mapping (i.e., assigning) < None > to the associated episode
    key. Otherwise, various < utl.convert_to_*() > functions are called as necessary in an attempt
    to convert certain episode values to more appropriate types per the "Type conversions" listed
    below.

    Type conversions:
        series_season_num (to int)
        series_episode_num (to int)
        season_episode_num (to int)
        episode_prod_code (to float)
        episode_us_viewers_mm (to float)
        episode_writers (to list)

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        list: nested episode dictionaries containing mutated key-value pairs
    """

    for episode in episodes:
        for key, val in episode.items():
            if val:
                if 'num' in key:
                    episode[key] = utl.convert_to_int(val)
                elif key == 'episode_prod_code' or key == 'episode_us_viewers_mm':
                    episode[key] = utl.convert_to_float(val)
                elif key == 'episode_writers':
                    episode[key] = utl.convert_to_list(val, ', ')
            else:
                episode[key] = utl.convert_to_none(val, utl.NONE_VALUES)
    return episodes
    # for episode in episodes:
    #     if episode:
    #         if has_viewer_data(episode):
    #             episode['series_season_num'] = utl.convert_to_int(episode['series_season_num'])
    #             episode['series_episode_num'] = utl.convert_to_int(episode['series_episode_num'])
    #             episode['season_episode_num'] = utl.convert_to_int(episode['season_episode_num'])
    #             episode['episode_prod_code'] = utl.convert_to_float(episode['episode_prod_code'])
    #             episode['episode_us_viewers_mm'] = utl.convert_to_float(episode['episode_us_viewers_mm'])
    #             episode['episode_writers'] = utl.convert_to_list(episode['episode_writers'])
    #         else:
    #             episode['series_season_num'] = utl.convert_to_int(episode['series_season_num'])
    #             episode['series_episode_num'] = utl.convert_to_int(episode['series_episode_num'])
    #             episode['season_episode_num'] = utl.convert_to_int(episode['season_episode_num'])
    #             episode['episode_prod_code'] = utl.convert_to_float(episode['episode_prod_code'])
    #             episode['episode_us_viewers_mm'] = None
    #             episode['episode_writers'] = utl.convert_to_list(episode['episode_writers'])
    # return episodes


def count_episodes_by_director(episodes):
    """Constructs and returns a dictionary of key-value pairs that associate each director with a
    count of the episodes that they directed. The director's name comprises the key and the
    associated value a count of the number of episodes they directed. Duplicate keys are NOT
    permitted.

    Format:
        {
            < director_name_01 >: < episode_count >,
            < director_name_02 >: < episode_count >,
            ...
        }

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        dict: a dictionary that store counts of the number of episodes directed
              by each director
    """
    director_episodes = {}
    for episode in episodes:
        if episode['episode_director'] not in director_episodes.keys():
            director_episodes[episode['episode_director']] = 1
        else:
            director_episodes[episode['episode_director']] += 1
    return director_episodes


def create_droid(data):
    """Returns a new "thinned" dictionary representation of a droid based on the passed in
    < data > dictionary, converting string values to more appropriate types whenever possible.

    < data > values that are members of < utl.NONE_VALUES > (case insensitive comparison)
    are first converted to < None > by calling < utl.convert_none_values > and returning
    a new dictionary. Once that task is accomplished other < utl.convert_to_*() > functions
    are called as necessary in an attempt to convert certain values to more appropriate types
    per the "Type conversions" and "New/repurposed key-value pairs" listed below. Key-value
    pairs that are retained, renamed, or added are listed below under "Key order".

    Type conversions:
        create_year (to dict)
        height (to float)
        mass (to float)
        equipment (to list)

    New/repurposed key-value pairs:
        create_date (dict): < create_year > converted
        height_cm (float): < height > converted
        mass_kg (float): < mass > converted

    Key order:
        url
        name
        model
        manufacturer
        create_date {
            year
            era
            }
        height_cm
        mass_kg
        equipment
        instructions

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """
    data = utl.convert_none_values(data, utl.NONE_VALUES)
    return {
        'url': utl.convert_to_none(data.get('url'), utl.NONE_VALUES),
        'name': utl.convert_to_none(data.get('name'), utl.NONE_VALUES),
        'model': utl.convert_to_none(data.get('model'), utl.NONE_VALUES),
        'manufacturer': utl.convert_to_none(data.get('manufacturer'), utl.NONE_VALUES),
        'create_date': utl.convert_to_year_era(data.get('create_year')),
        'height_cm': utl.convert_to_float(data.get('height')),
        'mass_kg': utl.convert_to_float(data.get('mass')),
        'equipment': utl.convert_to_list(data.get('equipment'), delimiter='|'),
        'instructions': utl.convert_to_none(data.get('instructions'), utl.NONE_VALUES)
    }


def create_person(data, planets=None):
    """Returns a new "thinned" dictionary representation of a person based on the passed in
    < data > dictionary, converting string values to more appropriate types whenever possible.

    < data > values that are members of < utl.NONE_VALUES > (case insensitive comparison)
    are first converted to < None > by calling < utl.convert_none_values > and returning
    a new dictionary. Once that task is accomplished other < utl.convert_to_*() > functions
    are called as necessary in an attempt to convert certain values to more appropriate types
    per the "Type conversions" and "New/repurposed key-value pairs" listed below. Key-value
    pairs that are retained, renamed, or added are listed below under "Key order".

    Both the person's "homeworld" and "species" values are used to retrieve "thinned" dictionary
    representations of the planet and species values. Retrieving the homeworld is delegated
    to the function < get_homeworld > while retrieving the species is delegated to the function
    < get_species >. If an optional Wookieepedia-sourced < planets > list is provided, the
    argument is passed on to < get_homeworld > for processing.


    Type conversions:
        birth_year (to dict)
        height (to float)
        mass (to float)
        homeworld (to dict)
        species (to dict)

    New/repurposed key-value pairs:
        birth_date (dict): < birth_year > converted
        height_cm (float): < height > converted
        mass_kg (float): < mass > converted

    Key order:
        url
        name
        birth_date
        height_cm
        mass_kg
        homeworld
        species
        force_sensitive

    Parameters:
        data (dict): source data
        planets (list): optional supplemental planetary data

    Returns:
        dict: new dictionary
    """
    data = utl.convert_none_values(data, utl.NONE_VALUES)
    
    return {
        'url': utl.convert_to_none(data.get('url'), utl.NONE_VALUES),
        'name': utl.convert_to_none(data.get('name'), utl.NONE_VALUES),
        'birth_date': utl.convert_to_year_era(data.get('birth_year')),
        'height_cm': utl.convert_to_float(data.get('height')),
        'mass_kg': utl.convert_to_float(data.get('mass')),
        'homeworld': get_homeworld(data.get('homeworld'), planets),
        'species': get_species(data.get('species')),
        'force_sensitive': utl.convert_to_none(data.get('force_sensitive'), utl.NONE_VALUES)
    }


def create_planet(data):
    """Returns a new "thinned" dictionary representation of a planet based on the passed in
    < data > dictionary, converting string values to more appropriate types whenever possible.

    < data > values that are members of < utl.NONE_VALUES > (case insensitive comparison)
    are first converted to < None > by calling < utl.convert_none_values > and returning
    a new dictionary. Once that task is accomplished other < utl.convert_to_*() > functions
    are called as necessary in an attempt to convert certain values to more appropriate types
    per the "Type conversions" and "New/repurposed key-value pairs" listed below. Key-value
    pairs that are retained, renamed, or added are listed below under "Key order".

    Type conversions:
        suns (to int)
        moon (to int)
        orbital_period (to float)
        diameter (to int)
        gravity (to float)
        climate (to list)
        terrain (to list)
        population (to int)

    New/repurposed key-value pairs:
        location (dict): {< region >, < sector >}
        orbital_period_days (float): < orbital_period > converted
        diameter_km (int): < diameter > converted
        gravity_std (float): < gravity > converted

    Key order:
        url
        name
        location {
            region
            sector
            }
        suns
        moons
        orbital_period_days
        diameter_km
        gravity_std
        climate
        terrain
        population

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """
    data = utl.convert_none_values(data, utl.NONE_VALUES)
    return {
        'url': utl.convert_to_none(data.get('url'), utl.NONE_VALUES),
        'name': utl.convert_to_none(data.get('name'), utl.NONE_VALUES),
        'location': {
            'region': utl.convert_to_none(data.get('region'), utl.NONE_VALUES),
            'sector': utl.convert_to_none(data.get('sector'), utl.NONE_VALUES)
        },
        'suns': utl.convert_to_int(data.get('suns')),
        'moons': utl.convert_to_int(data.get('moons')),
        'orbital_period_days': utl.convert_to_float(data.get('orbital_period')),
        'diameter_km': utl.convert_to_int(data.get('diameter')),
        'gravity_std': utl.convert_gravity_value(data.get('gravity')),
        'climate': utl.convert_to_list(data.get('climate'), delimiter=', '),
        'terrain': utl.convert_to_list(data.get('terrain'), delimiter=', '),
        'population': utl.convert_to_int(data.get('population'))
    }


def create_species(data):
    """Returns a new "thinned" dictionary representation of a species based on the passed in
    < data > dictionary, converting string values to more appropriate types whenever possible.

    < data > values that are members of < utl.NONE_VALUES > (case insensitive comparison)
    are first converted to < None > by calling < utl.convert_none_values > and returning
    a new dictionary. Once that task is accomplished other < utl.convert_to_*() > functions
    are called as necessary in an attempt to convert certain values to more appropriate types
    per the "Type conversions" and "New/repurposed key-value pairs" listed below. Key-value
    pairs that are retained, renamed, or added are listed below under "Key order".

    Type conversions:
        average_lifespan (to int)
        average_height (to float)

    New/repurposed key-value pairs:
        average_height_cm (float): < average_height > converted

    Key order:
        url
        name
        classification
        designation
        average_lifespan
        average_height_cm
        language

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """
    data = utl.convert_none_values(data, utl.NONE_VALUES)
    return {
        'url': utl.convert_to_none(data.get('url'), utl.NONE_VALUES),
        'name': utl.convert_to_none(data.get('name'), utl.NONE_VALUES),
        'classification': utl.convert_to_none(data.get('classification'), utl.NONE_VALUES),
        'designation': utl.convert_to_none(data.get('designation'), utl.NONE_VALUES),
        'average_lifespan': utl.convert_to_int(data.get('average_lifespan')),
        'average_height_cm': utl.convert_to_float(data.get('average_height')),
        'language': utl.convert_to_none(data.get('language'), utl.NONE_VALUES)
    }


def create_starship(data):
    """Returns a new "thinned" dictionary representation of a starship based on the passed in
    < data > dictionary, converting string values to more appropriate types whenever possible.

    < data > values that are members of < utl.NONE_VALUES > (case insensitive comparison)
    are first converted to < None > by calling < utl.convert_none_values > and returning
    a new dictionary. Once that task is accomplished other < utl.convert_to_*() > functions
    are called as necessary in an attempt to convert certain values to more appropriate types
    per the "Type conversions" and "New/repurposed key-value pairs" listed below. Key-value
    pairs that are retained, renamed, or added are listed below under "Key order".

    Assigning crews and passengers consitute separate operations.

    Type conversions:
        length (to float)
        max_atmosphering_speed (to int)
        hyperdrive_rating (to float)
        MGLT (to int)
        crew (to dict)
        passengers (to dict)
        armament (to list)
        cargo_capacity (to int)

    New/repurposed key-value pairs:
        length_m (float): < length > converted
        max_megalight_hr (int): < MGLT > converted
        propulsion (dict): {
            < hyperdrive_rating >,
            < max_megalight_hr >,
            < max_atmosphering_speed >
            }
        crew_size (int): < crew > converted
        crew (dict): {
            < crew_size >
            < crew_members >
            }
        max_passengers (int): < passengers > converted
        passengers_on_board (list)
        passengers (dict): {
            < max_passengers >,
            < on_board >
        }
        cargo_capacity_kg (int): < cargo_capacity > converted

    Key order:
        url
        name
        model
        starship_class
        manufacturer
        length_m
        propulsion {
            hyperdrive_rating
            max_megalight_hr
            max_atmosphering_speed
            }
        crew {
            crew_size
            crew_members
            }
        passengers {
            max_passengers
            on_board
            }
        cargo_capacity_kg
        consumables
        armament

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """

    data = utl.convert_none_values(data, utl.NONE_VALUES)
    return {
        'url': utl.convert_to_none(data.get('url'), utl.NONE_VALUES),
        'name': utl.convert_to_none(data.get('name'), utl.NONE_VALUES),
        'model': utl.convert_to_none(data.get('model'), utl.NONE_VALUES),
        'starship_class': utl.convert_to_none(data.get('starship_class'), utl.NONE_VALUES),
        'manufacturer': utl.convert_to_none(data.get('manufacturer'), utl.NONE_VALUES),
        'length_m': utl.convert_to_float(data.get('length')),
        'propulsion': {
            'hyperdrive_rating': utl.convert_to_float(data.get('hyperdrive_rating')),
            'max_megalight_hr': utl.convert_to_int(data.get('MGLT')),
            'max_atmosphering_speed': utl.convert_to_int(data.get('max_atmosphering_speed'))
        },
        'crew': {
            'crew_size': utl.convert_to_int(data.get('crew')),
            'crew_members': utl.convert_to_none(data.get('crew_members'), utl.NONE_VALUES)
        },
        'passengers': {
            'max_passengers': utl.convert_to_int(data.get('passengers')),
            'on_board': utl.convert_to_none(data.get('passengers_on_board'), utl.NONE_VALUES)
        },
        'cargo_capacity_kg': utl.convert_to_int(data.get('cargo_capacity')),
        'consumables': utl.convert_to_none(data.get('consumables'), utl.NONE_VALUES),
        'armament': utl.convert_to_list(data.get('armament'), delimiter=',')
    }


def get_homeworld(identifier, planets=None):
    """Attempts to retrieve a SWAPI representation of a home planet using the provided
    < identifier >. The < identifier > is assumed to be either a planet name (e.g., Dagobah) or a
    SWAPI planet URL (e.g., https://swapi.py4e.com/api/planets/5/).

    If the < identifier > commences with the substring "https://" the < identifier > is considered a
    URL and is passed to the function < get_swapi_resource() > as the < url > argument. Otherwise
    the < identifier > is assumed to be a planet name and is passed to < get_swapi_resource() > as a
    < params > value.

    If an optional Wookieepedia-sourced < planets > list is provided, the task of retrieving the
    appropriate nested dictionary is delegated to the function < get_wookieepedia_data() >.
    Processing < planets > only occurs if the passed in < identifier > is a planet name since
    < get_wookieepedia_data() > filters on planet names only.

    If a match is obtained the SWAPI homeworld dictionary is updated with the Wookieepedia
    planet data. The updated dictionary is then passed to the function < create_planet > for further
    processing. This results in a "thinned" dictionary representation of the planet which is then
    returned to the caller.

    Parameters:
        identifier (str): either a planet name or a SWAPI planet URL
        planets (list): optional supplemental planetary data

    Returns:
        dict: "thinned" dictionary representation of a planet
    """
    if 'http' in identifier:
        planet_update = get_swapi_resource(identifier)
    else:
        planet_update = get_swapi_resource(utl.SWAPI_PLANETS, {'search': identifier})['results'][0]

    if planets:
        planet_update.update(get_wookieepedia_data(planets, identifier))
    planet_update_final = create_planet(planet_update)
    return planet_update_final


def get_species(identifier):
    """Attempts to retrieve a SWAPI representation of a species using the provided < identifier >.
    The < identifier > is assumed to be either the species name (e.g., Wookiee), a SWAPI species URL
    (e.g., https://swapi.py4e.com/api/species/3/), or a < list > that holds the SWAPI species URL.

    The function checks the < identifer > type. If the < identifier > is a list rather than a
    string, the function accesses the first list element and assigns it to < identifier >.

    If the < identifier > commences with the substring "https://" the < identifier > is considered a
    URL and is passed to the function < get_swapi_resource() > as the < url > argument. Otherwise
    the < identifier > is assumed to be a species name and is passed to < get_swapi_resource() > as
    a < params > value.

    The SWAPI species dictionary is then passed to the function < create_species()` > for further
    processing. This results in a "thinned" dictionary representation of the species which is then
    returned to the caller.

    Parameters:
        identifier (str): either a planet name or a SWAPI planet URL

    Returns:
        dict: "thinned" dictionary representation of a species
    """

    # if type(identifier) == list:
    #     identifier = identifier[0]
    #     if identifier:
    #         try:
    #             species_update = create_species(get_swapi_resource(utl.SWAPI_SPECIES, {'search': identifier})['results'][0])
    #         except:
    #             species_update = create_species(get_swapi_resource(identifier))
    #     else:
    #         species_update = None
    # else:
    #     if identifier:
    #         try:
    #             species_update = create_species(get_swapi_resource(utl.SWAPI_SPECIES, {'search': identifier})['results'][0])
    #         except:
    #             species_update = create_species(get_swapi_resource(identifier))
    #     else:
    #         species_update = None
    # return species_update
    if isinstance(identifier, list):
        identifier = identifier[0]
        species_update = create_species(get_swapi_resource(identifier))
    else:
        try:
            species_update = create_species(get_swapi_resource(utl.SWAPI_SPECIES, {'search': identifier})['results'][0])
        except:
            species_update = create_species(get_swapi_resource(identifier))
    return species_update


def get_most_viewed_episode(episodes):
    """Identifies and returns a list of one or more episodes with the highest recorded
    viewership. Ignores episodes with no viewship value. Includes in the list only those
    episodes that tie for the highest recorded viewership. If no ties exist only one
    episode will be returned in the list. Delegates to the function < has_viewer_data >
    the task of determining if the episode includes viewership "episode_us_viewers_mm"
    numeric data.

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        list: episode(s) with the highest recorded viewership.
    """
    most_viewed = []
    starter_viewership = 0
    for episode in episodes:
        if has_viewer_data(episode):
            if episode['episode_us_viewers_mm'] > starter_viewership:
                most_viewed.clear()
                starter_viewership = episode['episode_us_viewers_mm']
                most_viewed.append(episode)
            elif episode['episode_us_viewers_mm'] == starter_viewership:
                most_viewed.append(episode)
    return most_viewed



def get_nyt_news_desks(articles):
    """Returns a list of New York Times news desks sourced from the passed in < articles >
    list. Accesses the news desk name from each article's "news_desk" key-value pair. Filters
    out duplicates in order to guarantee uniqueness.

    Delegates to the function < utl.convert_to_none > the task of converting "news_desk"
    values that equal "None" (a string) to None. Only news_desk values that are "truthy"
    (i.e., not None) are returned in the list.

    Parameters:
        articles (list): nested dictionary representations of New York Times articles

    Returns:
        list: news desk strings (no duplicates)
    """
    news_desk = []
    for article in articles:
        article['news_desk'] = utl.convert_to_none(article['news_desk'], utl.NONE_VALUES)
        if article['news_desk']:
            if article['news_desk'] not in news_desk:
                news_desk.append(article['news_desk'])
    return news_desk


def get_swapi_resource(url, params=None, timeout=10):
    """Retrieves a deep copy of a SWAPI resource from either the local < cache >
    dictionary or from a remote API if no local copy exists. Delegates to the function
    < utl.create_cache_key > the task of minting a key that is used to identify a cached
    resource. If the desired resource is not located in the cache, delegates to the
    function < get_resource > the task of retrieving the resource from SWAPI.
    A deep copy of the resource retrieved remotely is then added to the local < cache > by
    mapping it to a new < cache[key] >. The mutated cache is written to the file
    system before a deep copy of the resource is returned to the caller.

    WARN: Deep copying is required to guard against possible mutatation of the cached
    objects when dictionaries representing SWAPI entities (e.g., films, people, planets,
    species, starships, and vehicles) are modified by other processes.

    Parameters:
        url (str): a uniform resource locator that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict|list: requested resource sourced from either the local cache or a remote API
      """

    key = utl.create_cache_key(url, params)
    if key in cache.keys():
        return copy.deepcopy(cache[key]) # recursive copy of objects
    else:
        resource = utl.get_resource(url, params, timeout)
        cache[key] = copy.deepcopy(resource) # recursive copy of objects
        utl.write_json(utl.CACHE_FILEPATH, cache) # persist mutated cache

        return resource


def get_wookieepedia_data(wookiee_data, filter):
    """Attempts to retrieve a Wookieepedia sourced dictionary representation of a
    Star Wars entity (e.g., droid, person, planet, species, starship, or vehicle)
    from the < wookiee_data > list using the passed in filter value. The function performs
    a case-insensitive comparison of each nested dictionary's "name" value against the
    passed in < filter > value. If a match is obtained the dictionary is returned to the
    caller; otherwise None is returned.

    Parameters:
        wookiee_data (list): Wookieepedia-sourced data stored in a list of nested dictionaries
        filter (str): name value used to match on a dictionary's "name" value

    Returns
        dict|None: Wookieepedia-sourced data dictionary if match on the filter is obtained;
                   otherwise returns None
    """

    for wookiee_data_obj in wookiee_data:
        if wookiee_data_obj['name'].lower() == filter.lower():
            return wookiee_data_obj
    # return None


def group_nyt_articles_by_news_desk(news_desks, articles):
    """Returns a dictionary of "news desk" key-value pairs that group the passed in
    < articles > by their parent news desk. The passed in < news_desks > list provides
    the keys while each news desk's < articles > are stored in a list and assigned to
    the appropriate "news desk" key. Each key-value pair is structured as follows:

    {
        < news_desk_name_01 >: [{< article_01 >}, {< article_05 >}, ...],
        < news_desk_name_02 >: [{< article_20 >}, {< article_31 >}, ...],
        ...
    }

    Each dictionary that represents an article is a "thinned" version of the New York Times
    original and consists of the following key-value pairs ordered as follows:

    Key order:
        web_url
        headline_main (new name)
        news_desk
        byline_original (new name)
        document_type
        material_type (new name)
        abstract
        word_count
        pub_date

    Parameters:
        news_desks (list): list of news_desk names
        articles (list): nested dictionary representations of New York Times articles

    Returns
        dict: key-value pairs that group articles by their parent news desk
    """

    article_by_newsdesk = {}
    for news_desk in news_desks:
        for article in articles:
            # news_desk_val = []
            if article['news_desk'] == news_desk:
                article_thinned = {
                        'web_url': article['web_url'],
                        'headline_main': article['headline']['main'],
                        'news_desk': article['news_desk'],
                        'byline_original': article['byline']['original'],
                        'document_type': article['document_type'],
                        'material_type': article['type_of_material'],
                        'abstract': article['abstract'],
                        'word_count': article['word_count'],
                        'pub_date': article['pub_date']
                }
                if news_desk in article_by_newsdesk.keys():
                    article_by_newsdesk[news_desk].append(article_thinned)
                else:
                    article_by_newsdesk[news_desk] = [article_thinned]
    return article_by_newsdesk


def has_viewer_data(episode):
    """Checks the truth value of an episode's "episode_us_viewers_mm" key-value pair. Returns
    True if the truth value is "truthy" (e.g., numeric values that are not 0, non-empty sequences
    or dictionaries, boolean True); otherwise returns False if a "falsy" value is detected (e.g.,
    empty sequences (including empty or blank strings), 0, 0.0, None, boolean False)).

    Parameters:
        episode (dict): represents an episode

    Returns:
        bool: True if "episode_us_viewers_mm" value is truthy; otherwise False
    """

    if episode['episode_us_viewers_mm']:
        return True
    else:
        return False


def main():
    """Entry point for program.

    Parameters:
        None

    Returns:
        None
    """

    # 9.1 CHALLENGE 01

    # 9.1.2
    assert utl.convert_to_none('', utl.NONE_VALUES) == None
    assert utl.convert_to_none('N/A ', utl.NONE_VALUES) == None
    assert utl.convert_to_none(' unknown', utl.NONE_VALUES) == None
    assert utl.convert_to_none('Yoda', utl.NONE_VALUES) == 'Yoda'
    assert utl.convert_to_none(('41BBY', '19BBY'), utl.NONE_VALUES) == ('41BBY', '19BBY')

    # 9.1.4
    assert utl.convert_to_float('4') == 4.0
    assert utl.convert_to_float('506,000,000.9999') == 506000000.9999
    assert utl.convert_to_float('Darth Vader') == 'Darth Vader'

    # 9.1.6
    assert utl.convert_to_int('506') == 506
    assert utl.convert_to_int('506,000,000.9999') == 506000000
    assert utl.convert_to_int('Ahsoka Tano') == 'Ahsoka Tano'

    # 9.1.8
    assert utl.convert_to_list('Use the Force') == ['Use', 'the', 'Force']
    assert utl.convert_to_list('X-wing|Y-wing', '|') == ['X-wing', 'Y-wing']
    assert utl.convert_to_list([506, 507], ', ') == [506, 507]


    # 9.2 CHALLENGE 02

    # 9.2.2
    # TODO Get data
    clone_wars_episodes = utl.read_csv_to_dicts('data-clone_wars_episodes.csv')

    # 9.2.4
    # TODO Implement loop
    count = 0
    for clone_wars_episode in clone_wars_episodes:
        if has_viewer_data(clone_wars_episode):
            count += 1
    # print(f"\n9.2.4 Episodes w/viewership data (n={len(clone_wars_episodes)}) = {count}")


    # 9.3 Challenge 03

    # 9.3.2
    # TODO Call function
    clone_wars_episodes = convert_episode_values(clone_wars_episodes)
    # print(clone_wars_episodes)
    # TODO Write to file
    utl.write_json('stu-clone_wars-episodes_converted.json', clone_wars_episodes)


    # 9.4 Challenge 04

    # 9.4.2
    # TODO Call function
    most_viewed_episode = get_most_viewed_episode(clone_wars_episodes)

    # print(f"\n9.4.2 Most viewed episode = {most_viewed_episode}")


    # 9.5 Challenge 05
    # print(clone_wars_episodes)

    # 9.5.2
    # TODO Call function
    # director_episode_counts = count_episodes_by_director(clone_wars_episodes)

    # TODO Uncomment
    # BONUS: Sort by count (descending), last name (ascending)
    # director_episode_counts = {
    #     director: count
    #     for director, count
    #     in sorted(director_episode_counts.items(), key=lambda x: (-x[1], x[0].split()[-1]))
    #     }

    # TODO Write to file
    # utl.write_json('stu-clone_wars-director_episode_counts.json', director_episode_counts)


    # 9.6 CHALLENGE 06

    # 9.6.2
    # TODO Get data
    articles = utl.read_json('./data-nyt_star_wars_articles.json')
    # TODO Call function
    news_desks = get_nyt_news_desks(articles)
    # TODO Write to file
    utl.write_json('stu-nyt_news_desks.json', news_desks)


    # 9.7 CHALLENGE 07

    # 9.7.2
    # TODO Call function
    news_desk_articles = group_nyt_articles_by_news_desk(news_desks, articles)
    # TODO Write to file
    utl.write_json('stu-nyt_news_desk_articles.json', news_desk_articles)

    # 9.8 CHALLENGE 08

    # 9.8.2
    ignore = ('Business Day', 'Movies')

    # TODO Implement loop
    mean_word_counts = {}
    for key, val in news_desk_articles.items():
        if key not in ignore:
            mean_counts = calculate_articles_mean_word_count(val)
            mean_word_counts[key] = mean_counts

    # 9.8.3
    # TODO Write to file
    utl.write_json('stu-nyt_news_desk_mean_word_counts.json', mean_word_counts)


    # 9.9 CHALLENGE 09

    # 9.9.2
    # TODO Get data
    wookiee_planets = utl.read_csv_to_dicts('data-wookieepedia_planets.csv')
    # TODO Call functions
    wookiee_dagobah = get_wookieepedia_data(wookiee_planets, 'dagobah')
    # TODO Write to files
    utl.write_json('stu-wookiee_dagobah.json', wookiee_dagobah)
    
    wookiee_haruun_kal = get_wookieepedia_data(wookiee_planets, 'HARUUN KAL')
    utl.write_json('stu-wookiee_haruun_kal.json', wookiee_haruun_kal)


    # 9.10 CHALLENGE 10

    # 9.10.2
    assert utl.convert_none_values(
        {'a': '', 'b': 'none '}, utl.NONE_VALUES
        ) == {'a': None, 'b': None}
    assert utl.convert_none_values(
        {'a': 'UNKNOWN', 'b': 'Hoth'}, utl.NONE_VALUES
        ) == {'a': None, 'b': 'Hoth'}
    assert utl.convert_none_values(
        {'a': 'X-wing', 'b': ' n/a'}, utl.NONE_VALUES
        ) == {'a': 'X-wing', 'b': None}


    # 9.11 CHALLENGE 11

    # 9.11.2
    assert utl.convert_gravity_value('1 standard') == 1.0
    assert utl.convert_gravity_value('5STANDARD') == 5.0
    assert utl.convert_gravity_value('0.98') == 0.98
    assert utl.convert_gravity_value('N/A') == 'N/A'
    # print(utl.convert_gravity_value('N/A'))

    # 9.11.4
    # TODO Call functions
    swapi_tatooine = get_swapi_resource(utl.SWAPI_PLANETS, {'search': 'Tatooine'})['results'][0]
    # print(swapi_tatooine)
    wookiee_tatooine = get_wookieepedia_data(wookiee_planets, 'Tatooine')
    for key, val in wookiee_tatooine.items():
        if val:
            swapi_tatooine.update({key: val})

    tatooine = create_planet(swapi_tatooine)
    # TODO Write to file
    utl.write_json('stu-tatooine.json', tatooine)


    # 9.12 CHALLENGE 12

    # 9.12.2
    assert utl.convert_to_year_era('1032BBY') == {'year': 1032, 'era': 'BBY'}
    assert utl.convert_to_year_era('19BBY') == {'year': 19, 'era': 'BBY'}
    assert utl.convert_to_year_era('0ABY') == {'year': 0, 'era': 'ABY'}
    assert utl.convert_to_year_era('Chewbacca') == 'Chewbacca'
    # print(utl.convert_to_year_era('0ABY'))

    # 9.12.4
    # TODO Get data
    wookiee_droids = utl.read_json('data-wookieepedia_droids.json')
    swapi_r2_d2 = get_swapi_resource(utl.SWAPI_PEOPLE, {'search': 'R2-D2'})['results'][0] 
    wookiee_r2_d2 = get_wookieepedia_data(wookiee_droids, 'R2-D2')
    if wookiee_r2_d2:
        swapi_r2_d2.update(wookiee_r2_d2)
    # for key, val in wookiee_r2_d2.items():
    #     if val:
    #         swapi_r2_d2.update({key: val})
    # utl.convert_none_values(swapi_r2_d2, utl.NONE_VALUES)
    # TODO Call functions
    r2_d2 = create_droid(swapi_r2_d2)
    # TODO Write to file
    utl.write_json('stu-r2_d2.json', r2_d2)


    # 9.13 Challenge 13

    # 9.13.2
    # TODO Get data
    swapi_human_species = get_swapi_resource(utl.SWAPI_SPECIES, {'search': 'human'})['results'][0] 
    # TODO Call function
    human_species = create_species(swapi_human_species)
    # TODO Write to file
    utl.write_json('stu-human_species.json', human_species)


    # 9.14 Challenge 14

    # 9.14.2
    # TODO Get data
    swapi_anakin = get_swapi_resource(utl.SWAPI_PEOPLE, {'search': 'Anakin Skywalker'})['results'][0]
    # print(swapi_anakin)
    # TODO Call functions
    anakin_swapi_homeworld = get_homeworld(swapi_anakin['homeworld'])
    # TODO Write to files
    utl.write_json('stu-anakin_swapi_homeworld.json', anakin_swapi_homeworld)
    # print(swapi_anakin)

    wookiee_people = utl.read_json('data-wookieepedia_people.json')
    wookiee_anakin = get_wookieepedia_data(wookiee_people, 'Anakin Skywalker')
    if wookiee_anakin:
        swapi_anakin.update(wookiee_anakin)
    # for key, val in wookiee_anakin.items():
    #     if val:
    #         swapi_anakin.update({key: val})
    # utl.convert_none_values(swapi_anakin, utl.NONE_VALUES)
    # print(wookiee_anakin)
    # print(swapi_anakin)
    anakin_swapi_wookiee_homeworld = get_homeworld(swapi_anakin['homeworld'], wookiee_planets)
    # print(anakin_swapi_wookiee_homeworld)
    # print(create_planet(get_wookieepedia_data(wookiee_planets, swapi_anakin['homeworld'])))
    # print(create_planet(get_swapi_resource(utl.SWAPI_PLANETS, {'search': 'Tatooine'})['results'][0]))
    utl.write_json('stu-anakin_swapi_wookiee_homeworld.json', anakin_swapi_wookiee_homeworld)


    # 9.15 Challenge 15

    # 9.15.2
    # TODO Call functions
    # print(swapi_anakin['species'])
    anakin_swapi_species = get_species(swapi_anakin['species'])
    # TODO Write to files
    utl.write_json('stu-anakin_swapi_species.json', anakin_swapi_species)

    # 9.16 CHALLENGE 16

    # 9.16.2
    # TODO Call functions
    anakin = create_person(swapi_anakin, wookiee_planets)
    # print(wookiee_planets)
    # print(get_wookieepedia_data(wookiee_planets, swapi_anakin))
    # TODO Write to files
    utl.write_json('stu-anakin_skywalker.json', anakin)

    swapi_obi_wan = get_swapi_resource(utl.SWAPI_PEOPLE, {'search': 'Obi-Wan Kenobi'})['results'][0]
    wookiee_obi_wan = get_wookieepedia_data(wookiee_people, 'Obi-Wan Kenobi')
    if wookiee_obi_wan:
        swapi_obi_wan.update(wookiee_obi_wan)
    # for key, val in wookiee_obi_wan.items():
    #     if val:
    #         swapi_obi_wan.update({key: val})
    # utl.convert_none_values(swapi_obi_wan, utl.NONE_VALUES)
    # print(swapi_obi_wan)
    obi_wan = create_person(swapi_obi_wan, wookiee_planets)
    utl.write_json('stu-obi_wan_kenobi.json', obi_wan)


    # 9.17 CHALLENGE 17

    # 9.17.2
    # TODO Call functions
    wookiee_starships = utl.read_csv_to_dicts('data-wookieepedia_starships.csv')
    wookiee_twilight = get_wookieepedia_data(wookiee_starships, 'Twilight')
    twilight = create_starship(wookiee_twilight)
    # TODO Write to file
    utl.write_json('stu-twilight.json', twilight)


    # 9.18 CHALLENGE 18

    # 9.18.2.1
    # TODO Call functions
    swapi_padme = get_swapi_resource(utl.SWAPI_PEOPLE, {'search': 'Padmé Amidala'})['results'][0] 
    wookiee_padme = get_wookieepedia_data(wookiee_people, 'Padmé Amidala')
    if wookiee_padme:
        swapi_padme.update(wookiee_padme)
    # for key, val in wookiee_padme.items():
    #     if val:
    #         swapi_padme.update({key: val})
    padme = create_person(swapi_padme, wookiee_planets)
    # TODO Write to files
    utl.write_json('stu-padme_amidala.json', padme)

    swapi_c_3po = get_swapi_resource(utl.SWAPI_PEOPLE, {'search': ' C-3PO'})['results'][0] 
    wookiee_c_3po = get_wookieepedia_data(wookiee_droids, 'C-3PO')
    if wookiee_c_3po:
        swapi_c_3po.update(wookiee_c_3po)
    # for key, val in wookiee_c_3po.items():
    #     if val:
    #         swapi_c_3po.update({key: val})
    c_3po = create_droid(swapi_c_3po)
    utl.write_json('stu-c_3po.json', c_3po)

    twilight['passengers']['on_board'] = board_passengers(twilight['passengers']['max_passengers'], [padme, c_3po, r2_d2])


    # 9.19 CHALLENGE 19

    # 9.19.2
    # TODO Assign value
    twilight['crew']['crew_members'] = assign_crew_members(twilight['crew']['crew_size'], ['pilot', 'copilot'], [anakin, obi_wan])

    # 9.19.3.
    # TODO Assign value
    r2_d2['instructions'] = ["Power up the engines"]


    # 9.20 CHALLENGE 20

    # 9.20.1
    # TODO Create list
    # for wookiee_planet in wookiee_planets:
    #     wookiee_planet = create_planet(wookiee_planet)
    planets = [create_planet(wookiee_planet) for wookiee_planet in wookiee_planets]
    # print(planets)
    # TODO Sort list
    planets.sort(key=lambda x: x['name'], reverse=True)
    # planets.sort(key=lambda x: -x['name'])
    # TODO Write to file
    utl.write_json('stu-planets_sorted_name.json', planets)


    # 9.20.2
    # TODO Add instruction
    instruction_r2_d2 = f"Plot course for Naboo, {planets[5]['location']['region']}, {planets[5]['location']['sector']}"
    r2_d2['instructions'].append(instruction_r2_d2)
    # print(r2_d2)


    # 9.20.3 BONUS
    # TODO Sort list
    # planets_diameter_km = sorted(planets, key=lambda x: (-x['diameter_km'], x['name']))
    # planets_diameter_km = sorted(sorted(planets, key=lambda x: (x['diameter_km'] is not None, x['diameter_km']), reverse=True), key=lambda x: x['name'])
    planets_diameter_km = sorted(sorted(planets, key=lambda x: x['name']), key=lambda x: ((x['diameter_km'] is not None, x['diameter_km'])), reverse=True)
    # planets_diameter_km = sorted(planets, key=lambda x: ((x['diameter_km'] is not None, x['diameter_km'])), reverse=True)

    # TODO Write to file
    utl.write_json('stu-planets_sorted_diameter.json', planets_diameter_km)

    # 9.20.4
    # TODO Add instruction
    r2_d2['instructions'].append("Release the docking clamp")

    # 9.20.5
    # TODO Write to file
    utl.write_json('stu-twilight_departs.json', twilight)


if __name__ == '__main__':
    main()
