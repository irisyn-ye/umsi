# SI 506: Lecture 10

## Topics

1. Warmup
   1. Challenge 01
2. `if-elif-else` statements
   1. Challenge 02
3. Compound conditional statements
   1. Working with `None` or blank values
   2. Logical `and` operator
   3. Challenge 03
   4. Logical `or` operator
   5. Logical `not` operator
   6. Grouping related expressions
   7. Challenge 04

<br />

## Vocabulary

* __Boolean__. A type (`bool`) or an expression that evaluates to either `True` or `False`.
* __Conditional Statement__. A statement that determines a computer program's _control flow_ or the
  order in which particular computations are to be executed.
* __Index__. Numeric position of an element or item contained in an ordered sequence. Python
  indexes are zero-based, i.e., the first element's index value is 0 not 1.
  `len(< some_list >)` is considered an expression.
* __Iterable__. An object capable of returning its members one at a time. Strings, lists, and tuples
  are examples of an iterable.
* __Iteration__. Repetition of a computational procedure in order to generate a possible sequence of
  outcomes. Iterating over a `list` using a `for` loop is an example of iteration.
* __Operator__. A [symbol](https://www.w3schools.com/python/python_operators.asp) for performing
  operations on values and variables. The assignment operator (`=`) and arithmetic operators
  (`+`, `-`, `*`, `/`, `**`, `%`, `//`).
* __Subscript operator__. Square brackets (`[]`) enclosing either an index value or a slicing
  expression that is used to access individual or groups of sequence characters, elements or items.

<br />

## Reference

Open the following [w3schools](https://www.w3schools.com/) reference pages in your browser and
bookmark them. The pages provide useful summaries of `str`, `list`, and `tuple` methods.

1. w3schools, ["Python Built-in Functions"](https://www.w3schools.com/python/python_ref_functions.asp)
   or python.org ["Built-in Functions"](https://docs.python.org/3/library/functions.html).
2. w3schools, ["Python Operators"](https://www.w3schools.com/python/python_operators.asp).
3. w3schools, ["Python String Methods"](https://www.w3schools.com/python/python_ref_string.asp)
4. w3schools, ["Python List Methods"](https://www.w3schools.com/python/python_ref_list.asp)
5. w3schools, ["Python Tuple Methods"](https://www.w3schools.com/python/python_ref_tuple.asp).

<br />

## Lecture data

Today's lecture data was retrieved by accessing the US Department of Energy's
[National Renewable Energy Laboratory](https://www.nrel.gov/) (NREL)
[API](https://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/)
(Application Programming Interface). This involved utilizing the third-party Python
[Requests](https://requests.readthedocs.io/en/latest/) library to issue an HTTP GET request to
retrieve information about electric vehicle (EV) stations located in Ann Arbor and
Ypsilanti, Michigan.

Below is a list of data retrieved for this week's lectures. Note that it represents a
curated selection of information that can be sourced from the NREL's API.

| Column | Description |
| :----- | :---------- |
| id | Unique identifer assigned to a station |
| station_name | The name of the station |
| facility_type | Facility type |
| access_code | A description of who is allowed to access the station (public | private). |
| access_days_time | Hours of operation |
| restricted_access | For public stations, an indication of whether the station has restricted access, given as a boolean (true | false) |
| city | Municipality in which the station is located. |
| zip | The ZIP code (postal code) of the station's location. |
| street_address | The street address of the station's location. |
| intersection_directions | Brief additional information about how to locate the station. |
| ev_network | Network that maintains the station. |
| ev_connector_types | Connector type(s) available at the station. |
| ev_dc_fast_num | The number of DC Fast EVSE ports. |
| ev_level1_evse_num | The number of Level 1 EVSE ports. |
| ev_level2_evse_num | The number of Level 2 EVSE ports. |
| ev_other_evse | The number and type of additional EVSE ports, such as: SP Inductive - Small paddle inductive, LP Inductive - Large paddle inductive, and/or Avcon Conductive. |
| ev_pricing | Pricing details. |
| date_last_confirmed | The date the station's details were last confirmed. |

<br />

## 1.0 Warmup

Let's explore the EV `station_data` by completing a challenges.

<br />

## 1.1 Challenge 01

__Task__: Return a count of the number of Meijer-owned EV fuel stations. Meijer, Inc. is described
as a regional "supercenter" chain that was founded in 1934 in Greenville, MI.

1. Access the "headers" nested list element in `station_data` and assign the list to a variable
   named `headers`.

   :bulb: We will reference `headers` throughout today's lecture.

2. Employ slicing to access the fuel station nested list elements in `station_data` and assign the
   slice to a variable named `stations`.

   :bulb: We will reference `stations` throughout today's lecture.

3. Look up the index value of the `headers` element "station_name" by calling the appropriate list
   method. Assign the integer returned to a variable named `name_idx`.

4. Loop over `stations` employing a `for` loop and implement an `if` statement that identifies
   Meijer-owned fuel stations. If the conditional statement evaluates to `True`, increment the
   value of the "counter" variable `meijer_count` by one (`1`).

5. Uncomment `print()` and check your work.

<br />

## 2.0 `if-elif-else` conditions

Multiple conditions can be specified by including one or more `elif` conditions in between
an `if-else` block. The `if-elif-else` statement chain or ladder is executed from the top downwards.

```python
if < condition >:
    # < statement A >
    # ...
elif < condition >:
    < statement B >
    # ...
elif < condition >:
    < statement C >
    # ...
else:
    < statement D >
    # ...
```

The `else` statement is _optional_ but recommended, especially for new programmers, in order to
render explicit the conditional logic to be evaluated. You can also nest `if-elif-else` statement
blocks. We will explore nested conditional statements during a later lecture.

Note the use of three `elif` statements in the `while` loop below to check for specific
EV networks:

```python
chargepoint_count = 0
elec_america_count = 0
ev_connect_count = 0
evgo_count = 0
greenlots_count = 0

for station in stations:
    if station[ev_network_idx].lower() == 'chargepoint network':
        chargepoint_count += 1
    elif station[ev_network_idx].lower() == 'electrify america':
        elec_america_count += 1
    elif station[ev_network_idx].lower() == 'ev connect':
        ev_connect_count += 1
    elif station[ev_network_idx].lower() == 'evgo network':
        evgo_count += 1
    elif station[ev_network_idx].lower() == 'greenlots':
        greenlots_count += 1
    else:
        continue # explicit but optional
```

<br />

## 2.1 Challenge 02

__Task__. Employ `if-elif-else` conditional statements to populate four "last confirmed" annual
lists with station identifiers.

1. Use the four empty lists assigned to the variables `last_confirmed_2020`, `last_confirmed_2021`,
   `last_confirmed_2022`, and `last_confirmed_other` to accumulate stationidentifiers ("id") based
   on the station's "date_last_confirmed" year value.

   :bulb: The last confirm date is a string formatted as follows: `YYYY-MM-DD` (e.g., "2021-07-14")

2. Employ a `for` loop and the `range` type to loop over a sequence of numbers that is the same
   length of the `stations` list.

3. Inside the loop block employ subscript operator chaining to access:
   1. the `stations` nested list element (a fuel station) whose index position corresponds to the
      current integer being looped over (assigned to the loop variable `i` typically)
   1. and the last element in the nested list (i.e., the station's "date_last_confirmed" value).

   Assign the value to a variable (name is your choice).

4. Implement `if-elif-else` conditional statements that check the year (`YYYY`) in which the
   station data was last confirmed. If a station's data was last confirmed in 2020, append its "id"
   value to the `last_confirmed_2020` list. Add additional conditional statements to accumulate
   station ids for the years 2021 and 2022. Otherwise, if a station's data falls on either side of
   the years 2020-2022 append its "id" value to the "last_confirmed_other" list.

   For example, after you run your code the `last_confirmed_2021` list will contain the following
   ids:

   ```python
   ['42726', '44282', '44283', '44284', '44285', '44286', '102221', '184715', '184845', '184846', '198009']
   ```

5. Uncomment the calls to `print()` and `pp.print()` and check your work.


<br />

## 3.0 Compound conditional statements (comparing values using logical operators)

Recall that the expression which comprises an `if` statement returns either `True` or `False`.

You can combine conditions and compare values in a single `if` statement using the logical
operators `and` (conjunction), `or` (disjunction) and `not` (negation), either singly or together
in various combinations, as occurs in Boolean algebra.

:exclamation: When crafting a compound `if` statement you _must_ specify each condition in its
entirety.

For example the following compound `if` statement triggers a runtime exception:

```commandline
>>> x = 5
>>> x > 2 and < 10
  File "<stdin>", line 1
    x > 2 and < 10
              ^
SyntaxError: invalid syntax
```

The compound `if` statement _must_ be written as follows:

```command line
>>> x = 5
>>> x > 2 and x < 10
True
```

Or better yet (in this case):

```commandline
>>> x = 5
>>> 2 < x < 10
True
```

For example, if you want to check whether or not a charging station was equipped with between `2`
and `4` (inclusive) EVSE units, you should consider carefully how you craft
your compound `if` statement lest you trigger a runtime exception.

<br />

# 3.1 Working with None or blank values

Note that some "columns" in the data set include `None` values. The presence of `None` or blank
(`''`) values is problematic. Their presence requires that we tread carefully when calling either
object methods (e.g., `str.split()`) or built-in functions (e.g., calling `int()` to cast a string
to integer) as either operation can trigger a runtime exception.

The code below provides a couple of approaches for dealing with `None` values encountered checking a station's Level 2 Electric vehicle supply equipment (EVSE).

A quick check confirms the presence of `None` values:

```python
level2_evse_idx = headers.index('ev_level2_evse_num') # lookup index value
ev_level2_evse_num_vals = []
for station in stations:
    if station[level2_evse_idx] not in ev_level2_evse_num_vals:
        ev_level2_evse_num_vals.append(station[level2_evse_idx])
```

Two approaches are available to check for the presence of `None`:

* Employ the identity operators `is` or `is not`.
* Truth value test (discussed in depth next week)

```python
station_evse = []

# INCORRECT SYNTAX
for station in stations:
    # if statement will trigger SyntaxError: invalid syntax
    if station[level2_evse_idx] is not None and int(station[level2_evse_idx]) >= 2 and <= 4:
        station_evse.append(f"{station[1]}: Level2 EVSE = {station[level2_evse_idx]}")

# CORRECT SYNTAX
for station in stations:
    if station[level2_evse_idx] is not None and int(station[level2_evse_idx]) >= 2 and int(station[level2_evse_idx]) <= 4:
        station_evse.append(f"{station[1]}: Level2 EVSE = {station[level2_evse_idx]}")

# PYTHONIC (INCLUDES TRUTH VALUE TEST)
station_evse.clear() # delete elements (avoid duplication)
for station in stations:
    if station[level2_evse_idx] and 2 <= int(station[level2_evse_idx]) <= 4:
        station_evse.append(f"{station[1]}: Level2 EVSE = {station[level2_evse_idx]}")
```

Below is another example of how to avoid triggering runtime exceptions when inadvertantly calling object methods on `None`.

Let's say you need to return station locations featuring the highest number of Level 2 EVSEs. You should assume that multiple locations could meet this requirement. In other words, you need to account for the possibility that ties exist in the data. In addition, stations that lack information on Level 2 EVSEs return a value of `None` so you must
adopt a defensive coding strategy to avoid triggering a runtime exception if you attempt (inadvertently) to operate on a `None` value.

The code satisfies both concerns. During each iteration of the loop the following actions occur:

* If `station[level2_evse_idx]` resolves to `None` the `continue` statement is invoked and the `for` loop proceeds immediately to next loop iteration.

* Otherwise, the `station[level2_evse_idx]` is converted to an integer
  and compared to the previous `evse_count` value.

* If `num` is greater than `evse_count` a new "leader" has been detected
  and the `evse_count` is assigned `num` and any previous stations appended to the `most_evse` list are removed by calling the `list.clear()` method. The new "leader" is then appended to the list.

* However if `num` is equal to the previous `evse_count` value a tie has been detected. In this case, the current station is appended to the `most_evse` list joining the previous leader(s).

```python
most_evse = []
evse_count = 0

for station in stations:
    if station[level2_evse_idx] is None:
        continue # proceed to next station

    num = int(station[level2_evse_idx])
    if num > evse_count:
        evse_count = num # new
        most_evse.clear() # clear previous leader(s)
        most_evse.append(station) # new leader
    elif num == evse_count:
        most_evse.append(station) # tie
    else:
        continue # explicit but optional
```

<br />

## 3.2 Logical `and` operator

The logical `and` operator combines two or more conditions in a single boolean expression. _All_
conditions comprising the expression _must_ evaluate to `True` for the expression to evaluates to
`True`; otherwise the expression evaluates to `False`.

### Examples

```commandline
< condition > and < condition > [and ...]

>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
```

There are a number of U-M owned stations in the `stations` list. If we needed to filter
that group of stations by a particular zip code (say, `48104`) we could do so by writing a
compound `if` statement that employs the logical `and` operator to join the two conditions.

```python
zip_idx = headers.index('zip')

um_count_48104 = 0
i = 0
while i < len(stations):
    if stations[i][name_idx].startswith('U-M') and int(stations[i][zip_idx]) == 48104:
        um_count_48104 += 1
    i += 1
```

<br />

## 3.3 Challenge 03

__Task__. Employ a `for` loop to access a select subset of stations.

1. Look up the index value of the `headers` element "street_address" by calling the appropriate list
   method. Assign the integer returned to a variable named `street_idx`.

2. Assign an empty list to the variable `um_stations_greene_st`.

3. Implement a `for` loop and an `if` statement that filters on the following stations:

   * U-M owned stations
   * "Greene St" locations

   :exclamation: You _must_ compose a compound conditional statement using the logical `and`
   operator.

4. Add each station that satisfies _both_ of the specified conditions to the list
   `um_stations_greene_st`.

5. Uncomment `print()` and check your work.

<br />

## 3.4 Logical `or` operator

The logical `or` operator combines two or more conditions in a single boolean expression. If _any_
condition comprising the expression evaluates to `True` the expression evaluates to `True`;
otherwise the expression evaluates to `False`.

### Examples

```commandline
< condition > or < condition > [or ...]

>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
```

In the example below, we can accumulate stations owned by the Ann Arbor Downtown Development
Authority (A2DDA) by employing the logical `or` operator:

```python
a2dda_stations = []
for station in stations:
    name = station[name_idx]
    if name.startswith('A2DDA') or name.startswith('Ann Arbor Downtown Development Authority'):
        a2dda_stations.append(station[name_idx])
```

<br />

## 3.5 Logical `not` operator

The logical `not` operator reverses or negates a boolean expression. If the boolean expression
evaluates to `True` the inclusion of the logical `not` operator _reverses_ the value to `False`;
likewise if the boolean expression evaluates to `False` the inclusion of the logical `not` operator
_reverses_ the value to `True`.

:exclamation: note that the logical `not` operator reverses only the condition to which it is
paired. Reversing multiple conditions requires grouping the conditions with parentheses as
described below in the next section.

### Examples

```commandline
not < condition >

>>> not True
False
>>> not True and True
False
>>> not True or True
True
>>> not True and False
False
>>> not True or False
False
>>> not False
True
>>> not False and True
True
>>> not False or True
True
>>> not False or False
True
```

Most of the stations in the `stations` list are part of the ChargePoint network. If you
needed to accumulate a count of stations that are either non-networked or a member of another
network you can employ the logical `not` operator to _reverse_ the booelan expression
returned by the expression contained in the following `if` statement.

```python
# Count EV stations that not part of the ChargePoint network
station_count = 0
for i in range(len(stations)):
    if not stations[i][ev_network_idx] == 'ChargePoint Network':
        station_count += 1
```

:bulb: One could argue that employing the comparison operator not equal (`!=`) instead of the
logical `not` operator provides a more readable expression:

```python
stations[i][ev_network_idx] != 'ChargePoint Network'
```

<br />

## 3.6 Grouping related expressions

You can employ parentheses `()` to group related conditions that comprise a boolean expression.
Pairing the logical `not` operator with a group will reverse the grouped conditions but not
conditions outside the group.

:exclamation: Logical operator precedences is `not`, then `and`, then `or`.

### Examples

```commandline
< condition > and < condition > or < condition >
is equivalent to
(< condition > and < condition >) or < condition >

However

not < condition > and < condition > or < condition >
is equivalent to
not < condition > and (< condition > or < condition >)

>>> not False and False or False
False
>>> not False and (False or False)
False
```

If you needed to return a list of stations located in designated parking garages or parking lots
you could implement the following `while` loop:

```python
parking_facilities = []
i = 0
while i < len(stations):
    facility_type = stations[i][facility_type_idx]
    if (facility_type is not None
        and (facility_type.lower() == 'parking_garage'
            or facility_type.lower() == 'parking_lot'
            or facility_type.lower() == 'pay_garage')):
        parking_facilities.append(f"{stations[i][1]} {stations[i][2]} {stations[i][3]}")
    i += 1
```

:bulb: Note the use of parentheses (`()`) surrounding the expressions comprising the `if` statement.
Their presence permits the `if` statement to be written across multiple lines in order to enhance
readability.

The compound `if` statement could simplified by referencing the "facility_type" strings we wish to
target in a tuple. Instead of using a `while` loop we can instead loop over a sequence of numbers
supplied by the `range` type:

```python
parking_facilities = []
facility_types = ('parking_garage', 'pay_garage', 'parking_lot')
for i in range(len(stations)):
    facility_type = stations[i][facility_type_idx]
    if facility_type is not None and facility_type.lower() in facility_types:
        parking_facilities.append(f"{stations[i][1]} {stations[i][2]} {stations[i][3]}")
```

If there was a need to restrict the results to stations open to the public the original `if`
statement can be amended by adding an additional condition using the logical `and` operator. This
time we will employ a standard `for` loop to perform the looping:

```python
parking_facilities = []
for station in stations:
    facility_type = station[facility_type_idx]
    access_code = station[access_code_idx]
    if (facility_type is not None
        and (facility_type.lower() == 'parking_garage'
            or facility_type.lower() == 'parking_lot'
            or facility_type.lower() == 'pay_garage')
        and access_code.lower() == 'public'):
        parking_facilities.append(station)
```

:exclamation: Note that the compound statement groups the `or` conditions through the use of
parantheses (`()`) in order to ensure that the trailing `and` condition is evaluated correctly
given that the following conditions are not equivalent:

`(< expression > or < expression > or <expression >) and < expression > != < expression > or < expression > or <expression > and < expression >`

<br />

## 3.7 Challenge 04

__Task__. Create a list of all Ann Arbor Downtown Development Authority (A2DDA) stations located on
either Forest Ave or Maynard St.

1. Assign an empty list to a variable named `a2dda_stations`.

2. Loop over the `stations` list employing a standard `for` loop. Inside the loop block implement
   a compound conditional statement that enforces the following conditions:

   1. Station name is either "A2DDA" or "Ann Arbor Downtown Development Authority", and
   2. Station is located on either Forest Ave or Maynard St.

3. If the compound conditional statement evaluates to `True` append the following formatted string
   literal to `a2dda_stations`:

   `f"< station_name > < street_address >"`

   :bulb: Recall that both `name_idx` and `street_idx` are available for use in this challenge.

4. Uncomment `print()` and check your work.
