import time
import random
import numpy
gameFinished = True

print("|-------------------|")
print("|       Welcome     |")
print("|-------------------|\n")
while gameFinished == True:

    print("|-----------------------------------------------------|")
    print("|                      Game Mode                      |")
    print("|-----------------------------------------------------|")
    print ("| option 1 : You think of a Nuber and we guess it    | ")
    print ("| option 2 : We think of a Nuber and you guess it    | ")
    print("|-----------------------------------------------------|\n")
    gamemode = input("** Choose and Option (1/2)\n")

    if gamemode =='1':
        WeGuess()
    elif gamemode =="2":
        UserGuess()
    else:
        print("\nInvalid input, Please Try Agian")