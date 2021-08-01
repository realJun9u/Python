# Summary Numpy  
# https://www.w3schools.com/python/numpy/default.asp  
# Array  
import numpy as np  
import seaborn as sns  
create ndarray: np.array()  
> dtype='i b u f c m M O S U V'  
> ndmin=  
check dimension: arr.ndim  
check dtype: arr.dtype  
change dtype: newarr = arr.astype(' ')  
# Copy  
deep copy: np.copy(arr)  
shallow copy: np.view(arr)  
check base: arr.base  
# Shape
check shape: arr.shape  
reshape: arr.reshape()  
> -1 : numpy will calculate  
# Iterate
iterate: np.nditer(arr)  
> flags=['buffered'], op_dtypes=' '  
enumerated iteration: np.ndenumerate(arr)  
> return index, value  
# Join
join array: np.concatenate((arr1, arr2), axis=)  
join array: np.stack((arr1, arr2), axis=)  
stacking along row: np.hstack((arr1, arr2))  
stacking along column: np.vstack((arr1, arr2))  
stacking along depth: np.dstack((arr1, arr2))  
# Split
split: np.array_split(arr, integer, axis=)  
newarr = np.array_split(arr, 3) = np.hsplit(arr, 3)  
newarr = np.array_split(arr, 3, axis=) = np.vsplit(arr, 3)  
# Search
search: np.where(arr condition) return index  
search sorted:np.searchsorted(arr, insertvalue) return index  
# Sort
sort: np.sort(arr)  
# Filter
filter_arr = [True, False, True]  
newarr = arr[filter_arr]  
filter_arr = arr % 2 == 0  
newarr = arr[filter_arr]  
# Numpy Random
# seaborn: plot distribution
np.random.normal(loc,scale,size)  
np.random.binormal(n,p,size)  
np.random.poisson(lam,size)  
np.random.uniform(lower,upper,size)  
np.random.logistic(loc,scale,size)  
np.random.multinormal(n,pvals,size)  
np.random.exponential(scale,size)  
np.random.chisquare(df,size)  
np.random.rayleigh(scale,size)  
# Numpy ufunc
# Create ufunc
np.frompyfunc(function, inputs, outputs)  
# Arithmetic
np.add(arr1, arr2)  
np.subtract(arr1, arr2)  
np.multiply(arr1, arr2)  
np.divide(arr1, arr2)  
np.power(arr1, arr2)  
np.remainder(arr1, arr2)  
np.divmod(arr1, arr2)  
np.absolute(arr)  
# Truncation
np.trunc(arr)  
np.fix(arr)  
np.around(arr, k)  
np.floor(arr)  
np.ceil(arr)  
# Log
np.log2(arr)  
np.log10(arr)  
np.log(arr)  
# Sum
np.sum([arr1, arr2])  
np.sum([arr1, arr2], axis=1)  
np.cumsum([arr1, arr2])  
# Product
np.product([arr1, arr2])  
np.product([arr1, arr2], axis=1)  
np.cumproduct([arr1, arr2])  
# Difference
np.diff([arr1, arr2], n)  
# LCM
np.lcm.reduce(arr)  
# GCD
np.gcd.reduce(arr)  
# Trigometric Function
np.cos(arr)  
np.arccos(arr)  
np.deg2rad(arr)  
np.rad2deg(arR)  
np.hypot(base, perp)  
np.sinh(arr)  
np.arcsinh(arr)  
# Set
np.unique(arr)  
np.union1d(set1, set2)  
np.intersect1d(set1, set2)  
np.setdiff1d(set1, set2)  
np.setxor1d(set1, set2)  