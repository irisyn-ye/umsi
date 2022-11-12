# SI 506 Lecture 12

## TOPICS

1. Functions that call other functions
2. Truth value testing
   1. Conditional statements and truth values
3. Iterable packing and unpacking
   1. Triggering `ValueError` runtime exceptions
   2. Unpacking in a `for` loop
4. Challenges
   1. Challenge 01
   2. Challenge 02
   3. Challenge 03

<br />

## Vocabulary

* __Argument__. A value passed to a function or method that corresponds to a parameter defined for
  the function or method.
* __Caller__. The initiator of a function call.
* __Function__. A defined block of code that performs (ideally) a single task. Functions only run
  when they are explicitly called. A function can be defined with one or more _parameters_ that
  allow it to accept _arguments_ from the caller in order to perform a computation. A function can
  also be designed to return a computed value. Functions are considered "first-class" objects in the
  Python eco-system.
* __Iterable packing__. Assigning items to an iterable such as list or tuple.
* __Iterable unpacking__. Assigning list elements or tuple items to an equal number of variables in a single assignment. This feature of the language has now been extended to all _iterables_ including lists and sets.
* __Parameter__. A named entity in a function or method definition that specifies an argument that
  the function or method accepts.
* __Scope__. The part of a script or program in which a variable and the object to which it is
  assigned is visible and accessible.
