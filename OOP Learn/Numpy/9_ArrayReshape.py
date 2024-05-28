import numpy as np

# Reshape 1D to 2D:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
# print(newarr)

# Reshape From 1-D to 3-D
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newa = a.reshape(2, 3, 2)
# print(newa)

# Flattering the array
b = np.array([[1, 2, 3], [4, 5, 6]])
newb = b.reshape(-1) # create 1D array from multi dimentional array
print(newb) 