from matplotlib import pyplot as plt
import numpy as np

xs = np.arange(1,6)
tops = np.arange(2,12,2)

plt.bar(xs, tops)
plt.show()