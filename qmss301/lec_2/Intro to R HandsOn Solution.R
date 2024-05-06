library(dplyr)


# Hands-on Session
flights <- read.csv('/Users/iye/Downloads/flights.csv')
# airlines <- read.csv('airlines.csv')

colnames(flights)

### Hands on 7

# Questions
# From flight data, create another dataframe which only contains the year, month, day, hour, origin, dest, tailnum and carrier.
# call the new dataframe 'flight2'.
# 1
flight2 <- flights %>%
        select(year:day, hour, origin, dest, tailnum, carrier, air_time, arr_delay, dep_delay)
colnames(flight2)

# Imagine that you don't need the 'origin' and 'dest' variables from the flight2 data,
# and at the same time you want to add the full airline names to it(flight2 data),
# Therefore, using thesame bunch of code, remove 'origin' and 'dest'
# from flight2 data and add the airline to the flight2 data with 'left_join'.

# 2
flight2 <- flight2 %>%
        select(-origin, -dest) %>%
        left_join(airlines, by = "carrier")


# From the flight data, select all flights on January 1st and name it 'jan1st' 
# Also, from the flight data, select all flights on Dec 25th and name it 'dec25th' 

# 3
jan1st <- flight2 %>% 
        filter(month == 1, day == 1)
jan1st

# 4
dec25th <- flight2 %>% 
        filter(month == 12 & day == 25)


# 5
# dep_delay column shows the flight departure delay (in minutes). Using the group_by and summarize functions, find the average departure delay
# in each day.
xxx <- flight2 %>% 
        group_by(year, month, day) %>% 
        summarize(delay = mean(dep_delay, na.rm = TRUE))

colnames(flights)


# 6
# Using the mutate function, create three new columns: 'gain', 'hours' and 'gain_per_hour'. 'gain' is the difference between arrival delay (arr_delay)
# and departure delay (dep_delay), 'hours' is arrival time (arr_time) divided by 60, while 'gain_per_hour' is 'gain' divided by 'hours'.
colnames(flight2)
flights <- mutate(flight2,
                  gain = arr_delay - dep_delay,
                  hours = air_time / 60,
                  gain_per_hour = gain / hours)

# 7

# Create a new column from the 'hours' column and call the new column 'duration'.
# For flights below 3 hours, let the duration be 'short flight', and for flights 3 hours and above, let the duration be 'long flight'.

flights <- flights %>% 
        mutate(duration = ifelse(hours < 3, 'short flight', 'long flight'))


# 8
# How many flights are 'short flight' and how many flights are 'long flight'.
table(flights$duration)



