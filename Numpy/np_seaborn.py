#%%
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# plot distribution
sns.distplot([0, 1, 2, 3, 4, 5])
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()