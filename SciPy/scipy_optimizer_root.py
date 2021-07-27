from scipy.optimize import root
from math import cos
# funtion, initial 추측값 2개의 인자 필요
# find root of the equation x + cos(x)
def eqn(x):
    return x + cos(x)
myroot = root(eqn, 0)
print(myroot.x)
print(myroot)