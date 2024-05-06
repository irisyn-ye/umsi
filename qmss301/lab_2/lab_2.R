# install package

#install.packages("dplyr")
#("magrittr")

#install.packages("https://cran.r-project.org/src/contrib/Archive/rlang/rlang_1.0.5.tar.gz", repos = NULL, type="source")
remove.packages("rlang")

# load package
library(dplyr)
#library(magrittr)
#library(tidyverse)



# use c() function
x = c(2, 3L, 6, 8, 10)  # separate elements w/ commas
x

# type of vector
typeof(x)

# number of elements
length(x)

# use : operator
y = 2:10
y

# type of vector
typeof(y)

# use seq() function
z = seq(2, 10, 2)  # start, stop, step
z

# type of vector
typeof(z)

# logical
logical_vector = c(TRUE, FALSE, TRUE, FALSE)
typeof(logical_vector)
logical_vector

# integer
integer_vector = c(2, 4L, 6L, 8L)
typeof(integer_vector)
integer_vector

# double
double_vector = c(2, 4, 6, 8)
typeof(double_vector)
double_vector

# character
character_vector = c("a", "b", "c", "d")
typeof(character_vector)
character_vector

# vector
x

# access first element
x[1]

# access first to third elements
x[1:3]

# access first and third elements
x[c(1, 3)]

# change first element
x[1] = 3
x

# change remaining elements
x[2:5] = seq(9, 18, 3)
x

# change remaining elements
x[c(2,3,4, 5)] = seq(9, 18, 3)

# create list
example_list = list(TRUE, 2:5, c("a", "b", "c", "d"))
example_list

# length of list
length(example_list)

# access third element
example_list[[3]]

# change first element
example_list[[1]] =  c(TRUE, FALSE, TRUE, FALSE)
example_list

# add element
example_list = append(example_list, "new element")
example_list

# remove element
example_list = example_list[-c(1,2)]
example_list

# create matrix
example_matrix = matrix(1:20, nrow = 5, ncol = 4)
example_matrix

# dimension of matrix
dim(example_matrix)

# access element
example_matrix[1, 2]  # row, column

# access row
example_matrix[1, ]

# access multiple rows
example_matrix[c(1, 2), ]

# access column
example_matrix[, 2]

# access multiple columns
example_matrix[, c(1, 2)]

# add column
example_matrix = cbind(example_matrix, 21:25)
example_matrix

# remove columns
example_matrix = example_matrix[, -c(2, 4)]
example_matrix

# create data frame
sex = c("F", "M", "F")
age = c(20, 22, 24)
data = data.frame(sex, age)
data

# dimension of data frame
dim(data)

# access first column ([])
data[1]

# access second column ($)
data$age

# add height column
data = cbind(data, height_in = c(64, 76, 68))
data

# add weight column
data$weight_lbs = c(125, 130, 200)
data



# remove first and fourth columns
data = data[-c(1, 4)]
data

# read data
iris_df = read.csv("iris.csv")

# descriptive statistics
summary(iris_df)

# pipe operator (%>%)
iris_df %>% summary()

iris_df %>%
  select(species, sepal_length, sepal_width) %>%
  arrange(desc(sepal_length))

iris_df %>%
  mutate(versicolor = ifelse(species == "Iris-versicolor", 1, 0)) %>%
  select(species, versicolor)

iris_df %>%
  filter(sepal_width > 3) %>%
  arrange(sepal_width)

iris_df %>%
  group_by(species) %>%
  summarize(avg_petal_length = mean(petal_length),
            SD_petal_length = sd(petal_length),
            avg_petal_width = mean(petal_width),
            SD_petal_width = sd(petal_width))
