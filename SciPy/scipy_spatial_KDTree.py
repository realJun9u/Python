from scipy.spatial import KDTree

points = [(1, -1), (2, 3), (-2, 3), (2, -3)]

res = KDTree(points).query((1, 1))
print(res)
