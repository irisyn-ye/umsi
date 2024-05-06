# Loading the libraries
library(sf)
library(dplyr)
library(tmap)

setwd("/Users/iye/Documents/umich/qmss301/proj_1/proj1_data")


##########################################
############ MAPPING #####################
##########################################

## One of the beauty of using sf packages over other packages like sp is that, even though the
# data is geospatial, it still maintain its dataframe attributes, and thus can work with it
# using packages used to handle normal dataframe.

# Let's read in a new data to perform this task
neighborhoods_data <- st_read("Neighborhoods.shp")              # A shapefile vector polygon
crime_by_neigh <- read.csv('crime_by_neighborhood1.csv')        # An ordinary dataframe


# View the column names
colnames(neighborhoods_data)
colnames(crime_by_neigh)

#Let's perform an inner join
new_crime_data <- neighborhoods_data %>%
        left_join(crime_by_neigh, by = c("nhood_name" = "neighborhood"))

st_crs(new_crime_data)
# reproject the crime data
new_crime_data_proj <- st_transform(new_crime_data, crs = 5623)


### Now, let's do some simple mapping using the tmap package


# The first thing about mapping with tmap package is the tm_shape function.
# That is where you specify the spatial object you want to map before adding further
# effects using other tm functions, such as tm_fill, tm_borders, etc.
# You can add additional layers to the shape using the '+' sign.
# You can get more info. from the tmap pdf document: https://cran.r-project.org/web/packages/tmap/tmap.pdf

# Geospatial Visualization using tmap
tmap_mode("plot") # For ploting view
tmap_mode("view") # For interactive View

# Just the shape and fill layer
tm_shape(new_crime_data_proj) +
        tm_fill() 

# Add border layer to the shape
tm_shape(new_crime_data_proj) +
        tm_borders()

# Add fill and border layers to the shape
tm_shape(new_crime_data_proj) +
        tm_fill() +
        tm_borders()

# The tm_polygons function combines both the tm_fill and tm_border layers
tm_shape(new_crime_data_proj) +
        tm_polygons('no_of_crime_inci')


# Add fill and border layers to the shape
tm_shape(new_crime_data_proj) +
        tm_polygons() +
        tm_symbols(col = "red", size = 'no_of_crime_inci')


# You can build shapefile on another by first saving the first as an object and then build on it.
# We want to build the bus stop shapefile on the crime shapefile, but we have to confirm that
# both of them have the same crs
# Take note that they both have thesame projected crs


# Save the crime incidents map as crime_map
crime_map <- tm_shape(new_crime_data_proj) +
        tm_polygons('no_of_crime_inci')

# Let's bring in the bus stop shapefile and project it
bus_stops <- st_read("DDOT_Bus_Stops.shp")
but_stop_proj <- st_transform(bus_stops, crs = 5623)

# plot the bus stop shapefile on the crime map
crime_map + tm_shape(but_stop_proj) +
        tm_dots() 


######################################################
############## SOME ANALYSIS #########################
######################################################

## Recommended Resources:
# https://geocompr.robinlovelace.net/index.html
# https://geodacenter.github.io/opioid-environment-toolkit/buffer_analysis.html


neighborhoods <- st_read("Neighborhoods.shp")
bus_stops <- st_read("DDOT_Bus_Stops.shp")
grocery <- st_read("Grocery_Stores_in_City_of_Detroit_Public_View.shp")

# check out their crs
st_crs(neighborhoods)
st_crs(bus_stops)
st_crs(grocery)

# Are the crs projected?
st_is_longlat(neighborhoods)
# ???
# ???

# Let' project them
bus_stops_p <- st_transform(bus_stops, crs = 5623)
neighborhoods_p <- st_transform(neighborhoods, crs = 5623)
grocery_p <- st_transform(grocery, crs = 5623)

st_crs(bus_stops_p)
#
st_is_longlat(bus_stops_p)

# colnames
colnames(grocery_p)
colnames(bus_stops_p)


# Geospatial Visualization using tmap
tmap_mode("plot") # For ploting view
tmap_mode("view") # For interactive View

# Geospatial Visualization
tm_shape(neighborhoods_p['nhood_name']) + tm_polygons(alpha = 0.8) +
        tm_shape(grocery_p) + tm_dots(col = 'blue', size = 0.1)


# Getting the projected CRS's unit of measurement 
st_crs(bus_stops_p)$units

st_crs(grocery_p)

# Create a buffer of 0.5 mile radius around each grocery store
gro_half_buff <- st_buffer(grocery_p, dist = 2640)


