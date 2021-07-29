#%%
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
# linestyle, ls : - -- -.
#plt.plot(ypoints, linestyle = 'dashed')
#plt.plot(ypoints, ls = '--')

# color, c
#plt.plot(ypoints, c = 'r')

# linewidth, lw
#plt.plot(ypoints, lw = '20.5')

x1 = np.array([2, 3, 4, 5])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)

plt.show()
# %%
