import numpy as np

a = np.array([1,2,3,4,5])
b = a.copy()
a[0] = 34
# print(a)
# print(b)

# Use of view() function:

c = np.array([3,4,5,6,7,8])
d = c.view() # View function update the value of an index for both c and d while copy can't.
c[2] = 67
c[0] = 7
# print(c)
# print(d)

# Check if Array Owns its Data:
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base) # base attribute checks if an array owns it's data or not:
print(y.base)