# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([2, 4, 2, 4])
ypoints = np.array([4, 6, 3, 5])
# plt.plot(ypoints, linestyle= 'dotted')

#plt.plot(ypoints, linestyle= 'dashed', color= 'r') #linewidth= 15)
fontdict1 = {
    'family': 'serif',
    'color': 'Red',
    'weight': 'bold',
    'size': '20',
    'style': 'italic'
}
fontdict2 = {
    'family': 'fantasy',
    'color': 'darkred',
    'weight': 'semibold',
    'size': '15',
    'style': 'oblique'
}

plt.plot(xpoints)
plt.plot(ypoints)

#plt.title("Line graph", fontdict1)
plt.title("Line graph", fontdict1, loc= "left")
plt.xlabel("x-axis", fontdict2)
plt.ylabel("y-axis", fontdict2)

plt.grid(color= 'green', linestyle='dotted', linewidth= 0.5)
plt.show()

# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
