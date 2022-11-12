# Midterm

import csv


def calculate_vax_pct(target_demographic, census_demographic, precision=None):
    """Computes the < target_demographic > vaccination percentage by dividing the
    < target_demographic > by the < census_demographic > and multiplying the result by 100. The
    computed value is then rounded to the specified < precision > integer before returning the
    computed value to the caller.

    If the caller does not specify the number of decimal places, calling the built-in < round >
    function is performed without passing it the optional second argument. In such cases the value
    returned is the nearest integer value to the computed value (e.g., 506.78914 -> 507).
    Otherwise, the function returns a floating point number with the number of decimal places to
    include in the computed value determined by the passed in < precision > value.

    The < target_demographic > comprises a particular vaccinated demographic (e.g.,
    all residents, residents 12 years and older, residents 65 years and older). The
    < census_demographic > corresponds to the total population (vaccinated and unvaccinated) for the
    specified target demographic.

    Parameters:
        target_demographic (int): vaccinated residents total for the specified county population
                            group
        census_demographic (int): total census population (vaccinated and unvaccinated) for the
                                  specified county population group
        precision (int): optional number of decimal places to round the computed value. Default
                         value is None

    Returns:
        float|int: floating point number if the < precision > is specified; otherwise the
                    value returned is the nearest integer value to the computed value
    """

    pass # TODO Implement


def clean_data(county):
    """Mutates the passed in < county > list by converting whole numbers masquerading as
    strings to an integer. Loops over < county > and for each element encountered delegates
    to the function < convert_to_int > the task of attempting to convert the element from a
    string (str) to an integer (int). Assigns the return value to the current element. After
    the loop terminates the county list is returned to the caller.

    Parameters:
      county (list): county vaccination data

    Returns:
       list: mutated < county > list with string elements that represent whole numbers
             converted to integers
    """

    pass # TODO Implement


def convert_to_int(value):
    """Attempts to convert a string, number or boolean < value > to an int. If a runtime
    ValueError exception is encountered, the function returns the < value > unchanged.

    WARN: This function does not convert a float value masquerading as a string to an
    integer (e.g., '506.5' -> 506). This is due to presence of a non-numeric character
    (a period) in the string. That said, the function will happily convert a float to
    an integer (e.g., 506.5 -> 506)

    Parameters:
        value (str|bool|float): string, boolean, or float value to be converted

    Returns:
        int|any: returns int if value successfully converted; otherwise returns the value
                 unchanged
    """

    pass # TODO Implement


def count_vaccinated(counties, headers, header_items):
    """Provides a two-item tuple containing the statewide vaccination count for a given population
    demographic together with the corresponding census population total across all counties.

    Loops over the < counties > list. For each nested county list encountered, delegates to the
    function < get_attribute > the task of retrieving the county's vaccinated residents
    and census population totals (vaccinated and unvaccinated) for a specified demographic
    (e.g., all residents, residents between 5 and 17 years old, residents 65 years and older).
    The function < get_attribute > is called twice to retrieve the two values.

    The < header_items > tuple provides the header names required for the two < get_attribute >
    calls. < header_items > is ordered as follows:

    ( < vaccinated residents header >, < corresponding census population header >)

    The tuple returned by this function is ordered as follows:

    ( < vaccinated residents count >, < corresponding census population count >)

    Parameters:
        counties (list): list of county lists
        headers (list): column names sourced from the first row of the CSV file
        header_items (tuple): two-item tuple comprising column names sourced from < headers >
                              that are used to look up index values

    Returns:
        tuple: statewide vaccination and census counts for a given demographic

    """

    pass # TODO Implement


def get_attribute(county, headers, header):
    """Returns a < county > list element by looking up its index in the corresponding < headers >
    list using the < header > name as a filter.

    Parameters:
        county (list): county vaccination data
        headers (list): column names sourced from the first row of the CSV file
        header (str): column name sourced from < headers > that is used to look
                      up an index value

    Returns:
        any: element sourced from < county >. The value returned is usually a string but
             other return types are possible if the element has been mutated.
    """

    pass # TODO Implement