# Visualize buffers
tm_shape(neighborhoods_p) + tm_polygons(alpha = 0.4) +
        tm_shape(grocery_p) + tm_dots(col = "blue", size = 0.1) +
        tm_shape(gro_half_buff) + tm_borders(col = "red") + tm_fill(col = "red", alpha = 0.2)


### Creating another buffer

# Create another buffer of 1 mile around the grocery stores and call it 'gro_1m_buff'.
# Add this layer to the existing map plot. Let the borders and fill colors be red. Set the fill alpha value to 0.5.
tmap_mode("plot")
gro_1m_buff <- st_buffer(grocery_p, dist = 5280)

tm_shape(neighborhoods_p) + tm_polygons(alpha = 0.4) +
        tm_shape(grocery_p) + tm_dots(col = "blue", size = 0.1) +
        tm_shape(gro_half_buff) + tm_borders(col = "red") + tm_fill(col = "red", alpha = 0.2) +
        tm_shape(gro_1m_buff) + tm_borders(col = 'red') + tm_fill(col = 'red', alpha = 0.5)



# Titling your plot and adding text
tm_shape(neighborhoods_p) + tm_polygons(alpha = 0.4) + tm_text('nhood_name', size = 0.4) +
        tm_shape(grocery_p) + tm_dots(col = "blue", size = 0.1) +
        tm_shape(gro_half_buff) + tm_borders(col = "red") + tm_fill(col = "red", alpha = 0.2) +
        tm_shape(gro_1m_buff) + tm_borders(col = 'red') + tm_fill(col = 'red', alpha = 0.5) +
        tm_layout(main.title = "Map of Detroit Neighborhood and Grocery Stores",
                  main.title.position = "center",
                  main.title.size = 1,
                  frame = FALSE)



## Adding the bus stop layer
tm_shape(neighborhoods_p) + tm_polygons(alpha = 0.4) +
        tm_shape(grocery_p) + tm_dots(col = "blue", size = 0.1) +
        tm_shape(gro_half_buff) + tm_borders(col = "red") + tm_fill(col = "red", alpha = 0.2) +
        tm_shape(gro_1m_buff) + tm_borders(col = 'red') + tm_fill(col = 'red', alpha = 0.5) +
        tm_shape(bus_stops_p) + tm_dots(col = 'green')

# columns of target data
colnames(bus_stops_p)
colnames(grocery_p)
colnames(gro_half_buff)

# check data sample
bus_stops_p %>% head(5)
grocery_p %>% head(5)
gro_half_buff %>% head(5)

#Getting the number of bus stops within radii of the grocery stores
bus_within_half <- st_within(bus_stops_p, gro_half_buff, sparse = FALSE) # Sparse geometry binary predicate (sgbp)
bus_within_1m <- st_within(bus_stops_p, gro_1m_buff, sparse = FALSE)

###########################################################
##Let's do a little demonstration with 'apply' to see how it works
x <- c(1,2,3,4,5)
y <- c(1,0,1,1,1)
z <- c(0,0,1,0,0)
zz <- data.frame(x,y,z)
zz
apply(zz, MARGIN = 1, FUN = sum)
#######################################################

#Number of bus stops: Summing the number of bus stops around the grocery stores
bstops_within_half <- apply(X = bus_within_half, MARGIN=2,FUN=sum)
bstops_within_1m <- apply(X = bus_within_1m, MARGIN=2,FUN=sum)

# print bus stop within range data
bstops_within_half
bstops_within_1m

# data type of bus stops sum
class(bstops_within_half)

# count row numbers
nrow(grocery)
length(bstops_within_half)

# Binding the grocery store data with the bus stops data within half mile and 1miles
grocery_bstops <- cbind(grocery, bstops_within_half, bstops_within_1m)

colnames(grocery_bstops)

# Creating a new objects by selecting few columns
grocery_bstops1 <- grocery_bstops %>% 
        select(Store_Name, Address, bstops_within_half, bstops_within_1m)

class(grocery_bstops1)

# Dropping the geometry column
grocery_bstops1 <- st_drop_geometry(grocery_bstops1)

class(grocery_bstops1)

# Save the data
save(grocery_bstops1, file = "detroit grocery stores and bus stops.RData")

library(writexl)
write_xlsx(grocery_bstops1, 'detroit grocery stores and bus stops.xlsx')




# The same technique can be used to find the number of bus stops within each neighborhood.

# Finding the number of bus stops in each neighborhood
neigh_bus <- st_within(bus_stops_p, neighborhoods_p, sparse = FALSE)

# Summing up the numbers
neigh_bus1 <- apply(X=neigh_bus, MARGIN=2,FUN=sum)

# Binding the bus data with the neighborhood
neigh_bus2 <- cbind(neighborhoods_p, neigh_bus1)





