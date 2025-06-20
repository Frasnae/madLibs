import madLists, random

#Empty all elements lists
def empty():
    #Package list
    madLists.package.clear()

    #Generals
    madLists.names.clear()
    madLists.nouns.clear()
    madLists.nounsPlur.clear()
    madLists.adjectives.clear()
    madLists.verbs.clear()
    madLists.verbings.clear()
    madLists.verblys.clear()
    madLists.numbers.clear()
    madLists.times.clear()
    madLists.colors.clear()

    #Silly
    madLists.sillys.clear()

    #Specials
    madLists.animals.clear()
    madLists.feelings.clear()
    madLists.bodys.clear()
    madLists.vehicles.clear()
    madLists.places.clear()
    madLists.rooms.clear()
    madLists.magicalCreaturesPlur.clear()

#Start creating a story
def fill():
    #choice = random.choice(madLists.titles)
    choice = 'forest' #Uncomment and comment previous line to run a test
    story = madLists.getStory(choice)

    for title in madLists.hasName:
        if choice == title:
            i = 0
            while i < story.names:
                madLists.names.append(input("\nGive me a name\n"))
                i += 1
            break

    for title in madLists.hasNoun:
        if choice == title:
            i = 0
            while i < story.nouns:
                madLists.nouns.append(input("\nGive me a noun\n"))
                i += 1
            break
        
    for title in madLists.hasNounPlur:
        if choice == title:
            i = 0
            while i < story.nounsPlur:
                madLists.nounsPlur.append(input("\nGive me a noun (plural)\n"))
                i += 1
            break

    for title in madLists.hasAdjective:
        if choice == title:
            i = 0
            while i < story.adjectives:
                madLists.adjectives.append(input("\nGive me an adjective\n"))
                i += 1
            break

    for title in madLists.hasVerb:
        if choice == title:
            i = 0
            while i < story.verbs:
                madLists.verbs.append(input("\nGive me a verb\n"))
                i += 1
            break

    for title in madLists.hasVerbing:
        if choice == title:
            i = 0
            while i < story.verbings:
                madLists.verbings.append(input("\nGive me a verb (-ing)\n"))
                i += 1
            break

    for title in madLists.hasVerbly:
        if choice == title:
            i = 0
            while i < story.verblys:
                madLists.verblys.append(input("\nGive me a verb (-ly)\n"))
                i += 1
            break

    for title in madLists.hasNumber:
        if choice == title:
            i = 0
            while i < story.numbers:
                madLists.numbers.append(input("\nGive me a number\n"))
                i += 1
            break

    for title in madLists.hasTime:
        if choice == title:
            i = 0
            while i < story.times:
                madLists.times.append(input("\nGive me a measure of time\n"))
                i += 1
            break

    for title in madLists.hasColor:
        if choice == title:
            i = 0
            while i < story.colors:
                madLists.colors.append(input("\nGive me a color\n"))
                i += 1
            break

    for title in madLists.hasSilly:
        if choice == title:
            i = 0
            while i < story.sillys:
                madLists.sillys.append(input("\nGive me a silly word\n"))
                i += 1
            break

    for title in madLists.hasAnimal:
        if choice == title:
            i = 0
            while i < story.animals:
                madLists.animals.append(input("\nGive me an animal\n"))
                i += 1
            break

    for title in madLists.hasFeelings:
        if choice == title:
            i = 0
            while i < story.feelings:
                madLists.feelings.append(input("\nGive me a feeling\n"))
                i += 1
            break

    for title in madLists.hasBody:
        if choice == title:
            i = 0
            while i < story.bodys:
                madLists.bodys.append(input("\nGive me a body part\n"))
                i += 1
            break

    for title in madLists.hasVehicle:
        if choice == title:
            i = 0
            while i < story.vehicles:
                madLists.vehicles.append(input("\nGive me a vehicle name\n"))
                i += 1
            break

    for title in madLists.hasPlace:
        if choice == title:
            i = 0
            while i < story.places:
                madLists.places.append(input("\nGive me a place\n"))
                i += 1
            break

    for title in madLists.hasRoom:
        if choice == title:
            i = 0
            while i < story.rooms:
                madLists.rooms.append(input("\nGive me the name of a room in a house\n"))
                i += 1
            break

    for title in madLists.hasMagicalCreaturePlur:
        if choice == title:
            i = 0
            while i < story.magicCreaturesPlur:
                madLists.magicalCreaturesPlur.append(input("\nGive me the name of a magical creature (plural)\n"))
                i += 1
            break

    madLists.pack()
    story.story(madLists.package)