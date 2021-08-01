#%%
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Normal distribution
# sns.distplot(np.random.normal(loc=10, scale=2, size=(1000)), hist=False)

# Binomial distribution is Discrete
# sns.distplot(np.random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

# Difference Between Normal and Binomial Distribution
# sns.distplot(np.random.normal(50, 5, 1000), hist=False, label='normal')
# sns.distplot(np.random.binomial(100, 0.5, 1000), hist=False, label='binomial')
# plt.legend()

# Poisson Distribution is Discrete
# sns.distplot(np.random.poisson(lam=2, size=1000), kde=False)

# Difference Between Normal and Poisson Distribution
# sns.distplot(np.random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
# sns.distplot(np.random.poisson(lam=50, size=1000), hist=False, label='poisson')
# plt.legend()

# Difference Between Poisson and Binomial Distribution
sns.distplot(np.random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(np.random.poisson(lam=10, size=1000), hist=False, label='poisson')
plt.legend()
plt.show() 

# %%
