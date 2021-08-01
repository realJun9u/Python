import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# Iterating 3-D Arrays
for x in arr:
  for y in x:
    for z in y:
      print(z)
print("")
# Iterating Arrays Using nditer()
for x in np.nditer(arr):
  print(x)
print("")
# Iterating Array With Different Data Types 
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
print("")
# Iterating With Different Step Size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:,::2]):
  print(x)
print("")
# Enumerated Iteration Using ndenumerate()
for idx, x in np.ndenumerate(arr):
  print(idx, x)

