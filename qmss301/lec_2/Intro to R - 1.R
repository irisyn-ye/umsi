####################################################################################
############### INTRODUCTION TO R #################################################
####################################################################################

############## DATA STRUCTURES IN R #########################

# 1. VECTORS: They are one-dimensional arrays that can hold elements of the same data types(e.g numeric, character, logical).

abc <- c(1, 2, 3, 4, 5)
class(abc)

xyz <- c("apple", "banana", "cherry")
class(xyz)

# Try changing number 5 in 'numeric_vector' to 'apple'

# 2. LIST: They are versatile data structures that can store elements of different data types, including other lists.
our_list <- list(42, "Hello", c(1, 2, 3), list(2,'no'))
class(our_list)


# 3. MATRICES: Matrices are two-dimensional data structures consisting of rows and columns.
# All elements in a matrix must be of the same data type.
our_matrix1 <- matrix(1:6, nrow = 2, ncol = 3)
our_matrix1
our_matrix2 <- matrix(c("A", "B", "C", "D", "E", "F"), nrow = 2, ncol = 3)
our_matrix2
class(our_matrix2)
# Arrays are multi-dimensional data structures that can have more than two dimensions.

# 4. DATAFRAMES: Data frames are two-dimensional tables where each column can be of a different data type.
# Dataframes are commonly used for structured data.

our_df <- data.frame(name = c("Alice", "Bob", "Charlie"),
                     age = c(25, 30, 22))
class(our_df)
class(our_df$name)
class(our_df$age)

######## PACKAGES AND LIBRARY ##################
# In R, packages are collections of functions, data sets, and documentation that extend the base functionality of R. 
# Think of packages as add-ons or plugins that provide specialized tools for specific tasks, such as data visualization,
# statistical analysis, machine learning, and more.
install.packages('dplyr')
library(dplyr)




########## IMPORTING DATA ########################
# Working Directory Vs. Working Environment
getwd()


our_data <- read.csv('C:/Users/kored/OneDrive/OTHERS/WINTER 2024/QMSS 301/Module 1 - Geo Spatial/Intro to R/iris.csv')

setwd("C:/Users/kored/OneDrive/OTHERS/WINTER 2024/QMSS 301/Module 1 - Geo Spatial/Intro to R")

our_data <- read.csv('iris.csv')
our_data1 <- read_excel('iris.xlsx')
# try use 'read.csv' to import '.xlsx' file.

library(readxl)

our_data1 <- read_excel('iris.xlsx')



######## EXPORTING DATA ####################

library(writexl)

save(our_data, file = 'xxxx.RData')
write_xlsx(our_data, 'xxxx.xlsx')
write.csv(our_data, file = 'xxxx.csv')

############# COMMON ERRORS ###################
# syntax errors
# mismatched data types
# case sensitivity
# failure to install or load necessary packages
# variable name errors
# incomplete code blocks



########################
# Name:
# Task:
########################

