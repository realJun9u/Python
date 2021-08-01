import numpy as np
# trunc(), fix()
# around(), floor(), ceil()
# Truncation - 정수부
darr = [-3.1666, 3.6667]
arr = np.trunc(darr)
print(arr)
arr = np.fix(darr)
print(arr)
# Rounding - 소수 n 번째까지 표시
arr = np.around(darr, 2)
print(arr)
# Floor - 버림
arr = np.floor(darr)
print(arr)
# Ceil - 올림
arr = np.ceil(darr)
print(arr)