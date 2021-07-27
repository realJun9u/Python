import numpy as np
from numpy.lib import nanquantile
from scipy.sparse import csr, csr_matrix
# csc: compressed sparse column
# csr: compressed sparse row
arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(arr))
print("")

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr))
print("")

print(csr_matrix(arr).count_nonzero)
print("")

mat = csr_matrix(arr)
mat.eliminate_zeros()
print(mat)
print("")

mat = csr_matrix(arr)
mat.sum_duplicates()
print(mat)
print("")

newarr = csr_matrix(arr).tocsc()
print(newarr)
print("")