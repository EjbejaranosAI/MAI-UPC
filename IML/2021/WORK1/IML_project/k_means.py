# Import the libraries to manage the project
from operator import itemgetter

import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm

from utils.arff_parser import arff_to_df_normalized
from utils.validator import validation, plot_accuracy


CONTENT = 'datasets/cmc.arff'

class KMeans:
    def __init__(self, k=2, tol=0.00001, max_iter=300):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def fit(self, data):
        data = np.array(data)
        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = data[i]

        for i in tqdm(range(self.max_iter)):

            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for features in data:
                distances = [np.linalg.norm(features - self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(features)

            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)

            optimized = True

            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid - original_centroid) / original_centroid * 100.0) > self.tol:
                    optimized = False
            if optimized:
                break

    def elbow(self, data):
        SSE_centroids = []
        SSE_average = []
        for k in range(1, 10):
            model = KMeans(k)
            model.fit(data)
            for i in range(0, model.k):
                SSE = np.sum((model.classifications[i] - model.centroids[i]) ** 2)
                SSE_centroids.append(SSE)
            SSE_average.append(np.average(SSE_centroids))

        print(SSE_average)

        plt.plot(range(1, 10), SSE_average, marker='.')
        plt.xlabel('Number of Clusters')
        plt.ylabel('Length of Data')
        plt.title('K-means Elbow method')
        plt.show()

    def predict(self, data):
        classifications = []
        data = np.array(data)
        for data_point in data:
            distances = [np.linalg.norm(data_point - self.centroids[centroid]) for centroid in self.centroids]
            cluster_index = distances.index(min(distances))
            classifications.append(cluster_index)

        return classifications


data, data_num_idxs, data_cat_idxs, names, classes = arff_to_df_normalized(CONTENT)

num_data = data[list(itemgetter(*data_num_idxs)(names))].to_numpy(dtype='float32')
model = KMeans(k=5, max_iter=1000)

model.elbow(num_data)

model.fit(num_data)

classified_data = model.predict(num_data)

accuracy, accuracy_ari = validation(classes, classified_data)

print(f"accuracy: {accuracy}")
print(f"accuracy_ari: {accuracy_ari}")

plot_accuracy(accuracy, list(classes.unique()))

print(classified_data)