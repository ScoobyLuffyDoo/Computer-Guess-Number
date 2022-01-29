from pickle import FALSE
import time
import random
# from numpy import random
gameFinished= True
haveNumnber = True

def WeGuess():    
    rangeList = list(range(1,101))
    while haveNumnber == False:
        print("*** To play think of a number between 1 and a 100 ")
        print("** And well try to guess it\n\n")
        if (input("Do you have a Number (Y/N)").upper()) =='Y':
            yes_no = input("Is your number Higher then 50 (Y/N)").upper
            
        else:   
            haveNumnber =False


def UserGuess():
     print("*** To play think of a number between 1 and a 100 **\n\n")



print("|-------------------|")
print("|       Welcome     |")
print("|-------------------|\n")
print ("Press enter to start")
while input().upper != 'CLOSE':
    while gameFinished == True:

        print("|-----------------------------------------------------|")
        print("|                      Game Mode                      |")
        print("|-----------------------------------------------------|")
        print ("| option 1 : You think of a Nuber and we guess it    | ")
        print ("| option 2 : We think of a Nuber and you guess it    | ")
        print ("| Close    : Type Close to end the Game              | ")
        print("|-----------------------------------------------------|\n")
        gamemode = input("** Choose and Option (1/2)\n")

        if gamemode =='1':
            WeGuess()
        elif gamemode =="2":
            UserGuess()
        else:
            print("\nInvalid input, Please Try Agian")
print("Bye")