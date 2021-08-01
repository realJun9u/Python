import numpy as np
# random distribution
x = np.random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(10))
print(x)
x = np.random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)
# random permutation
# shuffle(), permutation()
arr = np.arange(1, 6)
np.random.shuffle(arr)
print(arr)
print(np.random.permutation(arr))