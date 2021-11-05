import pandas as pd

from arff_parser import arff_to_df_normalized
from tqdm import tqdm
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
from numpy import linalg as LA, ndarray

content = "./datasets/vehicle.arff"
df_normalized, data_num_names, data_cat_names, data_names, class_names  = arff_to_df_normalized(content)

print(df_normalized.head())

'''Fuzzy c-Means
In this code we want implement the fuzzy c-means algorithm and at the same time 
calculate the performance for different clusters to obtain the optimal cluster'''

'''Inputs'''
cmax = 8
X = df = df_normalized.to_numpy()   #Dataset
T = 100                             # Maximun number of iterations   #Change to 100 later
m = 2                               # Fuzziness degree
n = (X.shape[0])                    # n number of instances
p = (X.shape[1])                    # p number of features
P = np.zeros([1, 8])                # Performance

'''With the next function we can find the optimal number of clusters'''
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

c_vec: ndarray = np.array(range(1, cmax+1))
for c in tqdm(c_vec):
#for c in tqdm(range(1, n+1)):
#for c in tqdm(range(1, 8)):
    '''STEP1 : Randomly weight selects'''
    U = np.random.random([c, n])
    # Create a weight matrix with random pesos
    for i in range(len(U[0, :])):
        NormWeights = sum(U[:, i])
        U[:, i] = U[:, i]/NormWeights

    '''STEP2: Compute the centroids'''
    # Create a centroid matrix
    V = np.zeros([c, p])
    for iteration in range(T):
        for i in range(c):
            for j in range(p):
                V_sup = 0
                V_inf = 0
                for k in range(n):
                    V_sup = V_sup + (U[i, k]**m)*(df[k, j])
                    V_inf = V_inf + (U[i, k]**m)
                V[i, j] = V_sup / V_inf

        ''' STEP 3: Update the membership matrix # '''
        exponente = (2/(m-1))
        for i in range(c):
            for k in range(n):
                u_sumatorio = 0
                u_sup = LA.norm(X[k, :]-V[i, :])
                u_inf = 0
                for j in range(c):
                    u_inf = LA.norm(X[k, :]-V[j, :])
                    u_sumatorio= u_sumatorio+((u_sup/u_inf)**exponente)
                U[i, k] = (u_sumatorio**-1)


    '''Fuzzy clusters to Crisp clusters'''

    Crisp = np.zeros(U.shape, dtype=bool)
    for j in range(n):
        idx = np.argmax(U[:, j])
        Crisp[idx, j] = True

    #for i in range(c):
        #plt.scatter(X[Crisp[i, :], 0], X[Crisp[i, :], 1])
    #PLot the centroids and the clusters
    #plt.scatter(V[:, 0], V[:, 1], marker='*', edgecolors='k')
    #plt.show()

    P[0, c-1] = performanceFCM(c, X, V, U, m, n, p)

#c_vec = np.array(range(1, n+1))
plt.suptitle('Performance index for optimal cluster')
plt.plot(c_vec, P[0, :])
plt.xlabel("Number of clusters")
plt.ylabel("Performance")
plt.show()

index_min = np.argmin(P)
#print('The optimal number of clusters (from 1 to) is:')
IdealCLuster = c_vec[index_min]

print("The optimal number of clusters (from 1 to %d) is: %d" % (cmax,IdealCLuster))
#print(f"The optimal number of clusters (from 1 to {cmax}) is: {IdealCLuster}")