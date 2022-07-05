import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Apples", "Banana", "Lemon", "Pineapple", "Orange"])
y = np.array([10, 4, 7, 9, 10])

plt.bar(x, y, color= "purple", width= 0.4)
#plt.barh(x, y, color= "purple", height= 0.2)
plt.show()

