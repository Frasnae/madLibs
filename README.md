# madLibs
console game Mad Libs

# HOW TO ADD A NEW STORY

Go to madTexts.py and create a new class, the name will be used to identify it across all documents, add this name to the end of the
"titles" list in madLists.py to add it to the random choice list

In this class you will need to add the following:

## ATTRIBUTES
  Any element that will be asked to the user to make a story must be added as an attribute and assigned the times you will need
  it as it's value; if the needed element already has a list for it in madLists.py make sure to use the same name of this list
  as the name of the attribute, for example:
      if you need 2 verbs, since there's an existing list for verbs you would declare it like this -> verbs = 2

  This will tell the program how many times to ask for each element in the fill() function in madFunctions.py
  
### IF YOU WISH TO ADD YOUR OWN ELEMENTS
  Go to madLists.py and add a block for your element at the end of the file before the pack() function according to the following
  structure:
      - Comment describing shortly the new element
      - 'has' list to include the titles of the stories that need said element, name it 'has[MyElement]' and assign the titles that
      need this element as values of a list -> hasMyElement = ['title1','title2']
      - container list to include the user inputs of this element, name it like the element in plural and assign an empty list as
      the value -> myElements = []

  Once your element is added, add a line to the pack() function to append your list to the main package containing all the lists:
  At the very end, do 'package.append(myElements)' to make sure it's used in your story

  After finishing editing the madLists.py file, make sure to save and then go to madFunctions.py to add a block to process your element
  when needed in a story using the following structure:
  
        for title in madLists.hasMyElement:
        if choice == title:
            i = 0
            while i < story.myElements:
                madLists.myElements.append(input("\nGive me a/an [element]\n"))
                i += 1
            break
            
  Make sure to declare in your story how many of your elements are needed to make sure they get requested
  
## FUNCTION "story(package)"
  To add the text of your story, first create a function within your class called "story" with an argument to recieve the list
  "package" (can be any name), then write your story using a print() with format to use curvy brackets for placeholders for your story
  elements; each time an element type is needed, use the brackets to indicate which type of element is needed followed by a number
  to identify which one it is, for example:
      print(f"Today I'm going out with {name1} and {name2}")

  After you're done formating your story, go back to the begining of the function to set the unpacking section

### UNPACKING
  Before your print() function, list all similar elements to then unpack the correspoding list inside the "package" list, to identify
  which index you will need, check at the list on the bottom of this file, and use it as follows:
  
      name1, name2 = package[0]

  If your story only needs one instance of the element, unpack the list twice using another variable to recieve the list inside the package
  to avoid the output to be printed as a list, for example:

      name1 = package[0]
      print(f"{name1}")

      Output -> ['yourName']
    
      name = package[0]
      name1 = name[0]
      print(f"{name1}")

      Output -> yourName
            
==ELEMENTS INDEX NUMBERS==
GENERAL
0   names
1   nouns
2   nounsPlur
3   adjectives
4   verbs
5   verbings (verbs ending in -ing)
6   verblys (verbs ending in -ly)
7   numbers
8   times (measure of time)
9   colors

SILLY
10  sillys (silly words)

SPECIAL
11  animals
12  feelings
13  bodys (body parts)
14  vehicles
15  places
16  rooms (rooms in a house)
17  magicalCreaturesPlur (magical creatures in plural)
