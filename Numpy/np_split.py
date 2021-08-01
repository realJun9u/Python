import numpy as np
# Splitting NumPy Arrays
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
for x in newarr:
    print(x)
print("")
# Splitting 2-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
# newarr = np.hsplit(arr, 3)
print(newarr)
print("")
newarr = np.array_split(arr, 3, axis=1)
# newarr = np.vsplit(arr, 3)
print(newarr)
print("")