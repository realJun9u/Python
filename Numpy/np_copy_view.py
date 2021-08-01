import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
arr[0] = 7
print(x, x.base)
print(y, y.base)