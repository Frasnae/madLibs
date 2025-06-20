import madFunctions

loop = 'y'
while loop != 'n':
    madFunctions.empty()
    madFunctions.fill()
    loop = 'x'
    while loop != 'y' and loop != 'n':
        loop = input("\nContinue? (y/n) ")
        loop = loop.lower()
