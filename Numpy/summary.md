# Summary Numpy Tutorial  
# https://www.w3schools.com/python/numpy/default.asp  
# Array  
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
# 1
filter_arr = [True, False, True]  
newarr = arr[x]  
# 2
filter_arr = arr % 2 == 0  
newarr = arr[filter_arr]  


