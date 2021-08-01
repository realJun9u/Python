import numpy as np
# 1D array
arr1 = np.array([1, 2, 3, 4, 5])
#arr = np.array((1, 2, 3, 4, 5))
print(arr1)
print(type(arr1))
# 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
# 3D array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3)
# check dimension
print(arr1.ndim, arr2.ndim, arr3.ndim)