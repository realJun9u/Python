#%%
import matplotlib.pyplot as plt
import numpy as np
# 원그래프는 합이 100이어야 한다.
y = np.array([35, 25, 25, 15])
# plt.pie
# colors labels startangle explode(떼내기) shadow
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(y, colors=mycolors, labels=mylabels, startangle=90, explode=myexplode, shadow=True)
# plt.legend(범례)
# title
plt.legend(title="Four Fruits")
plt.show()
