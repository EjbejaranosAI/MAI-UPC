import numpy as np
import matplotlib.pyplot as plt

N = 200
X = np.random.rand(N) * 10
secreto = 2 * X - 4

error = np.random.randn(N) * 2.25 # error de la distribución normal
Y = 2 * X - 4 + error

plt.scatter(X, Y, label = 'Datos reales')
plt.plot(X, secreto, label = 'La función a modelar')
plt.legend()
show.plot()

def J(w):
    return sum((w[0]*X[k] + w[1] - Y[k])**2 for k in range(0, N))
