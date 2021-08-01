import numpy as np
# i b u f c m M O S U V
arr = np.array([1, 2, 3, 4])
print(arr.dtype)
arr = np.array([1, 2, 3, 4], dtype='f')
print(arr.dtype)
arr = np.array([1.1, 2.2, 3.3, 4.4])
newarr = arr.astype('i')
print(newarr.dtype)