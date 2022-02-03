import time
import random
import numpy as np

w_numberGuess_arr  = np.arange(101) 
yes_no =''
def guessNumber(i_numberArray,i_key):
    if i_key.upper() == 'Y':
        o_numberArray = i_numberArray
        question = "aaaaaa"
        haveNumber = False
        return o_numberArray ,question, haveNumber
        
    elif i_key.upper() == 'N':    
        o_numberArray = i_numberArray
        question = "BBBB"
        haveNumber = False
        return o_numberArray ,question, haveNumber
    else:
        question = "CCCC"   
        o_numberArray = i_numberArray
        haveNumber = False
        return (o_numberArray ,question, haveNumber)

haveNumber =False
yes_no = ' '
while haveNumber == False:
    w_numberGuess_arr ,question, haveNumber = guessNumber(w_numberGuess_arr,yes_no)
    yes_no = input(f'{question}\n')  
