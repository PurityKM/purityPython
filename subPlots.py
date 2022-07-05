import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 3, 4])
y = np.array([2, 3, 4, 5])

#plt.subplot(1, 2, 1)
plt.subplot(2, 3, 1)
plt.plot(x, y)
plt.title("SALES")

x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])

#plt.suplot(1, 2, 2)
plt.subplot(2, 3, 2)
plt.plot(x, y)
plt.title("CUSTOMERS")

x = np.array([1, 2, 3, 4])
y = np.array([5, 10, 12, 20])

plt.subplot(2, 3, 3)
plt.plot(x, y)
plt.title("PRODUCTS")


x = np.array([1, 2, 3, 4])
y = np.array([3, 6, 10, 12])

plt.subplot(2, 3, 4)
plt.plot(x, y)
plt.title("PRICE")


x = np.array([1, 2, 3, 4])
y = np.array([15, 20, 25, 35])

plt.subplot(2, 3, 5)
plt.plot(x, y)
plt.title("QUANTITY")


x = np.array([1, 2, 3, 4])
y = np.array([6, 12, 24, 30])

plt.subplot(2, 3, 6)
plt.plot(x, y)
plt.title("QUALITY")

plt.suptitle("PURITY SHOP")
plt.show()