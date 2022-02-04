import time
import random
import numpy as np


class guessNumber:
    
    def __init__(self,i_numberArray,i_key,i_median):
       self.i_numberArray = i_numberArray
       self.i_key = i_key
       self.i_median = i_median

    def numberFilter(self):
        try:
            if len(self.i_numberArray)<=2:
                if len(self.i_numberArray)<=1:
                    if self.i_key.upper() == 'Y':
                        question =f"aa you number Greater{self.i_numberArray[1]}"
                        print(question)
                        haveNumber = False                     
                        return (self.i_numberArray,question,haveNumber,new_median)
                    elif self.i_key.upper() == 'N':    
                        haveNumber = False
                        question =f"cc you number Greater{self.i_numberArray[0]}"
                        print(question)                     
                        return (self.i_numberArray,question,haveNumber,new_median)
                else:    
                    if self.i_key.upper() == 'Y':
                        question =f"is you number Greater Then{self.i_numberArray[1]}"
                        print(question)
                        haveNumber = False                     
                        return (self.i_numberArray,question,haveNumber,new_median)
                    elif self.i_key.upper() == 'N':    
                        haveNumber = False
                        question =f"is you number Greater Then{self.i_numberArray[0]}"
                        print(question)                     
                        return (self.i_numberArray,question,haveNumber,new_median)
            else:    
                if self.i_key.upper() == 'Y':
                    print(self.i_numberArray)
                    o_numberArray = np.delete(self.i_numberArray,np.where(self.i_numberArray<=round(self.i_median)))       
                    new_median = round(np.median(o_numberArray))
                    question = f"Is Your Number Greater then {new_median}"
                    haveNumber = False
                    print(o_numberArray)
                    return (o_numberArray,question,haveNumber,new_median)            
                elif self.i_key.upper() == 'N':              
                        o_numberArray = np.delete(self.i_numberArray,np.where(self.i_numberArray>round(self.i_median)))   
                        new_median = round(np.median(o_numberArray))
                        question = f"Is Your Number Greater then {new_median}"
                        haveNumber = False
                        print(o_numberArray)        
                        return (o_numberArray,question,haveNumber,new_median)
                else:
                    new_median = np.median(self.i_numberArray)
                    question = f"Is Your Number Greater then {new_median}"   
                    o_numberArray = self.i_numberArray
                    haveNumber = False
                    return (o_numberArray,question,haveNumber,new_median)
        except:
            question = 'Error Please try again'                    
            return (self.i_numberArray,question,True,0)
    


w_numberGuess_arr  = np.arange(101)
haveNumber =False
yes_no = ' '
w_median =0
while haveNumber == False:
    
    tst = guessNumber(w_numberGuess_arr,yes_no,w_median).numberFilter() 
    w_median = tst[3]
    w_numberGuess_arr =tst[0]
    haveNumber =tst[2]
    yes_no = input(f'{tst[1]}\n')   
    
