# install packages if required
install.packages("sf")
install.packages("dplyr")

# load packages
library(sf)
library(dplyr)

# read data
neighborhoods_data <- st_read("Data/Neighborhoods.shp")         
crime_by_neigh <- read.csv('Data/crime_by_neighborhood1.csv') 
grocery_stores = st_read('Data/Grocery_Stores_in_City_of_Detroit_Public_View.shp')

#q1
# A) Use a function to define what type of object these data files belong to. Write a one line statement for your
# answers.
# B) Use a function to find out the CRS values for the data files. Note down your observations.
# C) How can you check if your data files have a projected or unprojected CRS? Interpret your answers.
class(neighborhoods_data)
class(crime_by_neigh)
class(grocery_stores)

st_crs(grocery_stores)
st_crs(crime_by_neigh)
st_crs(grocery_stores)

st_is_longlat(grocery_stores)
st_is_longlat(neighborhoods_data)

#q2
# Is the 'grocery_stores' shapefile object projected? Write a function to appropriately project it if needed and
# name your projected variable 'grocery_stores_proj'. Use a function to check for projection again.

grocery_stops_proj = st_transform(grocery_stores, crs = 5623)

st_is_longlat(grocery_stops_proj)

#q3
# Create an inner join between 'neighborhoods_data' and 'crime_by_neigh' data. Call your new data - 
# "combined_crime_neigh" 
# Hint: You might want to check for the same column name before making. If not, rename one of the 
# columns to match the other column.

combined_crime_neigh = neighborhoods_data %>% 
  rename("neighborhood" = "nhood_name") %>% 
  inner_join(crime_by_neigh, by = "neighborhood")

#q4
# We want to modify our combined dataset now so that is easily understandable. 
# A) Display only columns OBJECTID, nhood_num, neighborhood, no_of_crime_inci.
# B) Change these column names to NeighborhoodID, Neighborhood_Number, Neighborhood_Name, Crime_Inci_Number respectively.
# NOTE: The geometry column can still show in the final dataset.

combined_crime_neigh = 
  combined_crime_neigh %>%
  select(OBJECTID, nhood_num, neighborhood, no_of_crime_inci) %>% 
  rename("NeighborhoodID" = "OBJECTID",
         "Neighborhood_Number" = "nhood_num",
         "Neighborhood_Name" = "neighborhood",
         "Crime_Inci_Number" = "no_of_crime_inci")

#q5
# Which neighborhoods have the highest and lowest crime incidents? (Store in two new variables - highest, lowest)
# Hint: You can arrange them by the number of crime incidents and then combine with head/tail functions. 
highest = combined_crime_neigh %>% 
  arrange(desc(Crime_Inci_Number)) %>% 
  head(1)

highest

lowest = combined_crime_neigh %>% 
  arrange(Crime_Inci_Number) %>% 
  head(1)

lowest

#q6
# Neighborhoods with crime incidents above 2500 are considered as 'Unsafe' and those below are
# 'Safe'. Create a new column in the combined data called 'Neigh_Type' that will store this information.
# Finally, count the number of Unsafe and Safe neighborhoods using the 'Safety_Info' column. Give the name
# 'Neigh_Count' to the variable storing this count. Store this information in a new variable called 'safety_info'.

combined_crime_neigh = combined_crime_neigh %>% 
  mutate(Neigh_Type = if_else(Crime_Inci_Number > 2500, "Unsafe", "Safe"))

safety_info = combined_crime_neigh %>% 
  group_by(Neigh_Type) %>% 
  summarise(Neigh_Count = n())

safety_info
