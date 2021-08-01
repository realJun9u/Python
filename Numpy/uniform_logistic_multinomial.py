#%%
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Uniform Distribution
# a(lower bound), b(upper bound), size
# sns.distplot(np.random.uniform(size=1000), hist=False)

# Logistic Distribution
# 정규분포와 유사. 정규분포보다 첨도가 더 낮다
# default는 표준 로지스틱 분포(loc=0, scale=1)
# sns.distplot(np.random.logistic(size=1000), hist=False)

# Diferrence Between Logistic and Normal Distribution
# sns.distplot(np.random.normal(size=1000), hist=False, label='normal')
# sns.distplot(np.random.logistic(size=1000), hist=False, label='logistic')
# plt.legend()

# Multinomial Distribution is generalization of binomial distribution
sns.distplot(np.random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=1000))
plt.show()

