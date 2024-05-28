import numpy as np

# 1D Print:
a = np.array([1,2,3,4,5])
# for x in a:
#     print(x)

# 2D Print:
b = np.array([[1, 2, 3], [4, 5, 6]])
# for x in b:
#     print(x) # itearate the rows

# for x in b:
#   for y in x:
#     print(y) # itearate all the elements

# 3D Print and iteration:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in arr:
#   for y in x:
#     for z in y:
#       print(z)
      
# ------------------------------------>Use of ndinter()function<---------------------------

# Itearate 3D array:
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for x in np.nditer(c):
#   print(x)

# ------------------------------------>Use of ndenumerate()function<---------------------------

# Itearate 3D array:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
