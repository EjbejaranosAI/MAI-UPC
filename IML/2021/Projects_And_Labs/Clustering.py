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

# Read the dataset from a relative path
content = "datasets/datasets/waveform.arff"
data = arff.loadarff(content)  # With this we can work with datasets in format arff
# Create a new variable to store the names of the headings for each column
data_names = []
df = pd.DataFrame()
# We extract the columns
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
optics_model = OPTICS(metric='euclidean', min_samples=5, algorithm='kd_tree')

K_Means = KMeans


class K_Means:
    def _init_(self, k=2, tol=0.001, max_iter=300):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def fit(self, data):

        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = data[i]

        for i in range(self.max_iter):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for featureset in data:
                distances = [np.linalg.norm(featureset - self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)

            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)

            optimized = True

            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid - original_centroid) / original_centroid * 100.0) > self.tol:
                    print(np.sum((current_centroid - original_centroid) / original_centroid * 100.0))
                    optimized = False

            if optimized:
                break

    def predict(self, data):
        distances = [np.linalg.norm(data - self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification

    model = K_Means()
    model.fit(X)

    for centroid in model.centroids:
        plt.scatter(model.centroids[centroid][0], model.centroids[centroid][1],
                    marker="o", color="k", s=150, linewidths=5)

    for classification in model.classifications:
        color = colors[classification]
        for featureset in model.classifications[classification]:
            plt.scatter(featureset[0], featureset[1], marker="x", color=color, s=150, linewidths=5)

    plt.show()
