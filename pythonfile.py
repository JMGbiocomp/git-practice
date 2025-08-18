import pandas as pd
import numpy as np
import random

#basic python data structures
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #list of 10 values
b = {"allen": 1, "beth": 2, "cathy": 3, "dan": 4, "eddy": 5, "fred": 6, "greg": 7, "helen": 8, "ian": 9} #dictionary of 10 key: value pairs
c = {10, 11, 12, 13, 14, 15, 16, 17, 18, 19} #set of 10 values
d = (20, 21, 22, 23, 24, 25, 26, 27, 28, 29) #tuple with 10 values

#basic python data structure evaluation 
#print(a, type(a))
#print(b, type(b))
#print(c, type(c))
#print(d, type(d))

#NumPy data structures
py_data_list = [a, b, c, d]
for l in py_data_list:
    np_array = np.array([l]) #generate array
    np_shape = np.shape(np_array) #dimensions of array
    np_dim = np.ndim(np_array) #number of dimensions fo array
    print("basic structure:", l)
    print("array:", np_array)
    print("shape:", np_shape) 
    print("dimensions:", np_dim)
#sets and dictionaries do not simply convert to arrays using np.array([]) function
#not including the brackets 'np.array()' will treat the entire basic data structure as a single value in the array

z = np.array([a, a])
print(z)

for l in py_data_list:
    for m in py_data_list:
        np_array = np.array([l, m]) #generate array
        np_shape = np.shape(np_array) #dimensions of array
        np_dim = np.ndim(np_array) #number of dimensions fo array
        print("basic structure:", l, m)
        print("array:", np_array)
        print("shape:", np_shape) 
        print("dimensions:", np_dim)


