#%%
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o:r') # 'o'는 점만 찍고 선은 긋지 않는다.
plt.show()
# %%
