#%%
import matplotlib.pyplot as plt
import numpy as np
# plt.bar, plt.barh
# color width(defalut=0.8) height(default=0.8)
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color='blue', width=0.5)
#plt.barh(x, y, color='red', height=0.1)
plt.show()