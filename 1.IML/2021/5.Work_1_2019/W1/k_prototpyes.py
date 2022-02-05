import numpy as np
import pandas as pd
from itertools import islice
from collections import defaultdict, Counter
import math

class KPrototypes:
    MIN_VALUE_NUMERICAL = 0.0
    MAX_VALUE_NUMERICAL = 1.0
    MAX_TRIALS = 10

    def __init__(self, data):
        # print("Init....")
        self.some_config = False
        self.data = data
        self.numerical_feat = self.__get_orig_numerical_features()
        self.nominal_feat = self.__get_orig_nominal_features()
        self.n_points = self.data.shape[0]
        self.n_num_attrs = self.numerical_feat.shape[1]
        self.n_cat_attrs = self.nominal_feat.shape[1]

    def __get_orig_numerical_features(self):
        return self.data.select_dtypes(exclude=[np.object]).copy()

    def __get_orig_nominal_features(self):
        return self.data.select_dtypes([np.object])

    def __euclidean_distance(self, x, y):
        distance = 0.0
        for i in range(len(x)):
            distance += (x.iloc[i] - y[i]) ** 2
        return math.sqrt(distance)

    def init_random(self, n_clusters):
        cat_centroids = np.empty((n_clusters, self.n_cat_attrs), dtype='object')
        if(self.n_cat_attrs > 0):
            # select randomly non duplicated centroids
            for attr in range(self.n_cat_attrs):
                freq = defaultdict(int)
                for curattr in self.nominal_feat.iloc[:, attr]:
                    freq[curattr] += 1
                choices = [chc for chc, wght in freq.items() for _ in range(wght)]
                choices = sorted(choices)
                cat_centroids[:, attr] = np.random.choice(choices, n_clusters)

        # Nominal attributes
        num_centroids = np.random.rand(n_clusters, self.n_num_attrs)
        amplitude = KPrototypes.MAX_VALUE_NUMERICAL - KPrototypes.MIN_VALUE_NUMERICAL
        num_centroids = num_centroids * amplitude - KPrototypes.MIN_VALUE_NUMERICAL

        centroids = num_centroids
        centroids = np.append(centroids, cat_centroids, axis=1)
        return centroids

    def count_nominal_dissimilairty(self, a, b):
        return np.sum(a != b)

    def calculate_distance(self, n_clusters, centroids):
        # distance = d_n() +g*d_c()
        distances = np.zeros((self.n_points, n_clusters), dtype='float64')
        for i in range(self.n_points):
            for idx, mode in enumerate(centroids):
                distance_num = 0
                distances_nom = 0
                if self.n_num_attrs > 0:
                    distance_num = self.__euclidean_distance(self.numerical_feat.iloc[i], mode[:self.n_num_attrs])
                if self.n_cat_attrs > 0:
                    distances_nom = self.count_nominal_dissimilairty(self.nominal_feat.iloc[i], mode[self.n_num_attrs:])
                distances[i, idx] = distance_num + 0.5 * distances_nom
        return distances

    def assign_points_to_clusters(self, distances):
        clusters_assignments = np.empty(self.n_points, dtype='int8')
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

    def recalculate_centroids(self, n_clusters, clusters_assignments):

        num_centroids = np.empty((n_clusters, self.n_num_attrs), dtype='object')
        if self.n_num_attrs > 0:
            for i in range(n_clusters):
                num_itm = np.where(clusters_assignments == i)[0]
                for attr in range(self.n_num_attrs):
                    num_centroids[i, attr] = self.numerical_feat.iloc[num_itm, attr].mean()

        cat_centroids = np.empty((n_clusters, self.n_cat_attrs), dtype='object')
        if self.n_cat_attrs > 0:
            for i in range(n_clusters):
                num_itm = np.where(clusters_assignments[self.n_num_attrs:] == i)[0]
                temp = self.nominal_feat.iloc[num_itm]
                cat_centroids[i] = temp.mode(dropna=True).iloc[0]

        centroids = np.append(num_centroids, cat_centroids, axis=1)
        return centroids

    def __train_model(self, n_clusters, centroids):
        distances = self.calculate_distance(n_clusters, centroids)
        clusters_assignments = self.assign_points_to_clusters(distances)
        centroids = self.recalculate_centroids(n_clusters, clusters_assignments)
        return centroids, clusters_assignments

    def __calculate_num_sse(self, cluster_assignments, centroids):
        sse = 0.0
        for i in range(self.n_points):
            centroid = centroids[cluster_assignments[i]][:self.n_num_attrs]
            sse += self.__euclidean_distance(self.numerical_feat.iloc[i], centroid)
        return sse

    def model_name(self):
        return "k-Prot"

    def clusterize(self, n_clusters):
        print(" * Clustering data with {}...".format(self.model_name()))
        lowest_total_sse = math.inf
        # Randomly selected centroids (Careful not be duplicated)
        # Define the centroids n_clusters * n_attrs
        centroids = self.init_random(n_clusters)

        new_centroids, clusters_assignments = self.__train_model(n_clusters, centroids)

        sse = self.__calculate_num_sse(clusters_assignments, new_centroids)

        while np.where(centroids[self.n_num_attrs:] != new_centroids[self.n_num_attrs:])[0].any() or sse > 3:
            temp = new_centroids
            new_centroids, clusters_assignments = self.__train_model(n_clusters, new_centroids)
            centroids = temp
            sse = self.__calculate_num_sse(clusters_assignments, new_centroids)
            self.MAX_TRIALS -= 1
            if self.MAX_TRIALS == 0:
                break

        return np.array(clusters_assignments), new_centroids
