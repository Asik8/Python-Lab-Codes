import numpy as np

b = np.array([1,2,3,4,5])
# print(b[1]) # use index to access elements of 1D array

c = np.array([[1,2,3,4,5],
              [2,6,5,4,5]])
# print(c[0,1]) # Enter the row and column of array to acess the 2D array (2nd elements of 1st row)

a = np.array([[[1, 2, 3], 
               [4, 5, 6]], 
              [[7, 8, 9], 
               [10, 11, 12]]])
# print(a)
# print(a[1, 1, 0]) # 2d array number, number of row of 2D arry, num of index 

# Negative indexing:

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -2])