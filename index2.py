import time
import random
import numpy as np


class guessNumber:
    
    def __init__(self,i_numberArray,i_key):
       self.i_numberArray = i_numberArray
       self.i_key = i_key

    def numberFilter(self):
        if self.i_key.upper() == 'Y':
            w_median = np.median(self.i_numberArray)
            o_numberArray = np.delete(self.i_numberArray,np.where(self.i_numberArray<=round(w_median)))           
            question = f"Is Your Number Greater then {w_median}"
            haveNumber = False
            return o_numberArray ,question, haveNumber
            
        elif self.i_key.upper() == 'N': 
            w_median = np.median(self.i_numberArray)
            o_numberArray = np.delete(self.i_numberArray,np.where(self.i_numberArray>=round(w_median)))     
            question = f"Is Your Number Greater then {w_median}"
            haveNumber = False
            return o_numberArray ,question, haveNumber
        else:
            question = "They Key is Lower"   
            o_numberArray = self.i_numberArray
            haveNumber = False
            return (o_numberArray ,question, haveNumber)
         
    


w_numberGuess_arr  = np.arange(101)
haveNumber =False
yes_no = 'Y'
while haveNumber == False:
    
    tst = guessNumber(w_numberGuess_arr,yes_no).numberFilter() 
    w_numberGuess_arr =tst[0]
    haveNumber =tst[2]
    yes_no = input(f'{tst[1]}\n')   
    
