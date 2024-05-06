# ctrl/cmd+shift+C -> comment/uncomment
# ctrl/cmd+return -> run the specific line of code
# select the part of code you'd love to run
# use head() to limit the number of lines returned 

# load library
library(dplyr)

# trips data
trips <- read.csv('trips.csv')

# read column names
colnames(trips)
ncol(trips)

# number of rows 
nrow(trips)

# unique service id
trips %>% 
  select(service_id) %>%
  unique()

unique_service_id <- trips %>% 
  select(service_id) %>%
  unique()
# trips %>% select(service_id)
# trips %>% 
#   select(service_id)

# create new dataset without the last four columns
colnames(trips)

trips_2 <- trips %>%
  select(-tail(names(trips), 4))
deleted_col_counts = ncol(trips) - ncol(trips_2)
deleted_col_counts

# what columns are in the new dataset trips_2
colnames(trips_2)

trips_3 <- trips %>%
  select(head(names(trips), 1))
trips_3 %>% head(5)
colnames(trips)

trips_4 <- trips %>%
  select(tail(names(trips), 1))
trips_4 %>% head(5)
colnames(trips)

# convert dummy variable to semantic text
# direction_id is a dummy variable 
trips_2 %>% 
  select(direction_id) %>%
  head(10)

trips_2 %>% 
  mutate(direction_text = ifelse(direction_id == 1, "outbound", "inbound")) %>%
  head(5)

trips_2_direction_text <- trips_2 %>% 
  mutate(direction_text = ifelse(direction_id == 1, "outbound", "inbound"))

trips_2_direction_text %>%
  select(direction_text) %>%
  head(10)

trips_2 %>%
  select(direction_text) %>%
  head(10) # this should be error 
colnames(trips_2)

# count records of route 4 to "Washtenaw to YTC" direction
# route must be 4
# direction must be "Washtenaw to YTC"
route_4_count <- trips_2 %>%
  filter(route_id == 4 & trip_headsign == "Washtenaw to YTC") %>%
  count()
route_4_count

# trips_2 %>%
#   filter(route_id == 4 & trip_headsign == "Washtenaw to YTC")

# routes data
routes <- read.csv('routes.csv')
colnames(routes)
colnames(trips)

# unique routes in trips df 
trips_uniq_routes <- trips %>% 
  select(route_id) %>%
  unique()
trips_uniq_routes

# count unique routes in trips
trips_uniq_routes %>% count()
# count unique routes in routes 
routes %>% count()

routes %>%
  tail(1)
