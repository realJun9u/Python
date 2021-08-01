import numpy as np
# Filtering Arrays
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)
print("")
# Create a filter array that will return only values higher than 42:
filter_arr = []
for x in arr:
    if x > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]
print(newarr)
print("")
# Create a filter array that will return only even elements from the original array:
filter_arr = []
for x in arr:
    if x % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]
print(newarr)
print("")
# Creating Filter Directly From Array
arr = np.array([41, 42, 43, 44])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(newarr)
print("")