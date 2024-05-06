# installation
install.packages('dplyr')

# loading
library(dplyr)

# vectors
# atomic vector
# lists

# atomic vector
# create a vector
x = c(2, 3L, 6L, 8L, 10)
x

# type of vector
typeof(x)
# length of vector
length(x)

# use : operator
y = 2:10
y
typeof(y)
length(y)

# seq()
z = seq(2, 10, 2)
z

typeof(z)
length(z)

# logical vectors
logical_vector = c(TRUE, FALSE, TRUE, FALSE)
length(logical_vector)
typeof(logical_vector)

# integer 
integer_vector = c(2, 4L, 6L, 8L)
integer_vector

# character vector
character_vector = c("Maya", "Maisie", "Jess")
character_vector

first_table = c("Maya", "Maisie", "Jess")
first_table

# double vs. integer
five = 5L
typeof(five)

# access one element from a vector
x
# access first element from x
x[1]
# access second name from first table
first_table[3]

# access first all the way to third
x[1:3]
# access first and third only
x[c(1, 3)]

# update elements 
x
x[1]
x[2:5]

# what does this return
x[2:5] = seq(9, 18, 3)
x

# lists
example_list = list(TRUE, 2:5, c("a", "b", "c"))
length(example_list)
example_list

# access element in list
example_list[3]
example_list[[3]]

typeof(example_list[3])
typeof(example_list[[3]])

example_list[2]
example_list[[2]]

# change the first element in list
example_list[[1]] = c(TRUE, FALSE, TRUE, FALSE)
example_list

# add element 
example_list_new = append(example_list, "new element")
example_list_new

# remove element
example_list_new = example_list_new[-c(1,2)]
example_list_new

# remove another time
example_list_new = example_list_new[-c(1,2)]
example_list_new

# matrices
example_matrix = matrix(1:20, nrow = 5, ncol = 4)
example_matrix

# access first element
example_matrix[1]
# access first row as a whole
example_matrix[1, ]
# [row, col]

# access multiple rows
example_matrix[1:2, ]
example_matrix[c(1,2), ]

# access 1st and 3rd row 
example_matrix[c(1,3), ]

# access a specific number
example_matrix[2, 3]
# returns error because does not have 5th column
example_matrix[2, 5]

# add a column
example_matrix_new = cbind(example_matrix, 21:25)
example_matrix_new

# remove columns
example_matrix_deleted = example_matrix_new[ , -c(2, 4)]
example_matrix_deleted
