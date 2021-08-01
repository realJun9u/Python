import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print(arr.shape)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
newarr = arr.reshape(2, 3, 2)
print(newarr)
# it's a view
print(newarr.base)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# -1 : numpy will calculate
newarr = arr.reshape(2, -1, 2) 
print(newarr)
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)