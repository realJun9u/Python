# This method of filling values is called imputation
# 1D Interpolation
from scipy.interpolate import interp1d
# UnivariateSpline
# 스플라인 보간법: 전체 구간을 소구간별로 나누어 저차수의 다항식으로 매끄러운 함수를 구하는 방법
from scipy.interpolate import UnivariateSpline
# Radial Basis Function
# 방사형 기저 함수 보간: 가능한 고차원 공간에서 구조화되지 않은 데이터의 정확한 고차 보간법 을 구성 하기 위한 근사 이론 의 고급 방법
from scipy.interpolate import Rbf
import numpy as np

xs = np.arange(10)
ys = 2*xs +1
interp_func = interp1d(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1
interp_func = UnivariateSpline(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)

interp_func = Rbf(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)