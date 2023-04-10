# SI 507 Final Project - Fitness Assistant

## Introduction
People generally find strength training intimidating. The foremost pain point reported by users is - They lack fitness knowledge and have no idea how to start.

In this final project, I developed a program to assist users figuring out the strength training movements and locations. Users can input body parts they want to train for and the program will return the according training programs. After the program is returned, users can select a movement to check out the anatomy analysis and gif of the movement. Users can also check out fitness centers nearby their location.

## Data Sources
(1) Fitness program design
Exercise database and documentation: https://rapidapi.com/justin-WFnsXH_t6/api/exercisedb/

(2) Fitness centers nearby
Google Place API: https://developers.google.com/maps/documentation/places/web-service/place-data-fields

## Run the Program
### Step 1: Apply an API Key for Exercise DB
Both of the data sets already have API keys available in the program. If you want to replace it with your own key, please follow the below steps.

Exercise DB
(1) Go to "https://rapidapi.com/justin-WFnsXH_t6/api/exercisedb/" 
(2) Click "Pricing" tab to subscribe and get an API key
(3) Add the API key to line 11:
```
X-RapidAPI-Key: '<your key>'
```  

Google API
(1) Go to "https://developers.google.com/maps/documentation/places/web-service/place-data-fields" 
(2) Create a google account and click "Credentials" tab to get an API key
(3) Add the API key to line 208:
```
key = '<your key>'
```  

### Step 2: Install packages
There are five packages needed in the program, including two default packages - json and random. 
* requests
* json
* webbrowser
* sys
* random
```
$ pip install <package name>
```  

### Step 3: fitnessAssistant.py
```  
$ python fitnessAssistant.py
```  
The program uses command line prompt for interaction.