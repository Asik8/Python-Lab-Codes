import numpy as np

# 0 dimentional
a = np.array(25)
# print(a)

# 1D 
b = np.array([1,2,3,4,5])
# print(b)
# print(type(b))

# 2D 
c = np.array([[1,2,3,4,5],[2,6,5,4,5]])
# print(c)
# print(type(c))

# 3D In this case you need more than one 2D arrays
d = np.array([[[1,2,3,4,5],[2,6,5,4,5]],[[9,8,7,6,5],[5,4,3,2,1]]])
# print(d)
# print(type(d))

# We use ndim to check the dimentions of an numpy array
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim) 


# If you want to create a higher dimentianal array then
Higher = np.array([1,2,3,4,5],ndmin=5) # here used 5 to create 5D array
print(Higher)
print(Higher.ndim)