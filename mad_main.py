import mad_functions

loop = 'y'
while loop != 'n':
    mad_functions.empty()
    mad_functions.fill()
    loop = 'x'
    while loop != 'y' and loop != 'n':
        loop = input("\nContinue? (y/n) ")
        loop = loop.lower()