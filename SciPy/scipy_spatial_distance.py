# 두 점 사이 거리
from scipy.spatial.distance import euclidean
# 두 점 사이 상하좌우 이동만 가능할 때 이동 횟수
from scipy.spatial.distance import cityblock
# 두 점 사이 각의 코사인 값
from scipy.spatial.distance import cosine
# 두 binary의 각 bit값들이 서로 다른 비율
from scipy.spatial.distance import hamming

p1 = (1, 0)
p2 = (10, 2)

res = euclidean(p1, p2)
print(res)

res = cityblock(p1, p2)
print(res)

res = cosine(p1, p2)
print(res)

p1 = (1, 0, 1) # True, False, True
p2 = (0, 1, 1) # False, True, True
res = hamming(p1, p2)
print(res)