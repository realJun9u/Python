#%%
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Exponential Distribution
# 포아송 분포는 일정 기간 동안 이벤트의 발생 횟수
# 지수 분포는 이러한 이벤트 사이의 시간
# sns.distplot(np.random.exponential(scale=5, size=1000), hist=False)

# Chi Square Distribution
# 카이 제곱 분포는 가설 검증에 사용
# sns.distplot(np.random.chisquare(df=1, size=1000), hist=False)

# Rayleigh Distribution
# 신호 처리에 사용
sns.distplot(np.random.rayleigh(scale=1, size=1000), hist=False)
plt.show()