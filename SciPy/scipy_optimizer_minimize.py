from scipy.optimize import minimize
# func, x0, method, callback, options
def eqn(x):
    return x**2 + x + 2
mymin = minimize(eqn, 0, method='BFGS')
print(mymin) # x와 fuc 값 확인 가능