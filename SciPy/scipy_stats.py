# statistical significance means that the result that was produced has a reason behind it, it was not produced randomly, or by chance.
# Hypothesis is an assumption about a parameter in population.
# Null Hypothesis 귀무가설, Alternate Hypothesis 대립가설
# If p value <= alpha we reject the null hypothesis and say that the data is statistically significant.

import numpy as np
# T-Test 두 변수의 유의적 차이 결정
from scipy.stats import ttest_ind
# KS test 주어진 값이 분포를 따르는지 결정.
# test value와 CDF 매개변수 갖는다.
from scipy.stats import kstest
# summary of values in an array
# skewness: A measure of symmetry in data. For normal distributions it is 0.
# kurtosis: A measure of whether the data is heavy or lightly tailed to a normal distribution.
from scipy.stats import describe
# Normality tests are based on the skewness and kurtosis.
from scipy.stats import normaltest
from scipy.stats import skew
from scipy.stats import kurtosis

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)
res = ttest_ind(v1, v2)
print(res)
print("")

res = ttest_ind(v1, v2).pvalue
print(res)
print("")

v = np.random.normal(size=100)
res = kstest(v, "norm")
print(res)
print("")

res = describe(v)
print(res)
print("")

res = normaltest(v)
print(res)
print(skew(v))
print(kurtosis(v))
print("")