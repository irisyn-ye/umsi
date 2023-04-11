import requests
import json
import webbrowser
import sys
import random

# step 1 get data
BASE_URL = "https://exercisedb.p.rapidapi.com/exercises"

headers = {
	"X-RapidAPI-Key": "5380f3b0fcmshec010dad98ad6e5p199bcbjsnaa3538ec72c2",
	"X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
}

WorkoutData = requests.request("GET", BASE_URL, headers=headers).json()

# step 2 build class
class WorkoutDB:
    ''' Each workout in the database has bodyPart, name,
    sets, reps, movement gif url, target muscle and id.
    
    Instance Attributes
    -------------------
    bodyPart: string
        body part the workout focuses on
    name: string
        name of workout
    workSet: int
        workout sets
    workRep: int
        workout reps
    equipment: string
        equipment used by this workout
    url: string
        the url of the workout
    id: int
        id of the workout
    '''

    def __init__(self, bodyPart='', name='', workSet=0, workRep=0, equipment='', gifUrl='', targetMuscle='', json=None):
        self.bodyPart = json['bodyPart']
        self.name = json['name']
        self.workSet = random.randint(3, 6)
        self.workRep = random.randint(8, 12)
        self.equipment = json['equipment']
        self.gifUrl = json['gifUrl']
        self.targetMuscle = json['target']
        self.id = json['id']

Workouts = [WorkoutDB(json=d) for d in WorkoutData]

# step 3 cache
CACHE_FILENAME = "cache.json"

def open_cache():
    ''' opens the cache file if it exists and loads the JSON into
    a list, which it then returns.
    if the cache file doesn't exist, creates a new cache list
    
    Parameters
    ----------
    None
    
    Returns
    ----------
    The opened cache
    '''
    try:
        cache_file = open(CACHE_FILENAME, 'r')
        cache_contents = cache_file.read()
        cache_list = json.loads(cache_contents)
        cache_file.close()
    except:
        cache_list = []
    return cache_list

def save_cache(cache_list):
    ''' saves the current state of the cache to dict
    
    Parameters
    ----------
    cache_list: list
        The dictionary to save
    
    Returns
    ----------
    None
    '''
    dumped_json_cache = json.dumps(cache_list)
    fw = open(CACHE_FILENAME,"w")
    fw.write(dumped_json_cache)
    fw.close()  

WORKOUTS_CACHE = open_cache()

if len(WORKOUTS_CACHE) == 0: # if cache does not exist
    WORKOUTS_CACHE = [w.__dict__ for w in Workouts]
    save_cache(WORKOUTS_CACHE)

WORKOUTS_CACHE[0] # test 

# separate list of workouts
# shoulders, chest, legs, waist, back
shouldersM = []
chestM = []
legsM = []
waistM = []
backM = []
armsM = []
cardioM = []

for i in range(len(WORKOUTS_CACHE)):
    if 'shoulders' in WORKOUTS_CACHE[i]['bodyPart'].lower():
        shouldersM.append(WORKOUTS_CACHE[i])
    elif 'chest' in WORKOUTS_CACHE[i]['bodyPart'].lower():
        chestM.append(WORKOUTS_CACHE[i])
    elif 'legs' in WORKOUTS_CACHE[i]['bodyPart'].lower():
        legsM.append(WORKOUTS_CACHE[i])
    elif 'waist' in WORKOUTS_CACHE[i]['bodyPart'].lower():
        waistM.append(WORKOUTS_CACHE[i])
    elif 'back' in WORKOUTS_CACHE[i]['bodyPart'].lower():
        backM.append(WORKOUTS_CACHE[i])
    elif 'arms' in WORKOUTS_CACHE[i]['bodyPart'].lower():
        armsM.append(WORKOUTS_CACHE[i])
    else:
        cardioM.append(WORKOUTS_CACHE[i])


# tree
# tree structure
tree = ('Do you want to check out [1] fitness program, or [2] nearby fitness centers? (Enter a number): ', 
    ('Which body part do you want to work on? (Enter a number between 1-6 [1] shoulders, [2] chest, [3] legs, [4] waist, [5] back, [6] arms)', 
        (shouldersM), 
        (chestM),
        (legsM),
        (waistM),
        (backM),
        (armsM),
        ('Enter a number for the anatomy analysis and movement gif, or exit')), 
    ('Please enter your city or zipcode: ', 
        (), 
        ()),
    ('Enter [1] to design a new program, [2] search a new location', 
        (), 
        ()))

# handle user input errors
def errorHandler():
    ''' Handles the error inputs that not align with instructions
    redirect it to the first prompt
    
    Parameters
    ----------
    None
    
    Returns
    ----------
    None
    '''

    errorPrompt = input(f"Please enter a valid response (Enter 1 or 2): ")
    search(initPrompt = errorPrompt)

# show gif function
def anatomyGif(muscleGroups, url):
    ''' print out the muscle groups this workout uses,
    and open the gif in web browser
    
    Parameters
    ----------
    muscleGroups: string
        the muscle group name
    url: string
        the url of the workout gif
    
    Returns
    ----------
    None
    '''

    print(f"\nThe target muscle groups are {muscleGroups} \n") # target muscle groups
    url = url # get the movement gif url
    print(f"Launching {url} in web browser...")
    webbrowser.open(url)

