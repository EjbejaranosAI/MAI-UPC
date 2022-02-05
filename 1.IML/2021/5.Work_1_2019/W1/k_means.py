from collections import Counter
from random import uniform
import numpy as np
import math

class KMeansClustering:

    def __init__(self, data, min_value=0.0, max_value=1.0):
        # check the input data first
        self.__verify_k_means_input_data(data)

        self.data = data
        self.min_value = min_value
        self.max_value = max_value

        self.number_of_features = len(data[0])
        self.number_of_rows = len(data)

        self.max_iterations = 20

    # This method implements the Bisecting K-means clustering algorithm
    #
    # input parameters:
    # k - number of clusters
    # data - array [N][D], where N is the number of data elements and D is number of features
    # min_value (default 0.0) - minimum value after normalization
    # max_value (default 1.0) - maximum value after normalization
    #
    # constraints:
    # all feature values must be numerical and normalized
    #
    # output:
    # array of cluster numbers corresponding to each row of the input data
    # the output has exactly the same number of columns as the number of input rows

    def clusterize(self, k):
        print(" * Clustering data with {}...".format(self.model_name()))
        self.__verify_k(k)
        return self.__bisecting_k_means(k)

    def k_means(self, k, trials=5, centroids=[]):
        self.__verify_k(k)
        final_cluster_assignments = []
        lowest_total_sse = float('inf')
        best_trial = 0
        # there should be only one trial if centroids are not going to be chosen randomly
        if len(centroids) != 0:
            trials = 1
        computed_centroids = []
        for trial in range(trials):
            # centroids are chosen randomly when there is no argument applied
            computed_centroids = centroids
            if len(computed_centroids) == 0:
                computed_centroids = self.__initialize_centroids_randomly(k)

            cluster_assignments = []
            # assign to clusters and recalculate centroids
            for i in range(1, self.max_iterations + 1):
                if self.__update_cluster_assignments(computed_centroids, cluster_assignments):
                    computed_centroids = self.__calculate_centroids(k, cluster_assignments)
                else:
                    #print("K-means: breaking after {} iterations".format(i))
                    break

            sse = self.__calculate_total_sse(cluster_assignments, computed_centroids)
            if sse < lowest_total_sse:
                lowest_total_sse = sse
                final_cluster_assignments = cluster_assignments
                best_trial = trial

        #print("K-means: found the best {} clusters in the trial {} with the total SSE of {}".format(k, best_trial, lowest_total_sse))

        return final_cluster_assignments, np.array(computed_centroids)

    def model_name(self):
        return "k-Means"

    def __calculate_total_sse(self, cluster_assignments, centroids):
        sse = 0.0
        for i in range(len(cluster_assignments)):
            sse += self.__euclidean_distance(self.data[i], centroids[cluster_assignments[i]]) ** 2
        return sse

    def __calculate_cluster_sse(self, cluster, cluster_assignments, centroid):
        sse = 0.0
        for i in range(len(cluster_assignments)):
            if cluster_assignments[i] == cluster:
                sse += self.__euclidean_distance(self.data[i], centroid) ** 2
        return sse

    def __bisecting_k_means(self, k):
        # executing basic k-means to bisect the first cluster
        cluster_assignments, _ = self.k_means(2)

        # iteratively bisecting selected cluster
        number_of_clusters = len(Counter(cluster_assignments).most_common())
        while number_of_clusters < k:
            #print("bisecting {} to obtain {}".format(number_of_clusters, number_of_clusters + 1))
            cluster_assignments = self.__bisect(cluster_assignments)
            number_of_clusters = len(Counter(cluster_assignments).most_common())

        # calculate centroids of the obtained clusters
        centroids = self.__calculate_centroids(k, cluster_assignments)

        # run normal k-means with initialized centroids
        return self.k_means(k, centroids=centroids)

    def __bisect(self, cluster_assignments):
        cluster = self.__find_cluster_to_bisect(cluster_assignments)
        counter = Counter(cluster_assignments)
        number_of_data_points = counter[cluster]
        data_points_in_the_selected_cluster = np.empty((number_of_data_points, self.number_of_features))
        j = 0
        for i in range(len(cluster_assignments)):
            if cluster_assignments[i] == cluster:
                data_points_in_the_selected_cluster[j] = self.data[i]
                j += 1
        split_cluster_assignments, _ = KMeansClustering(
            data_points_in_the_selected_cluster,
            self.min_value,
            self.max_value
        ).k_means(2)

        # renumbering clusters
        counter_split = Counter(split_cluster_assignments)
        created_cluster = len(counter.most_common())
        j = 0
        for i in range(len(cluster_assignments)):
            # split_cluster_assignments[j] can be 0 or 1
            if cluster_assignments[i] == cluster:
                # let 0 be the old cluster number and assign created_cluster to the second half
                if split_cluster_assignments[j] == 1:
                    cluster_assignments[i] = created_cluster
                j += 1

        return cluster_assignments

    def __find_cluster_to_bisect(self, cluster_assignments):
        counter = Counter(cluster_assignments)
        clusters = []
        max_size = 0.0
        max_cluster_ess = 0.0
        centroids = self.__calculate_centroids(len(counter.most_common()), cluster_assignments)
        for cluster in range(len(counter.most_common())):
            size = counter[cluster]
            if size > max_size:
                max_size = size
            ess = self.__calculate_cluster_sse(cluster, cluster_assignments, centroids[cluster])
            if ess > max_cluster_ess:
                max_cluster_ess = ess
            clusters.append((size, ess))

        cluster_to_bisect = None
        highest = 0.0
        weight_size = 0.2
        weight_ess = 0.8
        for cluster in range(len(clusters)):
            size_normalized = clusters[cluster][0] / max_size
            ess_normalized = 0
            if max_cluster_ess > 0:
                ess_normalized = clusters[cluster][1] / max_cluster_ess
            f = size_normalized * weight_size + ess_normalized * weight_ess
            if f > highest:
                highest = f
                cluster_to_bisect = cluster
        return cluster_to_bisect

    def __initialize_centroids_randomly(self, k):
        centroids = np.random.rand(k, self.number_of_features)
        amplitude = self.max_value - self.min_value
        centroids = centroids * amplitude - self.min_value
        return centroids

    # This method verifies the input data for the K-means clustering algorithm
    def __verify_k_means_input_data(self, data):
        if len(data) == 0:
            raise AttributeError("data array is empty")

    def __verify_k(self, k):
        if k < 2:
            raise AttributeError("k must be greater than 1")

    def __euclidean_distance(self, x, y):
        distance = 0.0
        for i in range(len(x)):
            distance += (x[i] - y[i]) ** 2
        return math.sqrt(distance)

    def __update_cluster_assignments(self, centroids, cluster_assignments):
        updated = False
        for i in range(self.number_of_rows):
            # prepare the vector of a data point with all its features
            x = self.data[i]
            # variables for the minimum distance and the output cluster
            min_distance = float('inf')
            cluster = None
            # find minimum distance for the object
            for c in range(len(centroids)):
                distance = self.__euclidean_distance(x, centroids[c])
                if distance < min_distance:
                    cluster = c
                    min_distance = distance

            # add new item to the vector
            if len(cluster_assignments) <= i:
                cluster_assignments.append(cluster)
                updated = True
            # update the existing cluster assignment
            elif cluster_assignments[i] != cluster:
                cluster_assignments[i] = cluster
                updated = True

        return updated

    def __calculate_centroids(self, k, cluster_assignments):
        centroids = np.empty((k, self.number_of_features))

        for c in range(len(centroids)):
            centroids[c] = self.__calculate_centroid(k, cluster_assignments, c)

        return centroids

    def __calculate_centroid(self, k, cluster_assignments, cluster):
        counter = Counter(cluster_assignments)
        # sum of the vectors initialized with zeros
        vector_sum = np.zeros(self.number_of_features)
        # calculating the sum of current distance values
        for data_row_number in range(self.number_of_rows):
            if cluster_assignments[data_row_number] == cluster:
                x = self.data[data_row_number]
                # updating the sum
                vector_sum += x

        # if counter[c] is zero, do not change the centroid
        if counter[cluster] > 0:
            return vector_sum / float(counter[cluster])
        else:
            return vector_sum