def get_county(counties, county_name):
    """Attempts to retrieve a nested "county" list from the passed in < counties > list by
    performing a string comparison between the nested list's county name value and the passed in
    < county_name > string. A case-insensitive string comparison is performed. If a match is
    obtained a list representing the county is returned to the caller; otherwise None is returned.

    Parameters:
        counties (list): list of lists. Each nested list represents an individual county
        county_name (str): name of a county

    Returns:
        list | None: county with a name value that matches the < county_name > or None if no match
                     was obtained.
    """

    pass # TODO Implement


def get_ur_scheme(ur_codes, county_name):
    """Returns the NCHS urban/rural classification scheme code and descriptors, comprising
    the < cbsa_title >, < ur_code > (converted to an int), and < ur_code_name > associated
    with the matching < county_name > value. Name matching is case-insensitive. If no match
    is obtained the function returns None.

    Delegates to the function < convert_to_int > the task of converting the < ur_code > to
    an integer.

    Parameters:
        ur_codes (list): nested lists of NCHS urban/rural codes and descriptors
        county_name (str): name of the county (e.g., 'Washtenaw County')

    Returns:
        tuple|None: three-item tuple comprising the < cbsa_title > (str), < code > (int),
                    and < code_name > (str) for a given county; otherwise None if no
                    match is obtained
    """

    pass # TODO Implment


def read_csv(filepath, encoding='utf-8', newline='', delimiter=','):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list of lists,
    wherein each nested list represents a single row from the input file.

    WARN: If a byte order mark (BOM) is encountered at the beginning of the first line of decoded
    text, call < read_csv > and pass 'utf-8-sig' as the < encoding > argument.

    WARN: if newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted fields
    may not be interpreted correctly by the csv.reader.

    Parameters:
        filepath (str): The location of the file to read
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested "row" lists
    """

    with open(filepath, 'r', encoding=encoding, newline=newline) as file_obj:
        data = []
        reader = csv.reader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)
        return data


def write_csv(filepath, data, headers=None, encoding='utf-8', newline=''):
    """
    Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted
    fields may not be interpreted correctly by the csv.reader. On platforms that utilize
    `\r\n` an extra `\r` will be added.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list | tuple): sequence to be written to the target file
        headers (seq): optional header row list or tuple
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding, newline=newline) as file_obj:
        writer = csv.writer(file_obj)
        if headers:
            writer.writerow(headers)
            for row in data:
                writer.writerow(row)
        else:
            writer.writerows(data)


