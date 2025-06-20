class camping:
    names = 1
    nouns = 2
    verbs = 2
    verbings = 1
    verblys = 1
    numbers = 2
    times = 1
    colors = 2
    animals = 2
    feelings = 2
    sillys = 1

    def story(package):
        #Unpacking
        name = package[0]
        name1 = name[0]
        noun1, noun2 = package[1]
        verb1, verb2 = package[4]
        verbing = package[5]
        verbing1 = verbing[0]
        verbly = package[6]
        verbly1 = verbly[0]
        number1, number2 = package[7]
        time = package[8]
        time1 = time[0]
        color1, color2 = package[9]
        animal1, animal2 = package[11]
        feeling1, feeling2 = package[12]
        silly = package[10]
        silly1 = silly[0]

        #Story
        print(f"""\n 🏕️ A Camping We Will Go! 🎒
          
This weekend I am going camping with {name1}. I packed my lantern, sleeping bag, and
{noun1}. I am so {feeling1} to {verb1} in a tent. I am {feeling2} we
might see a {animal1}, they are kind of dangerous. We are going to hike, fish, and {verb2}.
I have heard that the {color1} lake is great for {verbing1}. Then we will
{verbly1} hike through the forest for {number1} {time1}. If I see a
{color2} {animal2} while hiking, I am going to bring it home as a pet! At night we will tell
{number2} {silly1} stories and roast {noun2} around the campfire!! 
          """)

class hospital:
    nouns = 5
    adjectives = 2
    verbs = 3
    numbers = 2
    times = 1
    colors = 1
    bodys = 2
    vehicles = 1
    sillys = 1

    def story(package):
        #Unpacking
        noun1,noun2,noun3,noun4,noun5 = package[1]
        adjective1,adjective2 = package[3]
        verb1,verb2,verb3 = package[4]
        number1,number2 = package[7]
        time = package[8]
        time1 = time[0]
        color = package[9]
        color1 = color[0]
        body1,body2 = package[13]
        vehicle = package[14]
        vehicle1 = vehicle[0]
        silly = package[10]
        silly1 = silly[0]

        #Story
        print(f"""\n 🩹 My Stay At The Hospital 💊

It was about {number1} {time1} ago when I came to the hospital in a {vehicle1}.
The hospital is a/an {adjective1} place, there are a lot of {color1} {noun1} here.
There are nurses here who have {body1} {verb1}. If someone wants to come into my room
I told them that they have to {verb2} first. I have decorated my room with {number2}
{noun2}. Today a doctor came into my room and they were wearing a {noun3} on their
{body2}. I heard that all doctors {verb3} {noun4} every day for breakfast. The
most {adjective2} thing about being in the hospital is the {silly1} {noun5}!
            """)
    
class forest:
    names = 1
    nouns = 4
    nounsPlur = 1
    adjectives = 5
    verbings = 1
    numbers = 1
    times = 1
    colors = 1
    places = 1
    rooms = 1
    animals = 1
    magicCreaturesPlur = 2

    def story(package):
        #Unpacking
        name = package[0]
        name1 = name[0]
        noun1,noun2,noun3,noun4 = package[1]
        nounPlur = package[2]
        nounPlur1 = nounPlur[0]
        adjective1,adjective2,adjective3,adjective4,adjective5 = package[3]
        verbing = package[5]
        verbing1 = verbing[0]
        number = package[7]
        number1 = number[0]
        time = package[8]
        time1 = time[0]
        color = package[9]
        color1 = color[0]
        place = package[15]
        place1 = place[0]
        room = package[16]
        room1 = room[0]
        animal = package[11]
        animal1 = animal[0]
        magicCreaturePlural1,magicCreaturePlural2 = package[17]

        #Story
        print(f"""\n 🌲 Enchanted Forest ✨

Dear {name1},
          
I am writing to you from a {adjective1} castle in an enchanted forest. I found myself here one day after
going for a ride on a {color1} {animal1} in {place1}. There are
{adjective2} {magicCreaturePlural1} and {adjective3} {magicCreaturePlural2} here! In the
{room1} there is a pool full of {noun1}. I fall asleep each night on a {noun2} of
{noun3} and dream of {adjective4} {nounPlur1}. It feels as though I have lived here for
{number1} {time1}. I hope one day you can visit, although the only way to get here now is
{verbing1} on a {adjective5} {noun4}!! 
          """)
        
class test:
    names = 2

    def story(package):
        #Unpacking
        name1, name2 = package[0]

        #Story
        print(f"""\n TEST STORY
Name 1 is {name1}
Name 2 is {name2}
""")