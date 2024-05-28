# Data Types in numpy
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

import numpy as np

arr = np.array([1, 2, 3, 4])
a = np.array(['apple', 'banana', 'cherry'])
# print(arr.dtype) # use dtype to check the data type of the array
# print(a.dtype)

b = np.array([1, 2, 3, 4], dtype='S') # For i, u, f, S and U we can define size as well.
# print(b)
# print(b.dtype)

c = np.array([1, 2, 3, 4], dtype='i4')
# print(c)
# print(c.dtype)

# What will happen if the value can't be changed?
# d = np.array(['a', '2', '3'], dtype='i')
# print(d) # it raise a value error 

# Change a float array into a integer type:
e = np.array([1.1, 2.1, 3.1])
newarr = e.astype('i') # astype used to change the variable type of a list
# newarr = e.astype(int) # Here int and 'i' do the same thing
# print(newarr)
# print(newarr.dtype)

# In case of Boolean type:
f = np.array([1, 0, -1])
newf = f.astype(bool) # here 0 means false and for others true
print(newf)
print(newf.dtype)





