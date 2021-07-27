import numpy as np
# Adjency Matrix
from scipy.sparse.csgraph import connected_components
# Shortest path dijkstrat(csgraph, return_predecessors, indices, limit)
from scipy.sparse.csgraph import dijkstra
# all pairs of elements
from scipy.sparse.csgraph import floyd_warshall
# can handle negative weithts
from scipy.sparse.csgraph import bellman_ford
# Depth First Order depth_first_order(csgraph, starting element)
from scipy.sparse.csgraph import depth_first_order
# Breadth First Order
from scipy.sparse.csgraph import breadth_first_order
# csr matrix
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr = csr_matrix(arr)
print(newarr)

print(connected_components(newarr))
print("")

print(dijkstra(newarr, return_predecessors=True, indices=0))
print("")

print(floyd_warshall(newarr, return_predecessors=True))
print("")

arr = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr = csr_matrix(arr)
print(bellman_ford(newarr, return_predecessors=True, indices=0))
print("")

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])
newarr = csr_matrix(arr)
print(depth_first_order(newarr, 1))

print(breadth_first_order(newarr, 1))