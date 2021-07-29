#%%
import matplotlib.pyplot as plt
import numpy as np
# subplot(row, column, rocation)
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
#plt.subplot(2, 1, 1)
plt.plot(x,y)
plt.title("SALES")
plt.grid()

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
#plt.subplot(2, 1, 2)
plt.plot(x,y)
plt.title("INCOME")
plt.grid()

# super title
plt.suptitle("MY SHOP")
plt.show()