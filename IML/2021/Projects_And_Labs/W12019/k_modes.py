import numpy as np
import pandas as pd
from itertools import islice
from collections import defaultdict


class KModes:

    def __init__(self, data):
        # print("Init....")
        self.some_config = False
        self.data = data

    def count_dissimilairty(self, a, b):
        """Simple matching dissimilarity function"""
        return np.sum(a != b)

    # Randomly chosen
    def init_huang(self, df, n_clusters):
        """Initialize centroids according to method by Huang [1997]."""
        n_attrs = df.shape[1]
        centroids = np.empty((n_clusters, n_attrs), dtype='object')

        # select randomly non duplicated centroids
        for attr in range(n_attrs):
            freq = defaultdict(int)
            for curattr in df.iloc[:, attr]:
                freq[curattr] += 1

            choices = [chc for chc, wght in freq.items() for _ in range(wght)]
            choices = sorted(choices)
            centroids[:, attr] = np.random.choice(choices, n_clusters)
        return centroids

    def calculate_distance(self, centroids, n_points, df, n_clusters):
        # difference[row][cluster] = Disimilarity(data[row], centroids[cluster])
        distances = np.zeros((n_points, n_clusters), dtype='int8')
        for index, row in islice(df.iterrows(), 0, None):
            for idx, mode in enumerate(centroids):
                # Calculate distance betwwen row.values, mode)
                distances[index, idx] = self.count_dissimilairty(row.values, mode)
        return distances

    def assign_points_to_clusters(self, distances, df, n_points):
        clusters_assignments = np.empty(n_points, dtype='int8')
        clusters_assignments.fill(np.nan)

        # All the clusters should have at least one item
        for idx, row in enumerate(distances):
            temp = np.where(row == min(row))[0]
            if len(temp) == 1:
                clusters_assignments[idx] = temp[0]
            else:
                for cnt, t in enumerate(temp):
                    if np.isnan(np.where(clusters_assignments == t)[0]).all():
                        clusters_assignments[idx] = t
                        break
                    # Impove it in order to assign the point to the cluster with the less points
                    if cnt == len(temp):
                        clusters_assignments[idx] = t

        return clusters_assignments

    def recalculate_centroids(self, df, clusters_assignments, n_clusters, n_attrs):
        centroids = np.empty((n_clusters, n_attrs), dtype='object')
        for i in range(n_clusters):
            cls_itm = np.where(clusters_assignments == i)[0]
            temp = df.iloc[cls_itm]
            centroids[i] = temp.mode(dropna=True).iloc[0]
        return centroids

    def __train_model(self, centroids, n_points, df, n_clusters, n_attrs):
        distances = self.calculate_distance(centroids, n_points, df, n_clusters)
        clusters_assignments = self.assign_points_to_clusters(distances, df, n_points)
        centroids = self.recalculate_centroids(df, clusters_assignments, n_clusters, n_attrs)
        return centroids, clusters_assignments

    def model_name(self):
        return "k-Modes"

    # data n_points * n_attrs
    # centroids: n_clusters * n_attrs
    # clusters: n_points* n_clusters
    def clusterize(self, n_clusters):
        print(" * Clustering data with {}...".format(self.model_name()))
        df = pd.DataFrame(self.data)
        n_points, n_attrs = df.shape

        # Randomly selected centroids (Careful not be duplicated)
        # Define the centroids n_clusters * n_attrs
        centroids = self.init_huang(df, n_clusters)

        new_centroids, clusters_assignments = self.__train_model(centroids, n_points, df, n_clusters, n_attrs)
        while np.where(centroids != new_centroids)[0].any():
            temp = new_centroids
            new_centroids, clusters_assignments = self.__train_model(new_centroids, n_points, df, n_clusters, n_attrs)
            centroids = temp
        return clusters_assignments, new_centroids
