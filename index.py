
import time
import random
import numpy as np
gameFinished= True


def WeGuess():    
    
    arr  = np.arange(101) 
    haveNumnber = False
    while haveNumnber == False:
        numberGuess_arr  = np.arange(101) 
        print("\n \n")    
        print("|-----------------------------------------------------|")
        print("| To play think of a number between 1 and a 100       |")
        print("| And well try to guess it                            |")
        print("|-----------------------------Y------------------------|\n")
        if (input("         Do you have a Number (Y/N)\n").upper()) =='Y':
            yes_no = input("Is your number Higher then or 50 (Y/N)\n").upper()
            if yes_no =='Y':            
                w_numberGuess_arr = np.delete(numberGuess_arr,np.where(numberGuess_arr<50))
                print(w_numberGuess_arr)
            elif yes_no == 'N':
                w_numberGuess_arr = np.delete(numberGuess_arr,np.where(numberGuess_arr>50))        
                print(w_numberGuess_arr)   
            
        else:   
            haveNumnber =False


def UserGuess():
     print("*** To play think of a number between 1 and a 100 **\n\n")





while gameFinished == True:
    print("\n \n \n \n\n")
    print("|-----------------------------------------------------|")
    print("|                     - Welcome -                     |")
    print("|                      Game Mode                      |")
    print("|-----------------------------------------------------|")
    print("| option 1 : You think of a Number and we guess it    | ")
    print("| option 2 : We think of a Number and you guess it    | ")
    print("|-----------------------------------------------------|\n")
    gamemode = input("** Choose and Option (1/2)\n")

    if gamemode =='1':
        WeGuess()
    elif gamemode =="2":
        UserGuess()
    else:
        print("\nInvalid input, Please Try Agian")
print("Bye")