def main():
    """Program entry point.

    Parameters:
        None

    Returns:
        None
    """

    # 9.1 CHALLENGE 01

    washtenaw_vax_rates = [
        ['Date', 'MMWR_week', 'Recip_County', 'Series_Complete_Yes', 'Series_Complete_Pop_Pct', 'Booster_Doses', 'Booster_Doses_Vax_Pct'],
        ['10/05/2022', 40, 'Washtenaw County', 266717, 72.6, 166848, 62.6],
        ['09/07/2022', 36, 'Washtenaw County', 265129, 72.1, 165052, 62.3],
        ['08/03/2022', 31, 'Washtenaw County', 263924, 71.8, 162532, 61.6],
        ['07/06/2022', 27, 'Washtenaw County', 263351, 71.6, 161285, 61.2],
        ['06/01/2022', 22, 'Washtenaw County', 262441, 71.4, 158801, 60.5],
        ['05/01/2022', 18, 'Washtenaw County', 261414, 71.1, 156630, 59.9],
        ['04/01/2022', 13, 'Washtenaw County', 260341, 70.8, 154744, 59.4],
        ['03/01/2022', 9, 'Washtenaw County', 258342, 70.3, 145886, 56.5],
        ['02/01/2022', 5, 'Washtenaw County', 255141, 69.4, 129506, 50.8],
        ['01/01/2022', 52, 'Washtenaw County', 251138, 68.3, 110569, 44.0],
        ['12/01/2021', 48, 'Washtenaw County', 245726, 66.8, None, None],
        ['11/01/2021', 44, 'Washtenaw County', 242688, 66.0, None, None],
        ['10/01/2021', 39, 'Washtenaw County', 230849, 62.8, None, None],
        ['09/01/2021', 35, 'Washtenaw County', 214233, 58.3, None, None],
        ['08/01/2021', 31, 'Washtenaw County', 209128, 56.9, None, None],
        ['07/01/2021', 26, 'Washtenaw County', 203868, 55.5, None, None],
        ['06/01/2021', 22, 'Washtenaw County', 185032, 50.3, None, None],
        ['05/01/2021', 17, 'Washtenaw County', 140623, 38.3, None, None],
        ['04/01/2021', 13, 'Washtenaw County', 76206, 20.7, None, None],
        ['03/01/2021', 9, 'Washtenaw County', 42605, 11.6, None, None],
        ['02/01/2021', 5, 'Washtenaw County', 17592, 4.8, None, None],
        ['01/01/2021', 53, 'Washtenaw County', 0, 0.0, None, None]
        ]

    vax_2022 = None # TODO slice

    vax_under_200k = None # TODO slice

    vax_even_months = None # TODO slice

    jan_2022_booster_pct = None # TODO slice


    # 9.2 CHALLENGE 02

    case_data = None
    case_headers = None
    case_counties = None

    case_ingham = None

    # TODO Implement loop

    region = (
        'genesee county',
        'lapeer county',
        'livingston county',
        'macomb county',
        'monroe county',
        'oakland county',
        'washtenaw county',
        'wayne county',
        'st. clair county'
        )
    region_cases = []

    # TODO Implement loop

    county_name = 'franklin county'
    has_county = None

    # TODO Implement loop and counter


    # 9.3 CHALLENGE 03

    case_jackson = None # TODO call function

    # 9.4 CHALLENGE 04

    # Add Anthony
    cases_idx = None

    # TODO call function and assign return value to element

    new_cases_idx = None

    # TODO call function and assign return value to element

    # TODO Uncomment
    # print(f"\n3.3 case_counties nested list mutated = {case_counties[37]}")


    # 9.5 CHALLENGE 05

    vax_county_data = None # TODO call function
    vax_headers = None
    vax_counties = None

    washtenaw = None # TODO call function

    washtenaw_vax_series_complete = None # TODO call function
    washtenaw_vax_series_complete = None # TODO call function


    # 9.6 CHALLENGE 06

    washtenaw_pop_total = None # TODO call function
    washtenaw_pop_total = None # TODO call function

    washtenaw_vax_series_complete_pct = None # TODO call function


    # 9.7 CHALLENGE 07

    # TODO Implement loop

    genesee = None # TODO call function
    genesee_vax_series_complete_5to17 = None # TODO call function
    genesee_pop_total_5to17 = None # TODO call function
    genesee_vax_series_complete_5to17_pct = None # TODO call function


    # 9.8 CHALLENGE 08

    header_items = None

    # TODO call function and unpack return value

    vax_total_18plus_pct = None # TODO call function


    # 9.9 CHALLENGE 09

    ur_data = None
    ur_headers = None
    ur_schemes = None

    # TODO Implement loop

    # TODO insert ur_headers elements into vax_headers

    # 9.10 CHALLENGE 10

    large_central_and_fringe_metro = None
    medium_and_small_metro = None
    micropolitan = None
    non_core = None

    # TODO Implement loop

    # TODO Call write_csv() (keyword args in reverse order)


# Do not modify or remove this if statement
if __name__ == '__main__':
    main()
