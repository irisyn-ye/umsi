# SI 506 Lecture 11

# Note: removed cholesterol_mg and saturated_fat_mg key-value pairs from each
# cereal: all values equal 0 mg.

# 1.1 DEFINING A FUNCTION

def print_slogan():
    print('\n1.1 Snap, Crackle, Pop') # Kellogg's Rice Crispies slogan

# TODO Call function # call function
print_slogan()

# 1.2 DEFINING A FUNCTION WITH A PARAMETER

def print_slogan(slogan):
    print(f"\n1.2 {slogan}")

slogan = 'They’rrrre GR-R-REAT'
# TODO Call function
print_slogan(slogan)

# 1.3 MULTIPLE PARAMETERS

def format_slogan(name, slogan):
    return f"{name}: {slogan}"

cereal = 'Wheaties'
slogan = 'The Breakfast of Champions.'
wheaties_slogan = format_slogan(cereal, slogan) # TODO Call function  # positional arguments

# print(f"\n1.3.1 {wheaties_slogan}")

cereal = 'Trix'
slogan = 'Silly Rabbit. Trix are for Kids.' # General Mills Trix
trix_slogan = format_slogan(cereal, slogan) # TODO Call function

# print(f"\n1.3.2 {trix_slogan}")


# 1.4 ARGUMENT ORDER MATTERS (PASSED POSITIONALLY)

cereal = 'Lucky Charms'
slogan = 'They’re always after me lucky charms' # General Mills Lucky Charms leprechaun
lucky_charms = format_slogan(slogan, cereal) # TODO Call function # Oops! string reversed

# print(f"\n1.4 String reversed\n{lucky_charms}")


# 1.5 CHALLENGE 01
# Sugar contente sources: USDA, Cereal nutrition labels
# See also https://tools.myfooddata.com/nutrition-facts/785739/wt1/1

cereals = [
    ['manufacturer', 'brand', 'serving_size_gm', 'sugar_gm'],
    ['Post Consumer Brands', 'Honey Bunches of Oats', 30, 6],
    ['General Mills', 'Cocoa Puffs', 36, 13.4],
    ['Kellogg Company', 'Frosted Flakes', 41, 14.5],
    ['General Mills', 'Honey Nut Cheerios', 28, 9],
    ['Post Consumer Brands', 'Grape-nuts', 29, 4.4],
    ['Kellogg Company', 'Raisin Bran', 59, 18],
    ['General Mills', 'Cheerios', 28, 1.3],
    ['Kellogg Company', 'Fruit Loops', 39, 12],
    ['Post Consumer Brands', 'Shredded Wheat (original spoon size)', 49, 0.4],
    ['General Mills', 'Lucky Charms', 36, 13],
    ['Quaker Oats Company', "Cap'n Crunch", 27, 12],
    ['Post Consumer Brands', 'Fruity Pebbles', 27, 9.3],
    ['Kellogg Company', 'Corn Flakes', 29, 10],
    ['General Mills', 'Wheaties', 27, 4.1],
    ['Kellogg Company', 'Apple Jacks (reduced sugar)', 28, 8]
    ]

def get_cereals_by_company(cereal_brands, company):
    brands = []
    for cereal in cereal_brands[1:]:
        if cereal[0].lower().startswith(company.lower()):
            brands.append(cereal[1])
    return brands # TODO replace

post_cereals = get_cereals_by_company(cereals, 'POST') # Call function
kellogg_cereals = get_cereals_by_company(cereals, 'Kellogg') # Call function

# print(f"\n1.5.1 Post cereals = {post_cereals}")
# print(f"\n1.5.2 Kellogg's cereals = {kellogg_cereals}")


# 2.1 KEYWORD ARGUMENTS (ANY ORDER ACCEPTABLE)

general_mills_cereals = get_cereals_by_company(cereal_brands = cereals, company = 'general mills') # TODO Call function

# print(f"\n2.1 General Mills cereals = {general_mills_cereals}")


# 2.2 OPTIONAL PARAMETERS

def calculate_sugar_content(cereal_brand, precision=2):
    return round(cereal_brand[-1] / cereal_brand[-2], precision) # TODO replace

def get_cereal(cereal_brands, cereal_name):
    for cereal in cereal_brands[1:]:
        if cereal_name.lower() in cereal[1].lower():
            return cereal # TODO replace

# Retrieve cereal
# TODO Uncomment
cocoa_puffs = get_cereal(cereals[1:], 'Cocoa Puffs')

# Accept precision default value
# TODO Uncomment
cocoa_puffs_sugar = calculate_sugar_content(cocoa_puffs)
# calculate_sugar_content function has two parameters but the second one is defined so can be omitted

# print(f"\n2.2.1 Cocoa Puffs sugar content = {cocoa_puffs_sugar}")

# Override precision default value
# TODO Uncomment
cocoa_puffs_sugar = calculate_sugar_content(cocoa_puffs, 4) # override

# print(f"\n2.2.2 Cocoa Puffs sugar content = {cocoa_puffs_sugar}")

# Pass get_cereal() as an argument
# TODO Uncomment
cocoa_puffs_sugar = calculate_sugar_content(get_cereal(cereals, 'Cocoa Puffs'), 3)

# print(f"\n2.2.3 Cocoa Puffs sugar content = {cocoa_puffs_sugar}")


# 2.3 Skipping optional parameters

def calculate_sugar_content_v2(cereal_brand, format_pct=False, precision=2):
    if format_pct:
        return f"{cereal_brand[-1] / cereal_brand[-2] * 100:.{precision}f}%" # trailing % sign
    else:
        return round(cereal_brand[-1] / cereal_brand[-2], precision)

# TODO Uncomment
raisin_bran = get_cereal(cereals, 'raisin bran')

# 3 binds to wrong parameter; returns string
# TODO Uncomment
raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, 3)

# print(f"\n2.3.1 Raisin Bran sugar content (type={type(raisin_bran_sugar)}) = {raisin_bran_sugar}")

# Keyword argument binds 3 correctly, returns float
# TODO Uncomment
raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, precision=3)

# print(f"\n2.3.2 Raisin Bran sugar content (type={type(raisin_bran_sugar)}) = {raisin_bran_sugar}")

# Returns formatted string
# TODO Uncomment
raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, format_pct=True, precision=3)
raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, True, 3) # Alternative

# print(f"\n2.3.3 Raisin Bran sugar content (type={type(raisin_bran_sugar)}) = {raisin_bran_sugar}")


# 2.4 CHALLENGE 02

def get_cereal_attribute(cereal, headers, header='brand'):
    pass # TODO replace

def calculate_sugar_content_v3(serving_size_gm, sugar_gm, precision=2):
    pass # TODO replace


headers = cereals[0] # extract headers
cereals_max_sugar = []
max_sugar_content = 0

# TODO Implement loop

# print(f"\n2.4 Cereal max sugar content ({max_sugar_content}) = {cereals_max_sugar}")


# 3.0 VARIABLE SCOPE

# print(f"\n3.0.1 Globally-scoped variable slogan = {slogan}")

# TODO Uncomment. Triggers a NameError runtime exception.
# print(f"\n3.0.2 Locally-scoped variable brands = {brands}")

