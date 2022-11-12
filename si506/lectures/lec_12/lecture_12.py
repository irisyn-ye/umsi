# SI 506 Lecture 12

import pprint

# Instantiate a custom PrettyPrinter object
pp = pprint.PrettyPrinter(indent=1, width=100, compact=True)

def calculate_sugar_content(serving_size_gm, sugar_gm, precision=2):
    return round(sugar_gm / serving_size_gm, precision)

def get_cereal(cereals, cereal_name):
    for cereal in cereals:
        if cereal_name.lower() in cereal[1].lower():
            return cereal # match, exit loop immediately

def get_cereal_attribute(cereal, headers, header='brand'):
    return cereal[headers.index(header)]


# 1.0 FUNCTIONS CALLING OTHER FUNCTIONS

cereal_ingredients = [
    ['manufacturer', 'brand', 'ingredients'],
    ['Kellogg Company', 'Frosted Flakes', ('Milled Corn', 'Sugar', 'Malt Flavoring', 'High Fructose Corn Syrup', 'Salt')],
    ['Kellogg Company', 'Raisin Bran', ('Whole Grain Wheat', 'Raisins', 'Wheat Bran', 'Sugar', 'High Fructose Corn Syrup')],
    ['General Mills', 'Cheerios', ('Whole Grain Oats', 'Modified Corn Starch', 'Sugar', 'Salt')],
    ['General Mills', 'Cocoa Puffs', ('Whole Grain Corn', 'Sugar', 'Corn Syrup', 'Cornmeal', 'Canola and or Rice Bran Oil')],
    ['General Mills', 'Lucky Charms', ('Oats', 'Marshmallows', 'Sugar', 'Corn Syrup', 'Corn Starch')],
    ['Post Consumer Brands', 'Shredded Wheat (original spoon size)', ('Whole Grain Wheat',)],
    ['Post Consumer Brands', 'Grape-nuts', ('Whole Grain Wheat', 'Flour', 'Malted Barley Flour', 'Salt', 'Dried Yeast')]
    ]

def has_ingredient(ingredients, ingredient):
    for item in ingredients:
        if ingredient.lower() in item.lower():
            return True # exit function; terminates loop
    return False

def get_cereals_by_ingredient(cereals, ingredient):
    results = []
    for cereal in cereals:
        if has_ingredient(cereal[-1], ingredient):
            results.append(cereal)
    return results

corn_syrup = get_cereals_by_ingredient(cereal_ingredients[1:], 'corn_syrup') # TODO call function

# print(f"\n1.0 Cereals w/corn syrup = {corn_syrup}")


# 2.0 TRUTH VALUES

def get_truth_value(val):
    return bool(val) # check's the object's truth value

fruity_pebbles = None
truth_value = get_truth_value(fruity_pebbles) # falsy

# print(f"\n2.0.1 None truth value = {truth_value}")

fruity_pebbles = []
truth_value = get_truth_value(fruity_pebbles) # falsy

# print(f"\n2.0.2 Empty list truth value (length={len(fruity_pebbles)}) = {truth_value}")

fruity_pebbles = ['Post Consumer Brands', 'Fruity Pebbles', 27, 9.3]
truth_value = get_truth_value(fruity_pebbles) # truthy

# print(f"\n2.0.3 List truth value (length={len(fruity_pebbles)}) = {truth_value}")


# 2.1 CONDITIONAL STATEMENTS AND TRUTH VALUES

def convert_to_list(value, delimiter=None):
    if delimiter:
        return value.split(delimiter)
    else:
        return value.split() # default


post_cereal_data = [
    'Grape-nuts, 29, 4.4',
    'Shredded Wheat (original spoon size), 49, 0.4',
    'Fruity Pebbles, 27, 9.3'
]

post_cereals = []
for cereal in post_cereal_data:
    post_cereals.append(convert_to_list(cereal, ', '))

# print(f"\n2.0.4 Post cereals (n={len(post_cereals)}) = {post_cereals}")


# 2.1 WHILE LOOP/INPUT() TRUTH VALUE TESTING EXAMPLE

