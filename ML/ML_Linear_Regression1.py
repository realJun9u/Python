#%%
import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# slope:기울기 intercept:Y절편 r:상관계수
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))
print(r) 
print(myfunc(10))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# %%
