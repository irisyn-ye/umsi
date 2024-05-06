##################################
# Devanshi Shah
# QMSS 301 005
# Geospatial Analysis Project
# 28 Sept. 2023
##################################



# loading the libraries

library(sf)
library(dplyr)
library(tmap)
tmap_options(max.categories = 205) # I had to use this to fix an error with loading the tmap package!



# reading in the data

neighborhoods <- st_read("Neighborhoods.shp")
zipcodes <- st_read("zip_codes.shp")
grocery_stores <- st_read("Grocery_Stores_in_City_of_Detroit_Public_View.shp")
crime <- st_read("RMS_Crime_Incidents.shp")



# reproject the datasets

crime_proj <- st_transform(crime, crs = 5623)
zipcodes_proj <- st_transform(zipcodes, crs = 5623)
grocery_proj <- st_transform(grocery_stores, crs = 5623)
neighborhoods_proj <- st_transform(neighborhoods, crs = 5623)



# filtering crime data for 2021 only

crime_proj_filtered <- crime_proj %>%
  filter(year == 2021)



##### Task 1 #####



### 1 ###



# using st_within to map 2021 crimes over neighborhoods and create a TRUE/FALSE matrix

crime_neighborhoods <- st_within(crime_proj_filtered, neighborhoods_proj, sparse = FALSE)



# using apply to count number of TRUE values, the number of crimes that occurred in each neighborhood 

crime_neighborhoods_1 <- apply(X = crime_neighborhoods, MARGIN = 2, FUN = sum)



# using cbind to join counted TRUE values to neighborhoods dataset

crime_neighborhoods_2 <- cbind(neighborhoods_proj, crime_neighborhoods_1)



# creating new variable from crime_neighborhoods_2 dataset that filters for neighborhoods with either less than 100 crimes or greater than 1200 crimes just to double check that the data has been correctly narrowed to the given conditions

crime_neighborhoods_filtered <- crime_neighborhoods_2[crime_neighborhoods_2$crime_neighborhoods_1 < 100 | crime_neighborhoods_2$crime_neighborhoods_1 > 1200, ]
  


# filtering the previously created variable to only get neighborhoods with crimes less than 100 and storing into new variable

crime_neighborhoods_filtered_safe <- crime_neighborhoods_filtered %>%
  filter( crime_neighborhoods_1 < 100)



# doing the same for neighborhoods with crimes greater than 1200

crime_neighborhoods_filtered_unsafe <- crime_neighborhoods_filtered %>%
  filter( crime_neighborhoods_1 > 1200)



# setting plot option for maps (and noting down view option as well)

tmap_mode("view") 
tmap_mode("plot") 



# creating neighborhoods map to be first layer on final map

neighborhoods_map <- tm_shape(neighborhoods_proj) +
  tm_polygons()
  


# creating map of safest neighborhoods (color coding to green) to be second layer on final map

safe_neighborhoods_map <- tm_shape(crime_neighborhoods_filtered_safe) +
  tm_polygons(col = "green") 



# creating map of unsafest neighborhoods (color coding to red) to be third layer on final map

unsafe_neighborhoods_map <- tm_shape(crime_neighborhoods_filtered_unsafe) +
  tm_polygons(col = "red") 



# layering each map in order to create final map

safest_unsafest_Detroit_neighborhoods_map <- neighborhoods_map + safe_neighborhoods_map + unsafe_neighborhoods_map +
  tm_layout(main.title = "Map of Least and Most Safe Detroit Neighborhoods by Crime Incidents in 2021",
          main.title.position = "center",
          main.title.size = 0.75,
          frame = FALSE)



# printing final map!

safest_unsafest_Detroit_neighborhoods_map



### 2 ###



# using st_within to map 2021 crimes over zipcodes and create a TRUE/FALSE matrix

crime_zipcodes <- st_within(crime_proj_filtered, zipcodes_proj, sparse = FALSE)



# using apply to count number of TRUE values, the number of crimes that occurred in each zipcode

crime_zipcodes_1 <- apply(X = crime_zipcodes, MARGIN = 2, FUN = sum)



# using cbind to join counted TRUE values to zipcodes dataset

crime_zipcodes_2 <- cbind(zipcodes_proj, crime_zipcodes_1)



# creating new variable from crime_zipcodes_2 dataset that filters for zipcodes with either less than 1000 crimes or greater than 5000 crimes just to double check that the data has been correctly narrowed to the given conditions

crime_zipcodes_filtered <- crime_zipcodes_2[crime_zipcodes_2$crime_zipcodes_1 < 1000 | crime_zipcodes_2$crime_zipcodes_1 > 5000, ]



