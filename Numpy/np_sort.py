import numpy as np
# Sorting Arrays
arr = np.array([3, 2, 0, 1])
# 방법 1
print(np.sort(arr))
# 방법 2
arr.sort()
print(arr)
print("")

arr = np.array([True, False, True])
print(np.sort(arr))
print("")

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
print("")