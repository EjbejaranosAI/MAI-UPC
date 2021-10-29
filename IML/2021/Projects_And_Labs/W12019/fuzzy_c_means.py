import numpy as np
import matplotlib.pyplot as plt


class FuzzyCMeans:
    """
    Implementation of the Fuzzy c-Means clustering algorithm

    Using the naming convention of James C. Bezdek et al. (1984)
    "FCM_ The Fuzzy c-Means Clustering Algorithm."

    Attributes
    ----------
    data : matrix of mixed types (same type column-wise)
        Input dataset
    m : int
        Weighting exponent (aka Fuzziness degree)
    epsilon : float
        Termination threshold
    t : int
        Max numbers of iterations

    Methods
    -------
    clustering(c)
        Returns a N-length array with the cluster assigned for each
    fuzzy_clustering(c)
        Returns a c-partition of the input dataset
    """

    def __init__(self, data, m=1.4, epsilon=0.01, t=100, v=True):
        self.df_dataset = data
        self.input_dataset = data.to_numpy()
        self.number_of_rows = len(self.input_dataset)
        self.number_of_features = len(self.input_dataset[0])
        self.m = m
        self.epsilon = epsilon
        self.max_iterations = t
        self.term_meas = []
        self.verbose = v
        self.iteration_ii = []

    def model_name(self):
        title = "FCM (m={})"
        return title.format(self.m)

    def clusterize(self, c):
        print(" * Clustering data with {}...".format(self.model_name()))
        c_partition, centroids = self.__fuzzy_clustering(c)
        crisp_cluster_assignments = self.__defuzzy(c_partition)
        return crisp_cluster_assignments, centroids

    def experiment(self, c, fuzzy_coeff):
        self.m = fuzzy_coeff
        print(" * Clustering data with {}...".format(self.model_name()))
        crisp_clusterings = []
        resulting_centroids = []
        metrics = {
            'ii': [],
            'iter': []
        }
        for m in fuzzy_coeff:
            self.m = m
            c_partition, centroids = self.__fuzzy_clustering(c)
            crisp_clusterings.append(self.__defuzzy(c_partition))
            resulting_centroids.append(centroids)
            metrics['ii'].append(self.__partition_coefficient(c_partition))
            metrics['iter'].append(self.iteration_ii.copy())
        return crisp_clusterings, resulting_centroids, metrics

    def __fuzzy_clustering(self, c):
        c_partition = self.__init_c_part(c)
        cluster_centers = []
        sses = []
        self.iteration_ii = []
        for i in range(self.max_iterations):
            cluster_centers = self.__update_centers(c, c_partition)
            new_c_partition = self.__update_c_part(c, cluster_centers)
            if self.__should_terminate(c_partition, new_c_partition):
                break
            c_partition = new_c_partition
            sses.append(self.__aux_sse(c_partition, cluster_centers))
            self.iteration_ii.append(self.__partition_coefficient(c_partition))
        self.__print_internal_index(self.__partition_coefficient(c_partition))
        return c_partition, cluster_centers

    def __init_c_part(self, c):
        c_partition = np.random.rand(c, self.number_of_rows)
        for k in range(self.number_of_rows):
            # Random initialization (observing c-partition conditions)
            summation = np.sum(c_partition[:, k])
            c_partition[:, k] = np.divide(c_partition[:, k], summation)
        return c_partition

    def __update_centers(self, c, c_partition):
        cluster_centers = np.empty([c, self.number_of_features])
        for i in range(c):
            fuzzy_mem_func_m = np.float_power(c_partition[i], self.m)
            sux = np.zeros(len(self.input_dataset[0]))
            for k in range(self.number_of_rows):
                sux += self.input_dataset[k] * fuzzy_mem_func_m[k]
            cluster_centers[i] = np.divide(sux, np.sum(fuzzy_mem_func_m))
        return cluster_centers

    def __update_c_part(self, c, cluster_centers):
        c_partition = np.empty([c, self.number_of_rows])
        exponent = 2 / (self.m - 1)
        for i in range(c):
            for k in range(self.number_of_rows):
                v_i = cluster_centers[i]
                x_k = self.input_dataset[k]
                sq_dist_i = np.sqrt(np.linalg.norm(np.add(x_k, v_i * -1))) ** 2
                result = 0
                for j in range(c):
                    v_j = cluster_centers[j]
                    sq_dist_j = np.sqrt(np.linalg.norm(np.add(x_k, v_j * -1))) ** 2
                    result += np.divide(sq_dist_i, sq_dist_j) ** exponent
                c_partition[i][k] = np.divide(1.0, result)
        return c_partition

    def __should_terminate(self, old_c_partition, new_c_partition):
        difference = np.add(old_c_partition, new_c_partition * -1)
        termination_test = np.linalg.norm(difference)
        self.term_meas.append(termination_test)
        return termination_test <= self.epsilon

    def __defuzzy(self, c_partition):
        return c_partition.argmax(axis=0)

    def __plot_measurement(self, measurement_value, measurement_name):
        plt.plot(measurement_value)
        plt.ylabel(measurement_name)
        plt.xlabel('Iteration')
        plt.title('Fuzzy Measurements')
        plt.show()

    def __print_internal_index(self, internal_index):
        if self.verbose:
            print("   - Partition Coefficient: {0:.3f}".format(internal_index))

    def __partition_coefficient(self, c_partition):
        c = len(c_partition)
        result = 0
        for i in range(c):
            for k in range(self.number_of_rows):
                result += c_partition[i, k] ** 2
        result = result / self.number_of_rows
        return result

    def __aux_sse(self, c_partition, centroids):
        sse = 0
        c = len(c_partition)
        for i in range(c):
            for k in range(self.number_of_rows):
                v_i = centroids[i]
                x_k = self.input_dataset[k]
                sq_dist = np.linalg.norm(np.add(x_k, v_i * -1))
                sse += (c_partition[i, k] ** self.m) * sq_dist
        return sse