# filtering the previously created variable to only get zipcodes with crimes less than 1000 and storing into new variable

crime_zipcodes_filtered_safe <- crime_zipcodes_filtered %>%
  filter(crime_zipcodes_1 < 1000)



# doing the same for neighborhoods with crimes greater than 5000

crime_zipcodes_filtered_unsafe <- crime_zipcodes_filtered %>%
  filter(crime_zipcodes_1 > 5000)



# creating zipcodes map to be first layer on final map

zipcodes_map <- tm_shape(zipcodes_proj) + tm_polygons() + 
  tm_text("zipcode", size = 0.5) 



# creating map of unsafest neighborhoods (color coding to red) to be second layer on final map

unsafe_zipcodes_map <- tm_shape(crime_zipcodes_filtered_unsafe) + tm_polygons(col = "red") + 
  tm_text("zipcode", size = 0.5) 



# creating map of safest neighborhoods (color coding to green) to be third layer on final map

safe_zipcodes_map <- tm_shape(crime_zipcodes_filtered_safe) + tm_polygons(col = "green") + 
  tm_text("zipcode", size = 0.5) 



# layering each map in order to create final map

safest_unsafest_Detroit_zipcodes_map <- zipcodes_map + unsafe_zipcodes_map + safe_zipcodes_map + 
  tm_layout(main.title = "Map of Least and Most Safe Detroit Zipcodes by Crime Incidents in 2021",
            main.title.position = "center",
            main.title.size = 0.75,
            frame = FALSE)



# printing final map!

safest_unsafest_Detroit_zipcodes_map



##### Task 2 #####



### 1 ###



# creating map of grocery stores in each neighborhood in Detroit

neighborhoods_grocery_map <- tm_shape(neighborhoods_proj) +
  tm_polygons() + tm_shape(grocery_proj) + 
  tm_dots(col = 'black', size = 0.05)



# Creating mile and half-mile buffers around each grocery store

grocery_half_mile_buff <- st_buffer(grocery_proj, dist = 2640)
grocery_mile_buff <- st_buffer(grocery_proj, dist = 5280)



# compiling first map with previously created buffers to obtain the 2 radii around each Detroit grocery store 

neighborhoods_grocery_buffer_map <- neighborhoods_grocery_map + tm_shape(grocery_half_mile_buff) + 
  tm_borders(col = "red") + tm_fill(col = "red", alpha = 0.2) +
  tm_shape(grocery_mile_buff) + tm_borders(col = "orange") +
  tm_fill(col = "orange", alpha = 0.2) + tm_layout(frame = FALSE)



# printing final map!

neighborhoods_grocery_buffer_map



### 2 ###



# filtering 2021 crime dataset to only robberies

robberies_proj_filtered <- crime_proj_filtered %>%
  filter(offense_de == "ROBBERY")



# using st_within to get the number of robberies within a 1/2 mile and mile radii of the grocery stores

robberies_within_half_mi <- st_within(robberies_proj_filtered, grocery_half_mile_buff, sparse = FALSE) # (sgbp)
robberies_within_mi <- st_within(robberies_proj_filtered, grocery_mile_buff, sparse = FALSE)



# using apply function to sum the number of robberies around the grocery stores

robberies_within_half_mi <- apply(X = robberies_within_half_mi, MARGIN=2,FUN=sum)
robberies_within_mi <- apply(X = robberies_within_mi, MARGIN=2,FUN=sum)



# using cbind to bind the grocery store data with the robberies data within the given radii

grocery_robberies <- cbind(grocery_stores, robberies_within_half_mi, robberies_within_mi)



# creating a new object, grocery_robberies_cleaned, by selecting the required columns to create a cleaned dataframe to export into excel

grocery_robberies_cleaned <- grocery_robberies %>% 
  select(Store_Name, Address, robberies_within_half_mi, robberies_within_mi)



# using st_drop_geometry to eliminate the geometry column

grocery_robberies_cleaned <- st_drop_geometry(grocery_robberies_cleaned)



# running descriptive statistics for the 2 robbery incidents variables

desc_stats_grocery_robberies_cleaned <- summary(grocery_robberies_cleaned)
desc_stats_grocery_robberies_cleaned



# saving the data 

save(grocery_robberies_cleaned, file = "Detroit Grocery Stores and Robberies.RData")
save(desc_stats_grocery_robberies_cleaned, file = "Detroit Grocery Stores and Robberies Descriptive Stats.RData")



# saving the grocery_robberies_cleaned dataframe as an Excel file

library(writexl)
write_xlsx(grocery_robberies_cleaned, 'Detroit Grocery Stores and Robberies.xlsx')






