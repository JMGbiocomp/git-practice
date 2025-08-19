"""
Purpose: NumPy learning for handling and working with data structures in a python environment, a lead up to Pandas.
Author: Joshua Glowalla
"""
# === Imports ===
import pandas as pd
import numpy as np
import random

# --- basic python data structures ---
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #list of 10 values
b = {"allen": 1, "beth": 2, "cathy": 3, "dan": 4, "eddy": 5, "fred": 6, "greg": 7, "helen": 8, "ian": 9} #dictionary of 10 key: value pairs
c = {10, 11, 12, 13, 14, 15, 16, 17, 18, 19} #set of 10 values
d = (20, 21, 22, 23, 24, 25, 26, 27, 28, 29) #tuple with 10 values

# --- basic python data structure evaluation ---
#print(a, type(a))
#print(b, type(b))
#print(c, type(c))
#print(d, type(d))

# --- NumPy data structures ---
ref_list_1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
ref_array_1 = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
ref_list_2 = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
ref_array_2 = np.array([0, 2, 4, 6, 8, 1, 3, 5, 7, 9])

zero_array = np.zeros(10)
ones_array = np.ones(10)
#print(zero_array)
#print(ones_array)

# --- Evalution of converting basic python structures into arrays ---
def pyDataStructure_Eval(data_list, data_dict, data_set, data_tuple):
    py_data_list = [data_list, data_dict, data_set, data_tuple]
    for l in py_data_list:
        np_array = np.array([l]) #generate array
        np_shape = np.shape(np_array) #dimensions of array
        np_dim = np.ndim(np_array) #number of dimensions fo array
        print("basic structure:", l)
        print("array:", np_array)
        print("shape:", np_shape) 
        print("dimensions:", np_dim)

#pyDataStructure_Eval(a, b, c, d)
#sets and dictionaries do not simply convert to arrays using np.array([]) function
#not including the brackets 'np.array()' will treat the entire basic data structure as a single value in the array

aa_array = np.array([a, a])
#print(aa_array)
ad_array = np.array([a, d])
#print(ad_array)

# --- Testihng syntax for constructing arrays from lists and their correspodning attributes
def array_syntax_tester(structure_1 = 0, structure_2 = 0, structure_3 = 0, high_dim = False):
    """
    -Lists are used to build NumPy arrays
    Arguments:
    structure_1 = 0
    structure_2 = 0
    structure_3 = 0
    """
    if len(structure_1) != len(structure_2):
        print("lists are not equal length")
    else:
        top_dim = list(range(len(structure_1)))
        if high_dim == False:
            if structure_3 == 0:
                a = np.array([structure_1, structure_2])
            else:
                a = np.array([structure_1, structure_2, structure_3])
        else:
            if structure_3 == 0:
                a = np.array([[top_dim, structure_1], [top_dim, structure_2]])
            else:
                a = np.array([[top_dim, structure_1], [top_dim, structure_2], [top_dim, structure_3]])
        print(a)
        print("shape:")
        print(a.shape)
        if high_dim == False:
            print("index [0,4]:")
            print(a[0,4]) #rows 0-1 and columns 0-9 indexes
        else:
            print("index [0,0,4]:")
            print(a[0,0,4]) #rows 0-1 and columns 0-9 indexes
        print("number of dimensions:")
        print(a.ndim)
        print("size or number of elements:")
        print(a.size)
        print("datatype:")
        print(a.dtype)

# --- testing proper syntax for increasing dimensionality of arrays ---    
#array_syntax_tester(a, a)
#array_syntax_tester(a, a, a)
#array_syntax_tester(a, a, high_dim = True)

# --- building arrays from exisitng arrays ---
array_2D = np.array([a, a, a, a, a, a, a, a, a, a]) #list 'a' with 10 elements used to build a 10 x 10 array
#print(array_2D) #view 10 x 10 array
#print(array_2D.shape) #confirm array structure
#print(array_2D[0,:]) #single row slice
#print(array_2D[:,0]) #single column slice

#stacking arrays to add rows or columns; *require homogeneity in length for corresponding dimension
#vstack and hstack
add_array = np.zeros(100) #build a 100 element array with zeroes
add_array = add_array.reshape(10,10) #reshape the zero array to a 10x10 array
array_2D_plusC = np.hstack((array_2D, add_array)) #combine arrays by columns
#print(array_2D_plusC)
array_2D_plusR = np.vstack((array_2D, add_array)) #combine arrays by rows
#print(array_2D_plusR)

#