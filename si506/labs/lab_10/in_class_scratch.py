# List Comprehension
list_1 = []
str_ = 'SI 506!'
for character in 'SI 506!':
    list_1.append(character)

print('List using for loop: ',list_1 ) 

list_2 = [char for char in 'SI 506!']
print('List using list comprehension: ',list_1 ) 

list_3 = [char for char in 'SI 506!' if char.isnumeric()]
print('List using list comprehension with if condition: ',list_3 )

list_4 = [char if not char.isnumeric() else int(char) for char in 'SI 506!']
print('List using list comprehension with if-else condition: ',list_4)

# Dictionary Comprehension
print('\n')
nums = [1, 2, 3, 4, 5]

dict_1 = {}
for number in nums:
    dict_1[number] = number*number ## or number**2

print('Dictionary of squares of numbers using for loop: ', dict_1)

dict_2 = {k: k**2 for k in nums}
print('Dictionary of squares of numbers using Dictionary comprehension: ', dict_2)

dict_month = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun'}
dict_3 = {key: value.upper() for key, value in dict_month.items()}
print('Manipulate Dictionary using Dictionary comprehension: ', dict_3)

age_dict = {'jack': 38, 'michael': 48, 'joy': 57, 'john': 33}
dict_4 = {k: v for (k, v) in age_dict.items() if v<40}
print('Dictionary comprehension with if: ', dict_4)

dict_5 = {k: ('old' if v > 40 else 'young') for (k, v) in age_dict.items()}
print('Dictionary comprehension with if-else: ', dict_5)

# Nested List Comprehension

my_list = [[1, 1, 1], [2, 4, 8], [3, 9, 27]]

n_list_1 = []
for i in range(1,4):
    temp_list = []
    for j in range(1,4):
        temp_list.append(i**j)
    n_list_1.append(temp_list)

print('Nested List using nested for loops: ', n_list_1)

n_list_2 = [[ i**j for j in range(1,4) ]for i in range(1,4)]
        
print('Nested List using nested List Comprehension: ', n_list_2)

nested_dict = {'first':{'a':1}, 'second':{'b':2}}
output_dict = {'first': {1.0}, 'second': {2.0}}

n_dict_1 = {}
for (outer_k, outer_v) in nested_dict.items():
    for (inner_k, inner_v) in outer_v.items():
        n_dict_1[outer_k] = float(inner_v)
        
print('Nested Dictionary using for loop: ',n_dict_1 )

n_dict_2 = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}
print('Nested Dictionary using Nested Dictionary comprehension: ',n_dict_2)

# Nested List and Dictionary comprehension

nested_dict = {'first':{'a':1, 'b':2, 'c':3}, 'second':{'b':2, 'd':4, 'e':5}}

n_dict_list = {outer_k: [inner_k for inner_k in outer_v.keys()] for outer_k, outer_v in nested_dict.items()}
print('Nested List and Dict Comprehension: ',n_dict_list)