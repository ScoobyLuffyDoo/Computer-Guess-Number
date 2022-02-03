
import time
import random
import numpy as np
gameFinished= True


def WeGuess():    
    
    arr  = np.arange(101) 
    have_Number = False
    while have_Number == False:
        numberGuess_arr  = np.arange(101) 
        print("\n \n")    
        print("|-----------------------------------------------------|")
        print("| To play think of a number between 1 and a 100       |")
        print("| And well try to guess it                            |")
        print("|-----------------------------Y-----------------------|\n")
        # Do you have a number
        if (input("         Do you have a Number (Y/N)\n").upper()) =='Y':
            yes_no = input("Is your number Higher then 50 (Y/N)\n").upper()
            # Is number > 50 (if)
            if yes_no =='Y':            
                w_numberGuess_arr = np.delete(numberGuess_arr,np.where(numberGuess_arr<50))
                yes_no = input("Is your Number An Even Number (Y/N)\n").upper()
                # is number even Number
                if yes_no == 'Y':
                    w_numberGuess_arr = list (filter (lambda x: (x % 2 == 0), w_numberGuess_arr))
                    w_median = w_numberGuess_arr[(round(len(w_numberGuess_arr)/2))]
                    yes_no = input(f"Is your Number Higher then {w_median} (Y/N)\n").upper() 
                    # is number > median 
                    if yes_no == 'Y': 
                        w_numberGuess_arr = np.delete(w_numberGuess_arr,np.where(w_numberGuess_arr<w_median))                            
                        yes_no = input(f"Is your Number Three Digits (Y/N)\n").upper()     
                        # 3 Digits 
                        if yes_no == 'Y':
                            w_numberGuess_arr = np.delete(w_numberGuess_arr,np.where(w_numberGuess_arr<max(w_numberGuess_arr))) 
                            print(f"Your Number is {w_numberGuess_arr}")
                            have_Number =True
                        # 3 Digits 
                        elif yes_no =='N':
                            w_numberGuess_arr = np.delete(w_numberGuess_arr,np.where(w_numberGuess_arr>max(w_numberGuess_arr)-1))                              
                            w_median = w_numberGuess_arr[(round(len(w_numberGuess_arr)/2))]
                            yes_no = input(f"Is your Number Higher then {w_median} (Y/N)\n").upper()
                            # is number > median2 
                            if yes_no == 'Y':
                                w_numberGuess_arr = np.delete(w_numberGuess_arr,np.where(w_numberGuess_arr<w_median))      
                                print(w_numberGuess_arr)
                                w_median = w_numberGuess_arr[(round(len(w_numberGuess_arr)/2))]
                                yes_no = input(f"Is your Number Higher then {w_median} (Y/N)\n").upper()
                                # is number > median 3
                                if yes_no == 'Y':
                                    w_numberGuess_arr = np.delete(w_numberGuess_arr,np.where(w_numberGuess_arr<w_median))      
                                    print(w_numberGuess_arr)                                                                               
                                    w_median = np.median(w_numberGuess_arr)
                                    yes_no = input(f"Is your Number Higher then {round(w_median)} (Y/N)\n").upper()
                                    # is number > median 4
                                    if yes_no == 'Y':
                                        w_numberGuess_arr = np.delete(w_numberGuess_arr,np.where(w_numberGuess_arr<=w_median))      
                                        print(f'your number is {w_numberGuess_arr}' )
                                        have_Number =True                                                                                
                                    # is number > median 4    
                                    elif yes_no =='N':
                                        w_numberGuess_arr = np.delete(w_numberGuess_arr,np.where(w_numberGuess_arr>w_median))    
                                        print(w_numberGuess_arr)    
                                        yes_no = input(f"Is your Number Higher then {round(w_numberGuess_arr[0])} (Y/N)\n").upper()
                                        if yes_no == 'Y':
                                            w_numberGuess_arr = np.delete(w_numberGuess_arr,np.where(w_numberGuess_arr<=w_numberGuess_arr[0]))                                                
                                            print(f'Your Number is {w_numberGuess_arr}')
                                        elif yes_no =='N':
                                            w_numberGuess_arr = np.delete(w_numberGuess_arr,np.where(w_numberGuess_arr>w_numberGuess_arr[0]))                                                
                                            print(f'Your Number is {w_numberGuess_arr}')
                                # is number > median 3
                                elif yes_no =='N':        
                                    w_numberGuess_arr = np.delete(w_numberGuess_arr,np.where(w_numberGuess_arr>w_median))    
                                    print(w_numberGuess_arr)    
                            # is number > median2    
                            elif yes_no =='N':    
                                w_numberGuess_arr = np.delete(w_numberGuess_arr,np.where(w_numberGuess_arr>w_median))    
                                print(w_numberGuess_arr)
                    # is number < median
                    elif yes_no =='N':  
                        w_numberGuess_arr = np.delete(w_numberGuess_arr,np.where(w_numberGuess_arr>w_median))    
                        print(w_numberGuess_arr)






                # is number / 2
                elif yes_no =='N':
                    w_numberGuess_arr = list (filter (lambda x: (x % 2 != 0), w_numberGuess_arr))                
                    print(w_numberGuess_arr)
                    w_median = w_numberGuess_arr[(round(len(w_numberGuess_arr)/2))]
                    yes_no = input(f"Is your Number Higher then {w_median} (Y/N)\n").upper()
                     # is number > median 
                    if yes_no == 'Y':
                        w_numberGuess_arr = np.delete(w_numberGuess_arr,np.where(w_numberGuess_arr<w_median))    
                        print(w_numberGuess_arr)
                    # is number > median 
                    elif yes_no =='N':  
                        w_numberGuess_arr = np.delete(w_numberGuess_arr,np.where(w_numberGuess_arr>w_median))    
                        print(w_numberGuess_arr)
    



            # Is number > 50 (if)                    
            elif yes_no == 'N':
                w_numberGuess_arr = np.delete(numberGuess_arr,np.where(numberGuess_arr>50))
                yes_no = input("Is your Number An Even Number (Y/N)").upper()
                # is number / 2
                if yes_no == 'Y':
                    w_numberGuess_arr = list (filter (lambda x: (x % 2 == 0), w_numberGuess_arr))
                    print(type(w_numberGuess_arr))
                    yes_no = input("Is your Number a single Digit (Y/N)").upper()
                    
                    

                # is number / 2    
                elif yes_no =='N':
                    w_numberGuess_arr = list (filter (lambda x: (x % 2 == 0), w_numberGuess_arr))                
                    print(w_numberGuess_arr)
                     
        # Do you have a number    
        else:   
            have_Number =False


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