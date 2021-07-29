#%%
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
#plt.plot(ypoints, marker = '*')

# fmt: marker|line|color
#plt.plot(ypoints, 'o:r')

# markersize, ms
# markeredgecolor, mec
# markerfacecolor, mfc
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'm')
plt.show()

# %%
