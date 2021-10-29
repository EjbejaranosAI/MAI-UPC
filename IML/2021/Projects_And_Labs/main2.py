
#Import the libraries to manage the project

import numpy as np
import pandas as pd
import sklearn
from matplotlib import pyplot as plt, gridspec
from scipy.io import arff
from sklearn.cluster import OPTICS, cluster_optics_dbscan
from sklearn.preprocessing import normalize, StandardScaler
#Read the dataset from a relative path
content = "datasets/datasets/adult.arff"
data = arff.loadarff(content) # With this we can work with datasets in format arff
#Create a new variable to store the names of the headings for each column
data_names = []
df = pd.DataFrame()
#We extract the columns
for i, row in enumerate(data[0]):
    if i == 0:
        for j in range(len(row)):
            data_names.append(row.dtype.descr[j][0].lower())
        df = pd.DataFrame(columns=data_names)

    df.loc[i] = pd.Series(np.asarray(row).tolist(), index=data_names)

print(df.columns)

df = df.drop(['class'], axis=1)
scalar = StandardScaler()
df_scaled = scalar.fit_transform(df)

df_normalized = normalize(df_scaled)

df_normalized = pd.DataFrame(df_normalized)

df_normalized.columns = df.columns
print(sklearn.neighbors.VALID_METRICS['kd_tree'])
optics_model = OPTICS(metric='minkowski', min_samples=5, algorithm='kd_tree')




optics_model.fit(df_normalized)

# Producing the labels according to the DBSCAN technique with eps = 0.5
labels1 = cluster_optics_dbscan(reachability=optics_model.reachability_,
                                core_distances=optics_model.core_distances_,
                                ordering=optics_model.ordering_, eps=0.5)

# Producing the labels according to the DBSCAN technique with eps = 2.0
labels2 = cluster_optics_dbscan(reachability=optics_model.reachability_,
                                core_distances=optics_model.core_distances_,
                                ordering=optics_model.ordering_, eps=2)

# the specified range
space = np.arange(len(df_normalized))

# Storing the reachability distance of each point
reachability = optics_model.reachability_[optics_model.ordering_]

# Storing the cluster labels of each point
labels = optics_model.labels_[optics_model.ordering_]

print(labels)

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


# Creating a numpy array with numbers at equal spaces till
