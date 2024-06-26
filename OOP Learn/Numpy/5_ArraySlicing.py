import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5]) # 2,3,4,5

a = np.array([1, 2, 3, 4, 5, 6, 7])
# print(a[4:])
# print(a[:4])

b = np.array([1, 2, 3, 4, 5, 6, 7])
# print(b[-3:-1])


# -------------------------------------->STEP slicing<--------------------------------------------------------
n1 = np.array([1, 2, 3, 4, 5, 6, 7])
# print(n1[0:5:2])

n2 = np.array([1, 2, 3, 4, 5, 6, 7])
# print(n2[::2])

# -------------------------------------->Slicing 2-D Arrays<--------------------------------------------------

s1 = np.array([[1, 2, 3, 4, 5], 
               [6, 7, 8, 9, 10]])
# print(s1[1, 1:4])

s2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(s2[0:2, 2])

s3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(s3[0:2, 1:4])