# NumPy special operatons:
import numpy as np
a = np.array([[1,2,3],[2,4,5]])
print(a.ndim) # returns dimention of the array -- 2
print(a.shape) # gives shape of numpy
print(a.size) # gives size
c= print(a.reshape(3,2)) # to resize the numpy 

###############

# SLicing of numpy array

import numpy as np

a= np.array([[2,3,4,5],[1,2,3,4],[4,5,6,9]])
print(a[0,2]) # gives 4

print(a[0:,2]) # gives array([4, 3]) gives all rows 2nd colum
print(a[0:3,3]) # gives rows 3rd column

#########################
# Arithmatic operations on numpy array

a1=np.array([[1,2,3],[5,6,7]])
a2=np.array([[9,6,3],[4,8,1]])
print(a1+a2)
print(a1-a2)
print(a1*a2)
print(a1/a2)
print(a1%a2)
