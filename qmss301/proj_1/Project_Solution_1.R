# The libraries
library(sf)
library(dplyr)
library(tmap)

## Recommended Resources:
# https://geocompr.robinlovelace.net/index.html
# https://geodacenter.github.io/opioid-environment-toolkit/buffer_analysis.html

setwd("/Users/iye/Documents/umich/qmss301/proj_1/proj1_data")

neighborhoods <- st_read("Neighborhoods.shp")
grocery <- st_read("Grocery_Stores_in_City_of_Detroit_Public_View.shp")
zipcode <- st_read("zip_codes.shp")
crime <- st_read("RMS_Crime_Incidents.shp")

neighborhoods_p <- st_transform(neighborhoods, crs = 5623)
grocery_p <- st_transform(grocery, crs = 5623)
zipcode_p <- st_transform(zipcode, crs = 5623)
crime_p <- st_transform(crime, crs = 5623)

crime_2021 <- filter(crime_p, year == 2021)

###########################

## Task 1: Crime Incidents in Detroit's Neighborhood and zip code areas.

# Question 1
neigh_crime <- st_within(crime_2021, neighborhoods_p, sparse = FALSE)

neigh_crime1 <- apply(X=neigh_crime, MARGIN=2,FUN=sum)

neigh_crime2 <- cbind(neighborhoods_p, neigh_crime1)

# check colnames of each dataset 
colnames(neighborhoods_p)
colnames(neigh_crime1)
colnames(neigh_crime2)

neigh_with_lt100_crimes <- filter(neigh_crime2, neigh_crime1 < 100)
neigh_with_mt1500_crimes <- filter(neigh_crime2, neigh_crime1 > 1200)

tm_shape(neighborhoods_p) + tm_polygons() + 
        tm_shape(neigh_with_lt100_crimes) + tm_polygons(col = 'green') +
        tm_shape(neigh_with_mt1500_crimes) + tm_polygons(col = 'red') +
        tm_layout(main.title = "Map of Detroit neighborhood and crime rate",
                  main.title.position = "center",
                  main.title.size = 1,
                  frame = FALSE)


# Question 2:
zip_crime <- st_within(crime_2021, zipcode_p, sparse = FALSE)

zip_crime1 <- apply(X=zip_crime, MARGIN=2,FUN=sum)

zip_crime2 <- cbind(zipcode_p, zip_crime1)

zip_with_lt100_crimes <- filter(zip_crime2, zip_crime1 < 1000)
zip_with_mt1500_crimes <- filter(zip_crime2, zip_crime1 > 5000)

tm_shape(zipcode_p) + tm_polygons()  +
        tm_shape(zip_with_lt100_crimes) + tm_polygons(col = 'green') +
        tm_shape(zip_with_mt1500_crimes) + tm_polygons(col = 'red') +
        tm_shape(zipcode_p) + tm_borders() + tm_text('zipcode', size = 0.5) +
        tm_layout(main.title = "Map of Detroit zipcodes and crime rate",
                  main.title.position = "center",
                  main.title.size = 1,
                  frame = FALSE)

#######################



################################

# Task 2: Robbery Incidents around grocery stores. 

# Question 1:

rob_crime_2021 <- filter(crime_p, year == 2021 & offense_de == 'ROBBERY')

gro_half_buff <- st_buffer(grocery_p, dist = 2640)
gro_1m_buff <- st_buffer(grocery_p, dist = 5280)


tm_shape(neighborhoods_p) + tm_polygons(alpha = 0.4) +
        tm_shape(grocery_p) + tm_dots(col = "blue", size = 0.1) +
        tm_shape(gro_half_buff) + tm_borders(col = "red") + tm_fill(col = "blue", alpha = 0.7) +
        tm_shape(gro_1m_buff) + tm_borders(col = 'red') + tm_fill(col = 'blue', alpha = 0.5) +
        tm_layout(main.title = "Map of Detroit grocery stores",
                  main.title.position = "center",
                  main.title.size = 1,
                  frame = FALSE)

# Question 2:

rob_within_half <- st_within(rob_crime_2021, gro_half_buff, sparse = FALSE)
rob_within_1m <- st_within(rob_crime_2021, gro_1m_buff, sparse = FALSE)


rob_within_half <- apply(X = rob_within_half, MARGIN=2,FUN=sum)
rob_within_1m <- apply(X = rob_within_1m, MARGIN=2,FUN=sum)


rob_gro <- cbind(grocery, rob_within_half, rob_within_1m)

rob_gro1 <- rob_gro %>% 
        select(Store_Name, Address, rob_within_half, rob_within_1m)

rob_gro1 <- st_drop_geometry(rob_gro1)

library(writexl)
write_xlsx(rob_gro1, 'robery around grocery stores.xlsx')
################################



