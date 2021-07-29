# Summary
import matplotlib.pyplot as plt
import numpy as np

# fmc : marker|linestyle|color
plt.plot(x, y, c, ls, lw, marker, ms, mec, mfc)

# font={"family":"","color":"","size":}
plt.title("Title name", fontdict, loc)
plt.xlabel("xlabel name", fontdict)
plt.ylabel("ylabel name", fontdict)

plt.grid(axis, c, ls, lw)

plt.subplot(1, 2, 1)
plt.suptitle("Super Title name")

plt.scatter(x, y, color, c(colors), cmap, s(size), alpha)
plt.colormaps()
plt.colorbar()
# width, height default=0.8
plt.bar(x, y, color, width)
plt.barh(x, y, color, height)

plt.hist(x)

plt.pie(y, colors, labels, startangle, explode, shadow)
plt.legend(title)