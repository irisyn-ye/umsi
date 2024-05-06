
# There are two major objectives this week. First, learn how to join different dataset together.
# Second, how to manipulate data using 'dplyr'.

# JOINS
# Read in the data

library(readxl)
library(writexl)
library(dplyr)

data1 <- read_excel('data_a.xlsx')
data2 <- read_excel('data_b.xlsx')

airlines <- read.csv('airlines.csv')
flights <- read.csv('flights.csv')
planes <- read.csv('planes.csv')

colnames(airlines)
colnames(flights)
colnames(planes)

airlines_flights <- airlines %>%
  left_join(flights, by = 'carrier') 
airlines_flights %>% head(5)

airlines_flights <- airlines %>%
  inner_join(flights, by = 'carrier') 
airlines_flights %>% head(5)

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


