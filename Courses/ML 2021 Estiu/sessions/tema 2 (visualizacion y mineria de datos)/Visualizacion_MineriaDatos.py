import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = np.random.uniform(0, 10, 100)


ax1 = plt.plot(x, y)
plt.show()

ax2 = plt.scatter(x, y)
plt.show()

ax3 = plt.scatter(x, y, c = 'red', marker = 'x')
plt.show()


x1 = np.random.multivariate_normal([0,4], np.eye(2), 100)
x2 = np.random.multivariate_normal([5,8], np.eye(2), 100)

plt.scatter(x1[:,0], x1[:,1], label = 'Cluster 1')
plt.scatter(x2[:,0], x2[:,1], label = 'Cluster 2', marker = 'x')
plt.legend()


