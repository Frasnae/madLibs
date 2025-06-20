import mad_lists, random

#Empty all elements lists
def empty():
    #Package list
    mad_lists.package.clear()

    #Generals
    mad_lists.names.clear()
    mad_lists.nouns.clear()
    mad_lists.nounsPlur.clear()
    mad_lists.adjectives.clear()
    mad_lists.verbs.clear()
    mad_lists.verbings.clear()
    mad_lists.verblys.clear()
    mad_lists.numbers.clear()
    mad_lists.times.clear()
    mad_lists.colors.clear()

    #Silly
    mad_lists.sillys.clear()

    #Specials
    mad_lists.animals.clear()
    mad_lists.feelings.clear()
    mad_lists.bodys.clear()
    mad_lists.vehicles.clear()
    mad_lists.places.clear()
    mad_lists.rooms.clear()
    mad_lists.magicalCreaturesPlur.clear()

#Start creating a story
def fill():
    choice = random.choice(mad_lists.titles)
    #choice = 'forest' #Uncomment and comment previous line to run a test
    story = mad_lists.getStory(choice)

    for title in mad_lists.hasName:
        if choice == title:
            i = 0
            while i < story.names:
                mad_lists.names.append(input("\nGive me a name\n"))
                i += 1
            break

    for title in mad_lists.hasNoun:
        if choice == title:
            i = 0
            while i < story.nouns:
                mad_lists.nouns.append(input("\nGive me a noun\n"))
                i += 1
            break
        
    for title in mad_lists.hasNounPlur:
        if choice == title:
            i = 0
            while i < story.nounsPlur:
                mad_lists.nounsPlur.append(input("\nGive me a noun (plural)\n"))
                i += 1
            break

    for title in mad_lists.hasAdjective:
        if choice == title:
            i = 0
            while i < story.adjectives:
                mad_lists.adjectives.append(input("\nGive me an adjective\n"))
                i += 1
            break

    for title in mad_lists.hasVerb:
        if choice == title:
            i = 0
            while i < story.verbs:
                mad_lists.verbs.append(input("\nGive me a verb\n"))
                i += 1
            break

    for title in mad_lists.hasVerbing:
        if choice == title:
            i = 0
            while i < story.verbings:
                mad_lists.verbings.append(input("\nGive me a verb (-ing)\n"))
                i += 1
            break

    for title in mad_lists.hasVerbly:
        if choice == title:
            i = 0
            while i < story.verblys:
                mad_lists.verblys.append(input("\nGive me a verb (-ly)\n"))
                i += 1
            break

    for title in mad_lists.hasNumber:
        if choice == title:
            i = 0
            while i < story.numbers:
                mad_lists.numbers.append(input("\nGive me a number\n"))
                i += 1
            break

    for title in mad_lists.hasTime:
        if choice == title:
            i = 0
            while i < story.times:
                mad_lists.times.append(input("\nGive me a measure of time\n"))
                i += 1
            break

    for title in mad_lists.hasColor:
        if choice == title:
            i = 0
            while i < story.colors:
                mad_lists.colors.append(input("\nGive me a color\n"))
                i += 1
            break

    for title in mad_lists.hasSilly:
        if choice == title:
            i = 0
            while i < story.sillys:
                mad_lists.sillys.append(input("\nGive me a silly word\n"))
                i += 1
            break

    for title in mad_lists.hasAnimal:
        if choice == title:
            i = 0
            while i < story.animals:
                mad_lists.animals.append(input("\nGive me an animal\n"))
                i += 1
            break

    for title in mad_lists.hasFeelings:
        if choice == title:
            i = 0
            while i < story.feelings:
                mad_lists.feelings.append(input("\nGive me a feeling\n"))
                i += 1
            break

    for title in mad_lists.hasBody:
        if choice == title:
            i = 0
            while i < story.bodys:
                mad_lists.bodys.append(input("\nGive me a body part\n"))
                i += 1
            break

    for title in mad_lists.hasVehicle:
        if choice == title:
            i = 0
            while i < story.vehicles:
                mad_lists.vehicles.append(input("\nGive me a vehicle name\n"))
                i += 1
            break

    for title in mad_lists.hasPlace:
        if choice == title:
            i = 0
            while i < story.places:
                mad_lists.places.append(input("\nGive me a place\n"))
                i += 1
            break

    for title in mad_lists.hasRoom:
        if choice == title:
            i = 0
            while i < story.rooms:
                mad_lists.rooms.append(input("\nGive me the name of a room in a house\n"))
                i += 1
            break

    for title in mad_lists.hasMagicalCreaturePlur:
        if choice == title:
            i = 0
            while i < story.magicCreaturesPlur:
                mad_lists.magicalCreaturesPlur.append(input("\nGive me the name of a magical creature (plural)\n"))
                i += 1
            break

    mad_lists.pack()
    story.story(mad_lists.package)