* __Truth Value__. In Python any object can be tested for its
  [truth value](https://docs.python.org/3/library/stdtypes.html#truth-value-testing) using an `if`
  or `while` condition or when it is used as an operand in a
  [Boolean operation](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not).

<br />

## 1.0 Functions calling other functions

Ideally, a function should perform a single computational task, delegating all related tasks
to other functions to perform.

For example, say you were asked to identify cereals from the `cereal_ingredients` list that contain corn syrup.

```python
cereal_ingredients = [
    ['manufacturer', 'brand', 'ingredients'],
    ['Kellogg Company', 'Frosted Flakes', ('Milled Corn', 'Sugar', 'Malt Flavoring', 'High Fructose Corn Syrup', 'Salt')],
    ...,
    ['General Mills', 'Lucky Charms', ('Oats', 'Marshmallows', 'Sugar', 'Corn Syrup', 'Corn Starch')],
    ...,
    ['Post Consumer Brands', 'Grape-nuts', ('Whole Grain Wheat', 'Flour', 'Malted Barley Flour', 'Salt', 'Dried Yeast')]
    ]
```

A data structure review (a nested list) suggests that the problem needs to be broken down into several subproblems. This process is known as _decomposition_.

1. Loop over the "cereals" slice in `cereal_ingredients` (i.e., exclude the "headers" nested list). Each element encountered is a nested list that represents a cereal
2. During each loop iteration access the current cereal's "ingredients" tuple element.
3. Loop over the tuple of ingredients and filter on "corn syrup".
4. If an ingredient contains the substring "corn syrup", append the cereal to an accumulator list.

Decomposing the problem into subproblems suggests that two loops are required to access each cereal's ingredients. You could get at the data by implementing a nested loop (a future topic), or a `for` loop and a function, or two functions. The latter approach is
preferred because each function can perform a specific task that is then available for
"reuse" elsewhere in your program.

In the solution below the two functions are named `has_ingredient` and `get_cereals_by_ingredient`. The functions perform the following operations:

* `has_ingredients`: Indentifies whether or not an ingredient is a member of a cereal's tuple of ingredients. Performs a case insensitive string comparison that __matches part or all__ of a an ingredient name. If a match is obtained returns `True`; otherwise returns `False`.

* `get_cereals_by_ingredient`: Loops over list of cereals provided by the caller. Delegates to the function `has_ingredient` the task of identifying whether or not a cereal possesses a specified ingredient. If an ingredient match is obtained, adds the cereal list to an local accumulator list. After the loop terminates, the accumulator list is returned to the caller.

:bulb: Since `has_ingredient` returns either `True` or `False` the function call (an expression) can be embedded in an `if` statement.

```python
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

corn_syrup = get_cereals_by_ingredient(cereal_ingredients[1:], 'corn syrup')
```

<br />

## 2.0 Truth value testing

In Python every object can be tested for its
[_truth value_](https://docs.python.org/3/library/stdtypes.html#truth-value-testing). You can check
an object's truth value in an `if` or `while` statement or as an operand (i.e., the value the
operator operates on) in an `and`, `or` `not` Boolean operation. A value that evaluates to `True`
is considered _truthy_ while a value that evaluates to `False` is considered _falsy_.

For SI 506 the following values are considered "truthy" or "falsy":

| Type | Value | Truth value |
| :---- | :--- | :---------- |
| Nonetype | `None` | falsy |
| numeric (`int`, `float`) | non-zero | truthy |
| numeric (`int`, `float`) | 0, 0.0 | falsy |
| boolean | `True` | truthy |
| boolean | `False` | falsy |
| sequence (`list`, `range`, `tuple`, `str`) | non-empty | truthy |
| sequence (`list`, `range`, `tuple`, `str`) | empty | falsy |
| associative array (`dict`) | non-empty | truthy |
| associative array  (`dict`) | empty | falsy |

The following example demonstrates testing a list's truth value utilizing the built-in function `bool()` which accepts an object and returns either `True` or `False` per the standard truth value testing rules:

```python
def get_truth_value(val):
    return bool(val) # check's the object's truth value

fruity_pebbles = None
truth_value = get_truth_value(fruity_pebbles) # falsy

fruity_pebbles = []
truth_value = get_truth_value(fruity_pebbles) # falsy

fruity_pebbles = ['Post Consumer Brands', 'Fruity Pebbles', 27, 9.3]

truth_value = get_truth_value(fruity_pebbles) # truthy
```

<br />

# 2.1 Conditional statements and truth values

You can employ an `if` or `elif` statement to check an object's truth value. In the example below the function `convert_to_list` can be called to split a string into a list.
The function is defined with two parameters: `value` and `delimiter`. The optional `delimiter` parameter is assigned a default value of `None` because the `str.split()`method does not require that the caller provide a delimiter value. In other words, the caller of `convert_to_list` is not required to pass a delimiter string to the function as an argument because `str.split()` does not require its caller to provide a delimiter argument.

Whenever a function's parameter is assigned a default value of `None`, a truth value test should be performed in the function block. In the case of the function `convert_to_list` the `delimiter` value is truth-tested. If the conditional statement evaluates to `True` a _truthy_ `delimiter` value has been detected and it is passed to the `str.split()` method. If the conditional statement evaluates to `False`, a _falsy_ `delimiter` value has been detected and `str.split()` is called without passing it a `delimiter (i.e., split on a space).

```python
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
```

Consider the next example. The `while` loop below is designed to continue looping indefinitely as long as the `cereal` value remains _falsy_. The only way to break out of the loop
is when the provided input passed to the function `get_cereal()` matches a cereal name in `sugary_cereals` (a subset of `cereals`).

:bulb: Note that a `while` loop will only iterate so long as the loop expression evaluates to `True` (e.g., `while True:`). But in this case, looping needs to continue indefinitely while the `cereal` value (i.e., `None`) remains _falsy_. To achieve this, the logical operator `not` is employed to reverse the expression (e.g., `not cereal` evaluates to `True` when the input fails to match a sugary cereal). When `cereal` is _truthy_ (e.g, points to a non-empty tuple) the expression `not cereal` evaluates to `False` and the `while` loop terminates.

```python
cereal_sugar_data = [
    ('manufacturer', 'brand', 'serving_size_gm', 'sugar_gm'),
    ('Post Consumer Brands', 'Honey Bunches of Oats', 30, 6),
    ...,
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
```

<br />

## 3.0 Iterable packing and unpacking

Both lists and tuples can be "packed" and "unpacked".

_Packing_ a list or tuple involves assigning multiple list elements or tuple items to a single object.

```python
grape_nuts = ['Post Consumer Brands', 'Grape-nuts', 29, 4.4]
# Equivalent
grape_nuts = get_cereal(cereal_sugars, 'grape-nuts')
```

_Unpacking_ or multple assignment involves accessing multiple list elements or tuple items and assigning the values to an equal number of comma-separated variables positioned on a single line.

```python
manufacturer, cereal_brand, serving_size_gm, sugar_gm = grape_nuts
```

<br />

## 3.1 Triggering `ValueError` runtime exceptions

Multiple assignment requires that list elements or tuple items are mapped (e.g., assigned) to an
_equal_ number of variables. Mismatches on either side of the assignment operator (`=`)  will raise
a `ValueError` runtime exception.

```python
manufacturer, cereal_brand, sugar_gm = grape_nuts # triggers a runtime exception
manufacturer, cereal_brand, serving_size_gm, sugar_gm, rating = grape_nuts # triggers a runtime exception
```

:exclamation: Also make sure that the comma-separated variables employed in the unpacking operation are ordered correctly; otherwise unanticipated variable assigments will occur.

```python
# Variables ordered incorrectly
cereal_brand, manufacturer, sugar_gm, serving_size_gm = grape_nuts
```

<br />

# 3.2 Unpacking in a loop

Recall that every iteration of a `for` loop involves the _implicit_ assignment of a loop variable to an element or item between the `for` and `in` keywords. You are not limited to a single implicit assignment as is demonstrated below in the second `for` loop below:

```python
# Conventional unpacking
for cereal in cereal_sugars:
    manufacturer, brand, serving_size_gm, sugar_gm = cereal
    print(f"\nmanufacturer: {manufacturer}",
        f"\nBrand: {brand}",
        f"\nSugar content: {calculate_sugar_content(serving_size_gm, sugar_gm)}")

# Also an option
for manufacturer, brand, serving_size_gm, sugar_gm in cereal_sugars:
    print(f"\nmanufacturer: {manufacturer}",
        f"\nBrand: {brand}",
        f"\nSugar content: {calculate_sugar_content(serving_size_gm, sugar_gm)}")

```

<br />

## 4.0 Challenges

Five star product ratings systems are ubiquitious on the Web but are now regarded as highly problematic measures of customer satisfaction. One would expect the ratings to tend towards a normal distribution as the number of ratings increase (obeying the Law of Large Numbers). Instead, the ratings tend to exhibit an asymmetric bimodal distribution (the infamous J-curve) with respect to the distribution of responses with the curve heavily skewed in the direction of highly favorable ratings. Self-selection bias provides a partial explanation for this phenomenon (i.e., only people who love or hate a product opt to rate it--which suggests that a simpler thumbs up/down scale would better capture such sentiments).

Anyways, let's explore cereal ratings data sourced from Walmart.

```python
cereal_ratings_data = [
    ['manufacturer', 'brand', 'five_stars', 'four_stars', 'three_stars', 'two_stars', 'one_star'],
    ['Kellogg Company', 'Apple Jacks', 185, 21, 10, 4, 2],
    ...,
    ['General Mills', 'Wheaties', 215, 18, 5, 2, 12]
    ]
```

<br />

## 4.1 Challenge 01

__Task__. Implement a function that returns the ratings for a given cereal.

1. Implement a function named `get_ratings` that defines a single parameter:

   * `cereal` (list): represents a cereal brand and its 1 to 5 star ratings.

   __Requirements__

   1. The function _must_ return a list of the cereal's 1 to 5 star rating elements (e.g., `[185, 21, 10, 4, 2]`).

   :bulb: this function can be implemented with one line of code.

2. After implementing `get_ratings`, call the function `get_cereal` and pass the following
   arguments to it in __reverse__ order using __keyword arguments__:

   1. the `cereal_ratings` list
   2. the string "raisin bran"

   Assign the return value to a variable named `raisin_bran`.

3. Next, call `get_ratings` and pass `raisin_bran` to it as the argument. Assign the return value
   to a variable named `raisin_bran_ratings`.

4. Uncomment the `brand` assignment and `print()` and check your work.

<br />

## 4.2 Challenge 02

__Task__. Loop over the `cereal_ratings` list and accumulate values to a new list named `ratings_groups` that summarize each cereal's ratings as "favorable", "neutral", and "unfavorable".

1. The empty `rating_groups` list will serve as an accumulator.

1. Loop over the `cereal_ratings` list. For each cereal encountered call the function `get_ratings` and pass the cereal list to it as the argument.

2. _Unpack_ the return value (a `list`) into five local variables named: `five`, `four`, `three`, `two`, and `one`.

3. Access the rating counts and assign the values to the following local variables per the specified groupings:

   1. `favorable` = sum of the 5 star and 4 star rating counts
   2. `neutral` = 3 star rating count
   3. `unfavorable` = sum of the 2 star and 1 star rating counts

4. Construct an f-string using the function's local variables formatted as follows:

   ```python
   f"<cereal name> ratings: favorable=< favorable count >, neutral=< neutral count >, unfavorable=< unfavorable count >"
   ```

5. Append the string to the list `rating_groups`.

6. Uncomment `print()` and `pp.print()` and check your work.

<br />

## 4.3 Challenge 03

__Task__. Implement functions that aid in computing a favorability rating (percent value) for a given
cereal.

1. Replace the `pass` statement in the function `count_ratings` to ensure that the function increments the `count` value correctly.

2. Implement a function named `calculate_favorable_rating_pct` that defines a single parameter:

   * `cereal` (list): represents a cereal brand and its 1 to 5 star ratings.

   __Requirements__

   1. The function _must_ calculate a cereal's favorability rating based on the following equation:

   ```python
   (<5 star rating count> + <4 star rating count>) / < total ratings count> * 100
   ```

   2. The function _must_ delegate to `get_ratings` the task of retrieving a cereal's ratings.

   3. The function _must_ delegate to `count_ratings` the task of providing a total count of all ratings provided for a given cereal.

   4. After calculating the passed in cereal's favorability rating, return the percentage value to the caller.

3. After implementing `calculate_favorable_rating_pct`, call the function `get_cereal` and retrieve the nested list in `cereal_ratings` that represents the Honey Nut Cheerios brand. Assign the list to the variable named `honey_nut_cheerios`.

4. Next, call the function `calculate_favorable_rating_pct` and pass `honey_nut_cheerios` to it as the argument. Assign the return value to the variable `cheerios_fav_pct`.

5. Uncomment the `brand` assignment and `print()` and check your work.
