# Read in the data
library(dplyr)

# trips data 
trips <- read.csv('trips.csv')

# count number of columns
ncol(trips)

# count rows
nrow(trips)

# check column names
colnames(trips)

# unique service_id
trips %>% 
  select(service_id) %>% 
  unique()

# create new data set without the last four columns
trips_2 <- trips %>%
  select(-tail(names(trips), 4))
deleted_col_counts = ncol(trips) - ncol(trips_2)
deleted_col_counts

# what are columns in the new dataset
colnames(trips_2)

# print out direction_id
trips_2 %>%
  select(direction_id) %>%
  head(5)
# dummy variables 
trips_2 %>% 
  mutate(direction_text = ifelse(direction_id == 1, "outbound", "inbound")) %>%
  head(5)

trips_2_direction_text <- trips_2 %>% 
  mutate(direction_text = ifelse(direction_id == 1, "outbound", "inbound"))

trips_2_direction_text %>%
  head(5)

trips_2 %>%
  head(5)

# sample error
trips_2 %>%
  select(direction_text) %>%
  head(10)

# right way
trips_2_direction_text %>%
  select(direction_text) %>%
  head(5)

# count records of route 4 to "Washtenaw to YTC" direction
trips_2 %>%
  filter(route_id == 4 & trip_headsign == "Washtenaw to YTC") %>%
  count()

colnames(trips_2)

route_4_count <- trips_2 %>%
  filter(route_id == 4 & trip_headsign == "Washtenaw to YTC") %>%
  count()
route_4_count

# route data
routes <- read.csv("routes.csv")
colnames(routes)

# unique routes in routes dataset
routes %>% 
  head(5)

routes %>%
  select(route_id) %>%
  unique()

# count unique routes in the dataset
routes %>%
  select(route_id) %>%
  unique() %>%
  count()

# flights dataset
flights <- read.csv("flights.csv")

# how we can get the average duration of hours for all flights in a day
colnames(flights)

flights %>%
  head(5)

# handy summarize
flights %>%
  group_by(month, year, day) %>%
  summarise(avg_hour = mean(hour, na.rm = TRUE))
