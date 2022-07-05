import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 2, 3, 5, 6, 4, 10, 8, 12, 15, 14])
y = np.array([2, 10, 5, 11, 5, 2, 2, 7, 9, 10, 12])
colors = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
sizes = np.array([5, 10, 15, 18, 20, 22, 25, 30, 32, 35, 40])
# colors1 = np.array(["beige","brown","gray","cyan","magenta", "hotpink", "aqua", "maroon"])
plt.scatter(x, y, c=colors, cmap='viridis')

# compairing

x = np.array([0, 2, 2.5, 4, 6, 8, 7, 9, 10, 13, 15])
y = np.array([1, 3, 5, 7, 11, 15, 9, 10, 12, 9, 5])
# colors2 = np.array(["red","green","blue","yellow","pink","black","orange","purple"])
plt.scatter(x, y, c=colors, cmap='viridis', s=sizes, alpha= 0.4)

# change size of dots
# using s


plt.colorbar()
plt.show()
