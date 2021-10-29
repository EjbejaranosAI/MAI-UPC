#Import the libraries to manage the project

import numpy as np
import pandas as pd
import sklearn
from matplotlib import pyplot as plt, gridspec
from scipy.io import arff
from sklearn.cluster import OPTICS, cluster_optics_dbscan
from sklearn.preprocessing import normalize, StandardScaler
#Read the dataset from a relative path
from arff_parser import arff_to_df_normalized

content = "./datasets/vehicle.arff"

df_normalized = arff_to_df_normalized(content)

df_normalized = pd.DataFrame(df_normalized)

print(sklearn.neighbors.VALID_METRICS['kd_tree'])
print(np.shape(df_normalized))


optics_model = OPTICS(min_samples = 10, xi = 0.05, min_cluster_size = 0.05, eps=0.02)

optics_model.fit(df_normalized)

# Producing the labels according to the DBSCAN technique with eps = 0.5
labels1 = cluster_optics_dbscan(reachability=optics_model.reachability_,
                                core_distances=optics_model.core_distances_,
                                ordering=optics_model.ordering_, eps=0.3)

# Producing the labels according to the DBSCAN technique with eps = 0.3
labels2 = cluster_optics_dbscan(reachability=optics_model.reachability_,
                                core_distances=optics_model.core_distances_,
                                ordering=optics_model.ordering_, eps=0.5)

# Creating a numpy array with numbers at equal spaces till
# the specified range
space = np.arange(len(df_normalized))

# Storing the reachability distance of each point
reachability = optics_model.reachability_[optics_model.ordering_]

# Storing the cluster labels of each point
labels = optics_model.labels_[optics_model.ordering_]

print(optics_model.labels_)

# Defining the framework of the visualization
plt.figure(figsize=(10, 7))
G = gridspec.GridSpec(2, 3)
ax1 = plt.subplot(G[0, :])
ax2 = plt.subplot(G[1, 0])
ax3 = plt.subplot(G[1, 1])
ax4 = plt.subplot(G[1, 2])

# Plotting the Reachability-Distance Plot
colors = ['c.', 'b.', 'r.', 'y.', 'g.']
for Class, colour in zip(range(0, 5), colors):
    Xk = space[labels == Class]
    Rk = reachability[labels == Class]
    ax1.plot(Xk, Rk, colour, alpha=0.3)
ax1.plot(space[labels == -1], reachability[labels == -1], 'k.', alpha=0.3)
ax1.plot(space, np.full_like(space, 2., dtype=float), 'k-', alpha=0.5)
ax1.plot(space, np.full_like(space, 0.5, dtype=float), 'k-.', alpha=0.5)
ax1.set_ylabel('Reachability Distance')
ax1.set_title('Reachability Plot')

# Plotting the OPTICS Clustering
colors = ['c.', 'b.', 'r.', 'y.', 'g.']
for Class, colour in zip(range(0, 5), colors):
    Xk = df_normalized[optics_model.labels_ == Class]
    ax2.plot(Xk.iloc[:, 0], Xk.iloc[:, 1], colour, alpha=0.3)

ax2.plot(df_normalized.iloc[optics_model.labels_ == -1, 0],
         df_normalized.iloc[optics_model.labels_ == -1, 1],
         'k+', alpha=0.1)
ax2.set_title('OPTICS Clustering')

print(df_normalized.iloc[optics_model.labels_ == -1, 0])
print(df_normalized.iloc[optics_model.labels_ == -1, 1])

# Plotting the DBSCAN Clustering with eps = 0.5
colors = ['c', 'b', 'r', 'y', 'g', 'greenyellow']
for Class, colour in zip(range(0, 6), colors):
    Xk = df_normalized[labels1 == Class]
    ax3.plot(Xk.iloc[:, 0], Xk.iloc[:, 1], colour, alpha=0.3, marker='.')

ax3.plot(df_normalized.iloc[labels1 == -1, 0],
         df_normalized.iloc[labels1 == -1, 1],
         'k+', alpha=0.1)
ax3.set_title('DBSCAN clustering with eps = 0.5')

# Plotting the DBSCAN Clustering with eps = 2.0
colors = ['c.', 'y.', 'm.', 'g.']
for Class, colour in zip(range(0, 4), colors):
    Xk = df_normalized.iloc[labels2 == Class]
    ax4.plot(Xk.iloc[:, 0], Xk.iloc[:, 1], colour, alpha=0.3)

ax4.plot(df_normalized.iloc[labels2 == -1, 0],
         df_normalized.iloc[labels2 == -1, 1],
         'k+', alpha=0.1)
ax4.set_title('DBSCAN Clustering with eps = 2.0')

plt.tight_layout()
plt.show()


