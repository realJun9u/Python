import numpy as np
# Log
arr = np.arange(1, 10)
print(np.log2(arr))
print(np.log10(arr))
print(np.log(arr))
# Sum
arr1 = np.arange(1, 4)
arr2 = np.arange(1, 4)
print(np.sum([arr1, arr2]))
print(np.sum([arr1, arr2], axis=1))
# Cummulative Sum (partial sum)
arr = np.arange(1, 4)
print(np.cumsum(arr))
# Product
arr = np.arange(1, 5)
print(np.product(arr))
arr1 = np.arange(1, 5)
arr2 = np.arange(5, 9)
print(np.product([arr1, arr2]))
print(np.product([arr1, arr2], axis=1))
# Cummulative Product
arr = np.arange(1, 5)
print(np.cumproduct(arr))
# Differences (인접한 원소간 차)
arr = np.array([10, 15, 25, 5])
print(np.diff(arr)) # default n=1
print(np.diff(arr, n=2))
# Find LCM
arr = np.array([3, 6, 9])
print(np.lcm.reduce(arr))
# Find GCD
arr = np.array([20, 8, 32, 36, 16])
print(np.gcd.reduce(arr))