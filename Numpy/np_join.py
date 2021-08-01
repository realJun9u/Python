import numpy as np
# concatenate(), stack()
# Joining NumPy 1D Arrays 
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr, arr1.ndim, arr1.shape, arr2.ndim, arr2.shape, arr.shape)
print("")
# Joining NumPu 2D Arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2))
print(arr, arr1.shape, arr2.shape, arr.shape)
arr = np.concatenate((arr1, arr2), axis=1)
print(arr, arr1.shape, arr2.shape, arr.shape)
print("")
# Joining Arrays Using Stack Functions
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1) 
print(arr)
print("")
# Stacking Along Rows
arr = np.hstack((arr1, arr2))
print(arr, arr.ndim)
print("")
# Stacking Along Columns
arr = np.vstack((arr1, arr2))
print(arr, arr.ndim)
print("")
# Stacking Along Height (depth)
arr = np.dstack((arr1, arr2))
print(arr, arr.ndim)
print("")