cereal_sugar_data = [
    ('manufacturer', 'brand', 'serving_size_gm', 'sugar_gm'),
    ('Post Consumer Brands', 'Honey Bunches of Oats', 30, 6),
    ('General Mills', 'Cocoa Puffs', 36, 13.4),
    ('Kellogg Company', 'Frosted Flakes', 41, 14.5),
    ('General Mills', 'Honey Nut Cheerios', 28, 9),
    ('Post Consumer Brands', 'Grape-nuts', 29, 4.4),
    ('Kellogg Company', 'Raisin Bran', 59, 18),
    ('General Mills', 'Cheerios', 28, 1.3),
    ('Kellogg Company', 'Fruit Loops', 39, 12),
    ('Post Consumer Brands', 'Shredded Wheat (original spoon size)', 49, 0.4),
    ('General Mills', 'Lucky Charms', 36, 13),
    ('Quaker Oats Company', "Cap'n Crunch", 27, 12),
    ('Post Consumer Brands', 'Fruity Pebbles', 27, 9.3),
    ('Kellogg Company', 'Corn Flakes', 29, 10),
    ('General Mills', 'Wheaties', 27, 4.1),
    ('Kellogg Company', 'Apple Jacks (reduced sugar)', 28, 8)
]

cereal_sugar_headers = cereal_sugar_data[0]
cereal_sugars = cereal_sugar_data[1:]

# Cereals with sugar content >= 35%
sugary_cereals = []
for cereal in cereal_sugars:
    serving_size_gm = get_cereal_attribute(cereal, cereal_sugar_headers, 'serving_size_gm')
    sugar_gm = get_cereal_attribute(cereal, cereal_sugar_headers, 'sugar_gm')
    if calculate_sugar_content(serving_size_gm, sugar_gm) >= 0.35:
        sugary_cereals.append(cereal)

# print(f"\n2.0.4 Sugery cereals (n={len(sugary_cereals)}) = {sugary_cereals}")

# TODO Uncomment while loop
prompt = '\nPlease name a cereal high in sugar: '
cereal = None
while not cereal:
    name = input(prompt)
    cereal = get_cereal(sugary_cereals, name) # attempt to match on name

    if cereal:
        brand_name = get_cereal_attribute(cereal, cereal_sugar_headers, 'brand')
        serving_size_gm = get_cereal_attribute(cereal, cereal_sugar_headers, 'serving_size_gm')
        sugar_gm = get_cereal_attribute(cereal, cereal_sugar_headers, 'sugar_gm')
        sugar_content = calculate_sugar_content(serving_size_gm, sugar_gm)

        print(f"\n2.0.4 One {serving_size_gm} gm serving of {brand_name}",
            f"contains {sugar_gm} gm of sugar ({sugar_content:.1%}).\n")
    else:
        prompt = '\nCereal not located. Please provide another cereal name: '


# 3.0 ITERABLE PACKING AND UNPACKING

# Packing
grape_nuts = ['Post Consumer Brands', 'Grape-nuts', 29, 4.4]
grape_nuts = get_cereal(cereal_sugars, 'grape-nuts') # equivalent expression

# Unpacking
# TODO Unpack -> ???? = grape_nuts
# manufacturer, cereal_brand, sugar_gm = grape_nuts

# print(f"\n3.0 grape-nuts unpacked:",
#     f"\nmanufacturer = {manufacturer}",
#     f"\ncereal_brand = {cereal_brand}",
#     f"\nserving_size_gm = {serving_size_gm}",
#     f"\nsugar_gm = {sugar_gm}")

# ValueError runtime exceptions triggered

# print(f"\n3.2.1 grape_nuts length = {len(grape_nuts)}")

# Triggers ValueError: too many values to unpack (expected 3)
# TODO Uncomment
# manufacturer, cereal_brand, sugar_gm = grape_nuts

# Triggers ValueError: not enough values to unpack (expected 5, got 4)
# TODO Uncomment
manufacturer, cereal_brand, serving_size_gm, sugar_gm, rating = grape_nuts

# Variables ordered incorrectly
# TODO Uncomment
cereal_brand, manufacturer, sugar_gm, serving_size_gm = grape_nuts

print(f"\n3.2.2 grape-nuts unpacked into wrong variables:",
    f"\nmanufacturer = {manufacturer}",
    f"\ncereal_brand = {cereal_brand}",
    f"\nserving_size_gm = {serving_size_gm}",
    f"\nsugar_gm = {sugar_gm}")


# 3.2 UNPACKING IN A FOR LOOP

# Conventional unpacking
# TODO Uncomment
print('\n3.3.1 for loop unpacking')
for cereal in cereal_sugars:
    manufacturer, brand, serving_size_gm, sugar_gm = cereal
    print(f"\nmanufacturer: {manufacturer}",
        f"\nBrand: {brand}",
        f"\nSugar content: {calculate_sugar_content(serving_size_gm, sugar_gm)}")

