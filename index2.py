import numpy as np


arr  = np.arange(101) 
new_arry = np.delete(arr,np.where(arr>50))
print(arr)
print(new_arry)



print((lambda x: (x + 1))(5))