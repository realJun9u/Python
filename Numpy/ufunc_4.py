import numpy as np
# Trigometric Function
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
print(np.cos(arr))
print(np.sin(arr))
arr = np.array([45, 90, 135, 180])
print(np.deg2rad(arr))
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
print(np.rad2deg(arr))
# Inverse Trigometric
arr = np.array([1, -1, 0.1])
print(np.arccos(arr))
# Hypotenues
base = 3
perp = 4
print(np.hypot(base, perp))
# Hyperbolic Function
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
print(np.sinh(arr))
# Invert Hyperbolic
arr = np.array([0.1, 0.2, 0.5])
print(np.arcsinh(arr))

# Create Set
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
print(np.unique(arr))
# Union, Intersection, Difference
arr1 = np.array([1, 2, 3, 4, 4, 4])
arr2 = np.array([3, 4, 5, 5, 5, 6])
print(np.union1d(arr1, arr2))
print(np.intersect1d(arr1, arr2))
set1 = np.unique(arr1)
set2 = np.unique(arr2)
print(np.setdiff1d(set1, set2)) # return [1, 2]
print(np.setxor1d(set1, set2)) # return [1, 2, 5, 6]