# gym locations
def gymFinder(location):
    ''' use Google Place API to search for the gym nearby,
    print the neares five gyms nearby the input,
    input can be city/place name, or zipcode,
    each result is printed in a line, with name, rating and address
    
    Parameters
    ----------
    location: string
        the string of a city/place, or zipcode
    
    Returns
    ----------
    None
    '''

    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'query': 'gyms near ' + str(location),
        'key': 'AIzaSyCcADhdYBBpPljyQc36tBOlcof0t7UwIRs'
    }

    # Make the API request
    response = requests.get(url, params=params)

    # Get the response data as JSON
    data = response.json()

    # Loop through the results and print the name and address of each gym
    for result in data['results'][:5]:
        name = result['name']
        address = result['formatted_address']
        rating = result['rating']
        print(f'{name} (rating {rating}): {address}')

# [1] design a fitness program
def programDesign():
    ''' [1] design a fitness program
    it starts from asking which body part the user wants to 
    have program being designed for;
    at anytime if user enters 0, it will restart from
    the initial questions;
    user can enter a number between 1-6, where 1 means
    shoulder, 2 means chest, 3 means legs, 4 means waist, 
    5 means back, 6 means arms accodingly;
    a program list with five workouts' name, sets and reps will be displayed,
    user will then be asked which of the movement they want 
    to check details of gif and target muscle group;
    
    after the first-time search, user can choose to continue with 
    another body part to design program for, or start over, or exit the program;
    
    Parameters
    ----------
    None
    
    Returns
    ----------
    None
    '''

    fitProgram = int(input(f"{tree[1][0]} {startOver}: "))

    if fitProgram == 0: # restart
        search(input(tree[0]))
    
    else: # select body part
        bodyPartM = tree[1][fitProgram]
        programChoices = [random.randint(0, (len(bodyPartM)-1)) for n in range(5)]
        counter = 1
        for i in programChoices:
            print(f"{counter} {bodyPartM[i]['name']}, {bodyPartM[i]['workSet']} sets, {bodyPartM[i]['workRep']} reps")
            counter += 1
        finishPrompt = input(f"{tree[1][-1]} {startOver}: ")
        
        if finishPrompt.lower() == 'exit':
            print(f"Bye!")
            sys.exit() 
        
        elif finishPrompt.isnumeric():
            finishPrompt = int(finishPrompt) # convert info to integer
            if finishPrompt in range(1, 6):
                muscleGroups = bodyPartM[programChoices[finishPrompt-1]]['targetMuscle']
                url = bodyPartM[programChoices[finishPrompt-1]]['gifUrl']
                anatomyGif(muscleGroups, url)
            
            contOrNot()
        
        elif finishPrompt == 0:
            search(input(tree[0]))

        else: # body part error input handler
            finishPrompt = int(input(f"Please enter a valid response (Enter number between 1-5): "))
            muscleGroups = bodyPartM[programChoices[finishPrompt-1]]['targetMuscle']
            url = bodyPartM[programChoices[finishPrompt-1]]['gifUrl']
            anatomyGif(muscleGroups, url)
            
            contOrNot()

# prompts after the first program design/gym search
def contOrNot():
    ''' this appears after finishing the first program design/gym search
    if user enters 1, meaning program design, it will fetch programDesign() to design the program,
    if user enters 2, meaning search for gym, it will fetch gymSearch() to search for gym,
    if user enters exit, meaning exit the program, it will exit the whole program,
    others, will be considered as error inputs handled by errorHandler()
    
    Parameters
    ----------
    None
    
    Returns
    ----------
    None
    '''

    contOrNot = input(f"{tree[3][0]} {startOver} or exit: ")
    if int(contOrNot) == 1: # [1] design fitness program
        programDesign()
    elif int(contOrNot) == 2: # [2] fitness centers nearby
        gymSearch()
    elif int(contOrNot) == 0: # restart
        search(input(tree[0]))
    elif contOrNot.lower() == 'exit': #exit
        print(f"Bye!")
        sys.exit() 
    else:
        errorHandler()

# [2] nearby fitness centers
def gymSearch():
    ''' [2] nearby fitness centers
    will use gymFinder() function to take in the location input
    and search for the gym nearby
    
    Parameters
    ----------
    None
    
    Returns
    ----------
    None
    '''
    location = input(tree[2][0])
    gymFinder(location)
    contOrNot()

# step 4 main function structure

startOver = f"or enter 0 to start over"

def search(initPrompt):
    ''' main search function
    try if the initial prompt input can be converted into integer,
    if it can, follow the instructions,
    if input is 1, do program design for user,
    if input is 2, do gym search for user, 
    others will be handled by errorHandler()
    
    Parameters
    ----------
    initPrompt: string
        The initial prompt to start with
    
    Returns
    ----------
    None
    '''

    try:
        initPrompt = int(initPrompt)

        if initPrompt == 1: # [1] design fitness program
            programDesign()

        elif initPrompt == 2: # [2] fitness centers nearby
            gymSearch()

        else:
            errorHandler()
    
    except Exception: # exit
        print(f"Bye!")
        sys.exit()

    except:
        errorHandler()


search(input(tree[0]))