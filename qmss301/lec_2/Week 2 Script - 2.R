
# There are two major objectives this week. First, learn how to join different dataset together.
# Second, how to manipulate data using 'dplyr'.

# JOINS
# Read in the data

library(readxl)
library(writexl)
library(dplyr)

data1 <- read_excel('data_a.xlsx')
data2 <- read_excel('data_b.xlsx')



colnames(airlines)
colnames(flights)
colnames(planes)

data1
data2


# Left_join: Retains all the rows(observations) in the first(left) dataframe
new_data <- data1 %>% 
        left_join(data2, by = 'name')
new_data

# Right_join: Retains all the rows(observations) in the second(right) dataframe
new_data <- data1 %>% 
        right_join(data2, by = 'name')
new_data

# Inner_join: Joins using identical(common) rows(observations) in both dataframes
new_data <- data1 %>%
        inner_join(data2, by = 'name')
new_data

# Full_join: Retains all the rows(observations) in both dataframes.
new_data <- data1 %>% 
        full_join(data2, by = 'name')
new_data

# Save data
save(new_data, file = 'new_data')
write.csv(new_data, 'new_data.csv')
write_xlsx(new_data, 'new_data.xlsx')




# STUDENTS TASK


# DPLYR - FOR DATA MANIPULATION AND TRANSFORMATION


# SELECT() FUNCTION: Used to selects columns(Variables) in a dataframe

new_data
result <- new_data %>%
        select(name, sex, grade)
result

result <- new_data %>%
        select(name:grade)
result

result <- new_data %>%
        select(-major)
result

result <- new_data %>%
        select(starts_with('s'))
result


# FILTER() FUNCTION: Used to select rows(observations) that fulfills a condition.

new_data
short <- new_data %>% 
        filter(grade == 'A')
short

#OR

short <- new_data %>% 
        filter(age > 18)
short

# You can also use more than 1 conditions
short <- new_data %>% 
        filter(age > 18 & grade == 'A')
short

#### You can also use 
# <   Less than                    
# >   Greater than                 
# ==  Equal to                     
# <=  Less than or equal to        
# >=  Greater than or equal to     
# !=  Not equal to
# is.na   is NA
# !is.na  is not NA


### GROUP_BY() AND SUMMARISE() FUNCTIONS
new_data
groups <- new_data %>% 
        group_by(sex) %>% 
        summarize(average_age = mean(age)) %>% 
        na.omit()
groups

# Note: You can also group by more than one variables

# ARRANGE() FUNCTION
new_data
arr <- new_data %>% 
        arrange(age)
arr

new_data
arr <- new_data %>% 
        arrange(desc(age))
arr

# MUTATE() FUNCTION

new_data <- new_data %>%
        mutate(sex_dummy = ifelse(sex == "Male", 1, 2))


mute <- new_data %>% 
        mutate(exam = sex_dummy/age)
mute


