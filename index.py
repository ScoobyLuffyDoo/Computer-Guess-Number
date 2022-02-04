import time
import random
import numpy as np


w_numberGuess_arr  = np.arange(101)
haveNumber =False
yes_no = ' '
w_median =0
class guessNumber:
    
    def __init__(self,i_numberArray,i_key,i_median):
       self.i_numberArray = i_numberArray
       self.i_key = i_key
       self.i_median = i_median
    def initial_Filter(self):
        data_Filtered = False
        while data_Filtered ==False:
            yes_no = input("Is Your Number An Even Number (Y/N)\n").upper()
            if  yes_no == 'Y':
                w_numberGuess_arr = np.array(list (filter (lambda x: (x % 2 == 0), self.i_numberArray)))
                w_numberGuess_arr =(w_numberGuess_arr)
                data_Filtered =True
            elif yes_no =='N':
                w_numberGuess_arr = np.array(list (filter (lambda x: (x % 2 != 0), self.i_numberArray)))    
                data_Filtered =True
            else:
                print('please use an valid input')    
        return w_numberGuess_arr
    def numberFilter(self):
        if self.i_key.upper() == 'Y':            
            o_numberArray = np.delete(self.i_numberArray,np.where(self.i_numberArray<round(self.i_median)))       
            new_median = round(np.median(o_numberArray))
            question = f"Is Your Number Greater then {new_median}"
            haveNumber = False
            return (o_numberArray,question,haveNumber,new_median)            
        elif self.i_key.upper() == 'N':              
            o_numberArray = np.delete(self.i_numberArray,np.where(self.i_numberArray>round(self.i_median)))   
            new_median = round(np.median(o_numberArray))
            question = f"Is Your Number Greater then {new_median}"
            haveNumber = False        
            return (o_numberArray,question,haveNumber,new_median)
        else:
            new_median = np.median(self.i_numberArray)
            question = f"Is Your Number Greater then {new_median}"   
            o_numberArray = self.i_numberArray
            haveNumber = False
            return (o_numberArray,question,haveNumber,new_median)
            
print("\n \n \n \n\n")
print("|-----------------------------------------------------|")
print("|                     - Welcome -                     |")
print("|                      Game Mode                      |")
print("|-----------------------------------------------------|")
print("| option 1 : You think of a Number and we guess it    | ")
print("|-----------------------------------------------------|\n")
gamemode = input("** Press Enter Key to start  (1/2)\n")
w_numberGuess_arr = guessNumber(w_numberGuess_arr,' ',0).initial_Filter()
while haveNumber == False:    
    return_Data = guessNumber(w_numberGuess_arr,yes_no,w_median).numberFilter() 
    if len(w_numberGuess_arr)<=1: 
        yes_no = input(f'Is your number{return_Data[0]}\n').upper()   
        if yes_no == 'Y':
            print("Nice")
            haveNumber = True
        elif yes_no == 'N':
            print("Try again")
    else:
        w_median = return_Data[3]
        w_numberGuess_arr =return_Data[0]
        haveNumber =return_Data[2]
        yes_no = input(f'{return_Data[1]}\n')   
    
