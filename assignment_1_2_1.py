import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']), 'Age':pd.Series([25,26,25,23,30,29,23]), 'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
df = pd.DataFrame(d) 
print("Shape of dictionary d: "+ str(df.shape))
print("Size of dictionary d: " + str(d.__sizeof__()) + "bytes")
print("Head of dictionary d: ")
print(str(df.head(1)))
print("Tail of dictionary d: ")
print(str(df.tail(1)))
print("Dtypes of dictionary d: ")
print(df.dtypes)


