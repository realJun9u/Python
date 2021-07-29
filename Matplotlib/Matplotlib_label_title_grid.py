#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)
# title xlabel ylabel
# fontdict
# loc (only title) left right center
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'red','size':15}
plt.title("Sports Watch Data", fontdict=font1, loc='right')
plt.xlabel("Average Pulse", fontdict=font2)
plt.ylabel("Calorie Burnage", fontdict=font2)
# grid
# axis='x' or 'y' or 'both'
# color linestyle linewidth
plt.grid(axis='both', c='c', ls='--', lw='0.5')

plt.show()
# %%
