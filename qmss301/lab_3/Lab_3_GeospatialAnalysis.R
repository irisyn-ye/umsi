#WEEK 3 LABS - Geospatial Analysis

##### Loading the necessary libraries
library(sf)
# The simple features library provides classes and functions for reading, writing, manipulating, 
# and visualizing spatial data.
library(dplyr)

# Reading in the data
stops = read.csv("google_transit/stops.csv")
stop_times = read.csv("google_transit/stop_times.csv")

# Check or verify the class of the data
class(stops)
class(stop_times)

# We can use the `st_crs()` function to retrieve the coordinate reference system
# (CRS) from an sf object. The data imported from the shapefile uses the World
# Geodetic System (WGS 84) as its CRS, which has an EPSG code of 4326.
# epsg website: https://epsg.org/home.html

# Check CRS using st_crs function, gives NA even if Longitude and Latitude values are available since it is
# not a shapefile object
st_crs(stops)
st_crs(stop_times)

# Check column names of datasets
colnames(stops)
colnames(stop_times)

# The data imported from the CSV file is not an sf object, but it can be converted
# to an sf object by using the `st_as_sf()` function and specifying the columns
# of coordinate data. 
stops_to_sf = st_as_sf(x = stops,
                       coords = c("stop_lon", "stop_lat"))

# Check or verify the class of the data
class(stops_to_sf)

# Check if CRS exists even though it is a shapefile now
st_crs(stops_to_sf)

# Even though the data has now been converted to an sf object,
# we still need to set the CRS as WGS 84 using the EPSG code of 4326.

# set CRS
st_crs(stops_to_sf) = 4326
st_crs(stops_to_sf)

# Before we can proceed, we need to make sure that the data are using a projected
# CRS. We can verify this using the `st_is_longlat()` function since we know that
# latitude and longitude coordinates are not projected. 

st_is_longlat(stops_to_sf)
# TRUE if x has geographic(unprojected) coordinates, FALSE if it has projected coordinates

# When working with geographical data, it is necessary that the data has a projected CRS. 
# This is more important when you want to perform spatial analysis between two or more geospatial entities.

# Project them by transforming them
stops_to_sf_proj = st_transform(stops_to_sf, crs = 5623)

# verify projected CRS
st_is_longlat(stops_to_sf_proj)

# retrieve CRS
st_crs(stops_to_sf_proj)

# Practice Question

# The benefit of using the sf package is that it maintains the features of
# working with data frames in R, including the ability to use the dplyr package.

# Let's say we want to answer a research question based on this data, the main data you are working with
# is the 'stops_to_sf_proj' shapefile (remember that we converted 'stops.csv' to this shapefile). 

# We want to map out the bus stations and shade them by the number of buses that stop at each bus station.

# We would start by creating a join between our shapefile 'stops_to_sf_proj' and 'stop_times'. By which variable
# do you think we should make the join?

stops_times_combined = 
  stops_to_sf_proj %>%
  left_join(stop_times, by = "stop_id")

# Verify the join created
colnames(stops_times_combined)

# Check class of combined data
class(stops_times_combined)

# Check if it is projected
st_is_longlat(stops_times_combined) 

# How would you project it if it was not projected?

# Answer - stops_times_combined_proj = st_transform(stops_times_combined, crs = 5623)

# Check CRS of data 
st_crs(stops_times_combined)

# How would you use the dplyr functions shown to you to find out the number of buses/trips going 
# through a particular stop?

no_of_trips <- 
  stops_times_combined %>%
  group_by(stop_name) %>% 
  summarise(count_trips = n_distinct(trip_id)) %>% 
  arrange(desc(count_trips))

no_of_trips

# Print the stop name and its corresponding number of buses/trips, that has the highest number of buses/trips
# going through it
highest_trips_stop_name = 
  no_of_trips %>% 
  filter(count_trips == max(count_trips))

highest_trips_stop_name

# Lastly, if the trips going through a bus stop are greater than 70, categorize it as a "Popular" bus stop
# otherwise a "Not Popular" bus stop
final_table = 
  no_of_trips %>% 
  mutate(bus_stop_type = ifelse(count_trips > 70, "Popular", "Not Popular"))

final_table =
  final_table %>% 
  group_by(bus_stop_type) %>% 
  summarise(pop_count = n())

final_table  
