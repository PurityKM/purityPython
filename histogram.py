import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(200, 15, 300)

plt.hist(x)
plt.show()