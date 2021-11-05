from utils.arff_parser import arff_to_df_normalized

# Import the libraries to manage the project

import numpy as np
from matplotlib import pyplot as plt
from numpy import linalg as LA

from utils.validator import validation, plot_accuracy

content = "datasets/vehicle.arff"

df_normalized, data_num_names, data_cat_names, data_names, class_names = arff_to_df_normalized(content)

print(df_normalized.head())
'''Imputs'''
# Data
X = df = df_normalized.to_numpy()

# c clusters
c = (len(class_names.unique()))
# Maximun number of iterations
T = (100)
# Fuzziness degree
m = 2

print('Our matrix')
print(df)
# n number of instances
n = (len(df[:, 0]))
# p number of fetures
p = (len(df[0, :]))

#
'''STEP1 : Randomly weight selects'''
U = np.random.random([c, n])
# Create a weight matrix with random pesos
for i in range(len(U[0, :])):
    sarita = sum(U[:, i])
    U[:, i] = U[:, i] / sarita
print('Our universe U with the weights')
print(U)

'''STEP2: Compute the centroids'''
# Create a centroid matrix
V = np.zeros([c, p])
print(V.shape)

for iteration in range(T):
    print('Parce vamos en la: ', iteration)

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

print('Universe matrix- Weights')
print(U)
print('Crisp matrix')
print(Crisp)
print('Centroids matrix: :)')
print(V)

plt.scatter(X[:, 0], X[:, 1])
plt.scatter(V[:, 0], V[:, 1])
plt.show()

for i in range(c):
    plt.scatter(X[Crisp[i, :], 0], X[Crisp[i, :], 1])
# Centroides
plt.scatter(V[:, 0], V[:, 1])
plt.show()

labels = np.argmax(np.transpose(Crisp, (1, 0)), axis=1)

accuracy, accuracy_ari = validation(class_names, labels)
plot_accuracy(accuracy, class_names)