# Also an option
# TODO Uncomment
# print('\n3.3.2 for loop unpacking')
# unpack the list in the for loop
for manufacturer, brand, serving_size_gm, sugar_gm in cereal_sugars:
    print(f"\nmanufacturer: {manufacturer}",
        f"\nBrand: {brand}",
        f"\nSugar content: {calculate_sugar_content(serving_size_gm, sugar_gm)}")


# 4.0 CHALLENGES

cereal_ratings_data = [
    ['manufacturer', 'brand', 'five_stars', 'four_stars', 'three_stars', 'two_stars', 'one_star'],
    ['Kellogg Company', 'Apple Jacks', 185, 21, 10, 4, 2],
    ['Quaker Oats Company', "Cap'n Crunch", 49, 5, 3, 1, 1],
    ['Quaker Oats Company', "Cap'n Crunch's Crunch Berries", 196, 15, 6, 2, 4],
    ['General Mills', 'Cheerios', 1310, 95, 14, 11, 28],
    ['General Mills', 'Cinnamon Toast Crunch', 577, 46, 10, 5, 19],
    ['General Mills', 'Cocoa Puffs', 147, 9, 1, 2, 5],
    ['Kellogg Company', 'Corn Flakes', 467, 45, 9, 3, 10],
    ['Kellog Company', 'Frosted Flakes', 1465, 116, 37, 11, 35],
    ['Kellogg Company', 'Frosted Mini-Wheats', 883, 95, 18, 6, 26],
    ['Kellogg Company', 'Fruit Loops', 750, 84, 14, 6, 8],
    ['Post Consumer Brands', 'Fruity Pebbles', 170, 23, 8, 2, 7],
    ['Post Consumer Brands', 'Grape-Nuts', 322, 25, 3, 1, 15],
    ['Post Consumer Brands', 'Honey Bunches of Oats', 95, 7, 3, 1, 2],
    ['General Mills', 'Honey Nut Cheerios', 814, 64, 22, 8, 22],
    ['General Mills', 'Lucky Charms', 388, 38, 12, 3, 7],
    ['Kellogg Company', 'Raisin Bran', 946, 79, 21, 14, 30],
    ['General Mills', "Reese's Puffs", 184, 14, 10, 4, 3],
    ['Kellogg Company', 'Rice Krispies', 429, 31, 11, 5, 13],
    ['Post Consumer Brands', 'Shredded Wheat', 208, 13, 6, 5, 11],
    ['General Mills', 'Wheaties', 215, 18, 5, 2, 12]
    ]

cereal_ratings_headers = cereal_ratings_data[0]
cereal_ratings = cereal_ratings_data[1:]


# 4.1 CHALLENGE 01

def get_ratings(cereal):
    return cereal[2:] # TODO Implement

raisin_bran = get_cereal(cereal_ratings, 'raisin bran') # TODO Call function
raisin_bran_ratings = get_ratings(raisin_bran) # TODO Call function

# Print
brand = {get_cereal_attribute(raisin_bran, cereal_ratings_headers, 'brand')}
print(f"\n4.1 {brand} ratings = {raisin_bran_ratings}")


# 4.2 CHALLENGE 02

rating_groups = []

# TODO Implement loop
for cereal in cereal_ratings:
    five, four, three, two, one = get_ratings(cereal)
    favorable = five + four
    neutral = three
    unfavorable = two + one
    
    brand = get_cereal_attribute(cereal, cereal_ratings_headers, header='brand')
    string = f"{brand} ratings: favorable={favorable}, neutral={neutral}, unfavorable={unfavorable}"
    rating_groups.append(string)

# print(f"\n4.2 Rating groups (n={len(rating_groups)})")
# pp.pprint(rating_groups)


# 4.3 CHALLENGE 03

# Part of setup
def count_ratings(ratings):
    count = 0
    for rating in ratings:
        pass # TODO Increment
    return count


def calculate_favorable_rating_pct(cereal):
    ratings = get_ratings(cereal)
    fav_pct = (rating[0] + rating[1]) / count_ratings(ratings) * 100
    return fav_pct # TODO Implement


honey_nut_cheerios = get_cereal(cereal_ratings, 'honey nut cheerios') # TODO Call function
honey_nut_cheerios_fav_pct = calculate_favorable_rating_pct(cereal) # TODO Call function

# Print
# brand = get_cereal_attribute(honey_nut_cheerios, cereal_ratings_headers, 'brand')
# print(f"\n4.3 {brand} favorability rating = {honey_nut_cheerios_fav_pct:.2f}%")
