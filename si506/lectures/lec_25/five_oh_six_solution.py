# SI 506 Lecture 25

import copy
import csv
import json
import requests

from urllib.parse import quote, urlencode, urljoin


# Constants
CACHE_FILEPATH = './stu-cache.json'
SWAPI_ENDPOINT = 'https://swapi.py4e.com/api'
SWAPI_CATEGORIES = f"{SWAPI_ENDPOINT}/"
SWAPI_FILMS = f"{SWAPI_ENDPOINT}/films/"
SWAPI_PEOPLE = f"{SWAPI_ENDPOINT}/people/"
SWAPI_PLANETS = f"{SWAPI_ENDPOINT}/planets/"
SWAPI_SPECIES = f"{SWAPI_ENDPOINT}/species/"
SWAPI_STARSHIPS = f"{SWAPI_ENDPOINT}/starships/"
SWAPI_VEHICLES = f"{SWAPI_ENDPOINT}/vehicles/"


def convert_to_float(value):
    """Attempts to convert a string, number, or boolean < value > to a float. Can also convert
    numbers masquerading as strings that include one or more thousand separator commas
    (e.g., "5,000,000"). If a runtime AttributeError, TypeError (usually triggered by NoneType),
    or a ValueError exception is encountered, the function returns the value unchanged.

    Parameters:
        value (obj): string or number to be converted

    Returns:
        float|any: float if value successfully converted; otherwise returns value unchanged
    """

    try:
        return float(value.replace(',', ''))
    except (AttributeError, TypeError, ValueError):
        return value


def convert_to_int(value):
    """Attempts to convert a string, number boolean < value > to an int. Can also convert
    numbers masquerading as strings that include one or more thousand separator commas
    (e.g., "5,000,000"). If a runtime AttributeError, TypeError (usually triggered by NoneType),
    or a ValueError exception is encountered, the function returns the value unchanged.

    Parameters:
        value (str|int): string or number to be converted

    Returns:
        int|any: integer if value successfully converted else returns value unchanged
    """

    try:
        # return int(value.replace(',', '')) # Challenge 01 refactor
        return int(convert_to_float(value)) # Challenge 02 refactor
        # return int(float(value.replace(',', ''))) # Challenge 02 refactor
    except (AttributeError, TypeError, ValueError):
        return value


def convert_to_list(value, delimiter=None):
    """Attempts to convert a string < value > to a list using the provided < delimiter >. Removes
    leading/trailing spaces before converting < value > to a list. If a runtime AttributeError,
    TypeError (usually triggered by NoneType), or a ValueError exception is encountered, the
    function returns the value unchanged.

    Parameters:
        value (str): string to be split.
        delimiter (str): optional delimiter provided for splitting the string

    Returns:
         list|any: list if value successfully converted else returns value unchanged
    """

    try:
        if delimiter:
            return value.strip().split(delimiter)
        else:
            return value.strip().split()
    except (AttributeError, TypeError, ValueError):
        return value


def create_cache(filepath):
    """Attempts to retrieve cache contents written to the file system. If successful the
    cache contents from the previous script run are returned to the caller as the new
    cache. If unsuccessful an empty cache is returned to the caller.

    Parameters:
        filepath (str): path to the cache file

    Returns:
        dict: cache either empty or populated with resources from the previous script run
    """

    try:
        return read_json(filepath)
    except FileNotFoundError:
        return {}


def create_cache_key(url, params=None):
    """Returns a lowercase string key comprising the passed in < url >, and, if < params >
    is not None, the "?" separator, and any URL encoded querystring fields and values.
    Passes to the function < urllib.parse.urljoin > the optional < quote_via=quote >
    argument to override the default behavior and encode spaces with '%20' rather
    than "+".

    Example:
       url = https://swapi.py4e.com/api/people/
       params = {'search': 'Anakin Skywalker'}
       returns 'https://swapi.py4e.com/api/people/?search=anakin%20skywalker'

    Parameters:
        url (str): string representing a Uniform Resource Locator (URL)
        params (dict): one or more key-value pairs representing querystring fields and values

    Returns:
        str: Lowercase "key" comprising the URL and accompanying querystring fields and values
    """

    if params:
        return urljoin(url, f"?{urlencode(params, quote_via=quote)}").lower() # space replaced with '%20'
    else:
        return url.lower()


def get_resource(url, params=None, timeout=10):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provided the response object body is returned in the form on an "envelope" with the data
    payload of one or more entities to be found in ['results'] list; otherwise, response
    object body is returned as a single dictionary representation of the entity.

    Parameters:
        url (str): a uniform resource locator that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        return requests.get(url, params, timeout=timeout).json()
    else:
        return requests.get(url, timeout=timeout).json()


def read_csv_to_dicts(filepath, encoding='utf-8', newline='', delimiter=','):
    """Accepts a file path, creates a file object, and returns a list of
    dictionaries that represent the row values using the cvs.DictReader().

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, 'r', newline=newline, encoding=encoding) as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:
            data.append(line) # OrderedDict()
            # data.append(dict(line)) # convert OrderedDict() to dict
        return data


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


def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file
        ensure_ascii (str): if False non-ASCII characters are printed as is; otherwise
                            non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to encoded JSON

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)
