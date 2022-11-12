# SI 506 Lecture 04

# 1.0 STATEMENTS AND EXPRESSIONS

# CHALLENGE 01

# TODO variable assignments
banned_title = "Gender Queer: A Memoir"
banned_author = "Maia Kobabe"
banned_publisher = "(Lion Forge Comics, 2019)"


# CHALLENGE 02

# TODO Call print() function
print(banned_author, banned_title, banned_publisher)


# CHALLENGE 03

banned_book = banned_author + ', ' + banned_title + ' ' + banned_publisher

# TODO Call print() function
print(banned_book)


# 2.0 FORMATTED STRING LITERALS

# CHALLENGE 04

# TODO Call print() function passing in an f-string
print(f"{banned_book}\n< newline >")

# 3.0 OBJECT METHODS


# CHALLENGE 05

# TODO variable assignment
bluest_eye = "Toni Morrison, The Bluest Eye (Holt, Rinehard and Winston, 1970)"

# TODO Return length of string assign value to a variable
bluest_eye_len = len(bluest_eye)

# TODO Uncomment
# print(f"bluest_eye char count = {bluest_eye_len}\n")
print(f"bluest_eye char count = {bluest_eye_len}\n")

# CHALLENGE 06

hate_u_give = "Angie Thomas, The Hate You Give (Balzer + Bray, 2017)" # typo

# TODO uncomment
# print(f"hate_u_give (id={id(hate_u_give)} = {hate_u_give}\n")
print(f"hate_u_give (id={id(hate_u_give)} = {hate_u_give}\n")

# TODO Fix typo and assign value to a variable
hate_u_give = hate_u_give.replace("You", "U")

# TODO uncomment
# print(f"hate_u_give (id={id(hate_u_give)} = {hate_u_give}\n")
print(f"hate_u_give (id={id(hate_u_give)} = {hate_u_give}\n")

# CHALLENGE 07

stamped = "Ibram X. Kendi with Jason Reynolds, Stamped: Racism, Antiracism, and You (Little, Brown Books for Young Readers, 2020)"

# TODO Call string method and assign value to a variable
stamped_i_count = stamped.count('i')

# TODO uncomment
# print(f"stamped 'i' count = {stamped_i_count}\n")
print(f"stamped 'i' count = {stamped_i_count}\n")

# 4.0 ARITHMETIC OPERATIONS

# CHALLENGE 08

votes_cast = 3045
votes_yes = 1141
votes_no = 1904

votes_yes_pct = votes_yes / votes_cast # TODO Replace with arithmetic expression
votes_no_pct = votes_no / votes_cast # TODO Replace with arithmetic expression

# TODO uncomment
# print(f"Percentage yes vote = {votes_yes_pct:.2f}\n")
# print(f"Percentage no vote = {votes_no_pct:.2f}\n")


# CHALLENGE 09

pop_est_2021 = 9923
pop_under_18 = .316

eligible_voters = pop_est_2021 * (1 - pop_under_18) # TODO Replace with arithmetic expression
eligible_voters = int(eligible_voters) # TODO convert float to int

# TODO Uncomment
# print(f"Eligible voters = {eligible_voters}\n")

turnout_est_pct = votes_cast / eligible_voters # TODO Replace with arithmetic expression

# TODO Uncomment
# print(f"Percentage estimated turnout = {turnout_est_pct:.2f}\n")
