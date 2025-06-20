import mad_texts

#Titles of the stories in madTexts
titles = ['camping','hospital','forest']

#List containing all the lists to be passed and then unpacked
package = []

#Sends the stories classes from madTexts
def getStory(title):
    match title:
        case 'camping':
            return mad_texts.camping
        case 'hospital':
            return mad_texts.hospital
        case 'forest':
            return mad_texts.forest
        case 'test':
            return mad_texts.test

#Lists of stories that contains each element

"""
The structure of the following segments is:
#Comment specify what element you need
has[Element] = [stories that need this element]
elements[number] = [stories that need [number] element(s)] #add as many copies as you need of this list
elements = [] #empty list to contain the inputed elements
"""

#General elements

#Stories that need names
hasName = ['camping','forest','test']
names = []

#Stories that need nouns
hasNoun = ['camping','hospital','forest']
nouns = []

#Stories that need nouns (plural form)
hasNounPlur = ['forest']
nounsPlur = []

#Stories that need adjectives
hasAdjective = ['hospital','forest']
adjectives = []

#Stories that need verbs
hasVerb = ['camping','hospital']
verbs = []

#Stories that need verbs (-ing)
hasVerbing = ['camping','forest']
verbings = []

#Stories that need verbs (-ly)
hasVerbly = ['camping']
verblys = []

#Stories that need numbers
hasNumber = ['camping','hospital','forest']
numbers = []

#Stories that need times
hasTime = ['camping','hospital','forest']
times = []

#Stories that need colors
hasColor = ['camping','hospital','forest']
colors = []

#Silly

#Stories that need silly
hasSilly = ['camping','hospital']
sillys = []

#Special elements

#Stories that need animals
hasAnimal = ['camping','forest']
animals = []

#Stories that need feelings
hasFeelings = ['camping']
feelings = []

#Stories that need body parts
hasBody = ['hospital']
bodys = []

#Stories that need vehicles
hasVehicle = ['hospital']
vehicles = []

#Stories that need places
hasPlace = ['forest']
places = []

#Stories that need house rooms
hasRoom = ['forest']
rooms = []

#Stories that need magical creatures (plural)
hasMagicalCreaturePlur = ['forest']
magicalCreaturesPlur = []

#Pack all the lists in the package list
#If you add an element type, add it to the end of the arguments, to unpack it, use it's index
def pack():
    package.append(names)
    package.append(nouns)
    package.append(nounsPlur)
    package.append(adjectives)
    package.append(verbs)
    package.append(verbings)
    package.append(verblys)
    package.append(numbers)
    package.append(times)
    package.append(colors)
    package.append(sillys)
    package.append(animals)
    package.append(feelings)
    package.append(bodys)
    package.append(vehicles)
    package.append(places)
    package.append(rooms)
    package.append(magicalCreaturesPlur)
