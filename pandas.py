# Import pandas library
import pandas as pd

# Creating series using python

ser= pd.Series([1,2,3])
print(type(ser))
print(ser)

#######
ch = pd.Series(["q","w",'w',"dd"])
print(ch)
#########
# Slicing
print(ch[1:2])
