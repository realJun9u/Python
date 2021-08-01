import numpy as np
# Create ufunc
# frompyfunc() 1. function 2. # of inputs 3. # of outputs
def myadd(x, y):
    return x+y
myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1,2,3,4],[5,6,7,8]))
print(type(myadd))
print(type(np.concatenate))
# Arithmetic
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
arr = np.add(arr1, arr2)
print(arr)
arr = np.subtract(arr1, arr2)
print(arr)
arr = np.multiply(arr1, arr2)
print(arr)
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])
arr = np.divide(arr1, arr2)
print(arr)
# Power
arr = np.power(arr1, arr2)
print(arr)
# Remainder
arr = np.remainder(arr1, arr2)
print(arr)
# quotient and mod
arr = np.divmod(arr1, arr2)
print(arr)
# absolute value
arr = np.array([-1, -2, 1, 2, 3, -4])
arr = np.absolute(arr)
print(arr)