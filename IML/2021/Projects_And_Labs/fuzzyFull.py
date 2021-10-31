import pandas as pd

from arff_parser import arff_to_df_normalized

# Import the libraries to manage the project

import numpy as np
import pandas as pd
import sklearn
from matplotlib import pyplot as plt, gridspec
from scipy.io import arff
from sklearn.cluster import OPTICS, cluster_optics_dbscan
from sklearn.preprocessing import normalize, StandardScaler
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from numpy import linalg as LA

content = "./datasets/vehicle.arff"

df_normalized, data_names = arff_to_df_normalized(content)

print(df_normalized.head())

X = df = df_normalized.to_numpy()

print(X.shape)

# Imputs
# Maximun number of iterations
T = (10)
# Fuzziness degree
m = 2

# Data
# X = df = np.array([[1,2],[2,2.5],[2,3],[9,4],[10,1],[8,4],[9,1.5],[1,1],[4,4],[10,2],[3,7]])
# X = df = np.array([[1,2],[1.1,2],[1,2.1],[9.8,10],[10,10],[10,9],[9,10],[3,7],[3.5,7],[3.2,7],[3.5,7.6]])
print('Our matrix')
print(df)
# n number of instances
n = (X.shape[0])
# p number of fetures
p = (X.shape[1])
#Performance
P = np.zeros([1, n])

'''OPtimal number of clusters'''


def performanceFCM(c, X, V, U, m, n, p):
    P = 0
    x_avg = np.zeros([1, p])
    for i in range(5):
        x_avg[0, i] = sum(X[:, i])
    x_avg = 1 / n * x_avg
    for i in range(c):
        for k in range(n):
            P = P + (U[i, k] ** m * (LA.norm(X[k, :] - V[i, :]) ** 2 - LA.norm(V[i, :] - x_avg) ** 2))

    return P


# c clusters
for c in range(1, n + 1):
    print('TENGO SUEÑO')
    print(c)
    '''STEP1 : Randomly weight selects'''
    U = np.random.random([c, n])
    # Create a weight matrix with random pesos
    for i in range(len(U[0, :])):
        NormWeights = sum(U[:, i])
        U[:, i] = U[:, i] / NormWeights
    print('Our universe U with the weights')

    '''STEP2: Compute the centroids'''
    # Create a centroid matrix
    V = np.zeros([c, p])

    for iteration in range(T):
        # print('Parce vamos en la: ',iteration)

        for i in range(c):
            for j in range(p):
                V_sup = 0
                V_inf = 0
                for k in range(n):
                    V_sup = V_sup + (U[i, k] ** m) * (df[k, j])
                    V_inf = V_inf + (U[i, k] ** m)
                V[i, j] = V_sup / V_inf

        ''' STEP 3: Update the membership matrix # '''
        exponente = (2 / (m - 1))
        for i in range(c):
            for k in range(n):
                u_sumatorio = 0
                u_sup = LA.norm(X[k, :] - V[i, :])
                u_inf = 0
                for j in range(c):
                    u_inf = LA.norm(X[k, :] - V[j, :])
                    u_sumatorio = u_sumatorio + ((u_sup / u_inf) ** exponente)
                U[i, k] = (u_sumatorio ** -1)

    '''Fuzzy clusters to Crisp clusters'''

    Crisp = np.zeros(U.shape, dtype=bool)
    for j in range(n):
        idx = np.argmax(U[:, j])
        Crisp[idx, j] = True

    #for i in range(c):
     #   plt.scatter(X[Crisp[i, :], 0], X[Crisp[i, :], 1])
    # Centroides
    # plt.scatter(V[:,0],V[:,1],marker='*',edgecolors='k')
    # plt.show()

    P[0, c - 1] = performanceFCM(c, X, V, U, m, n, p)

c_vec = np.array(range(1, n + 1))
plt.plot(c_vec, P[0, :])

plt.show()
