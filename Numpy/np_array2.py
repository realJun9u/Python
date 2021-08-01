import numpy as np
# Indexing
arr = np.array([1, 2, 3, 4])
print(arr[0] + arr[1])
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0, 1])
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])
print(arr[1, 0, -1])
# Slicing
print(arr[1, 0, 0:2])