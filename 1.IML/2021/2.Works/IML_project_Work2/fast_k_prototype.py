from operator import itemgetter

import numpy as np
import pandas as pd
import copy
import tqdm

from utils.arff_parser import arff_to_df_normalized
from utils.validator import validation, plot_accuracy

CONTENT = 'datasets/adult.arff'


class FKPT:
    def __init__(self, k, categorical_weight, num_iter, tol):
        self.k = k
        self.num_iter = num_iter
        self.categorical_weight = categorical_weight
        self.tol = tol
        self.cluster_centers = {}
        self.classifications = {key: [] for key in range(self.k)}

    def _dist_compute_n(self, data_point, idx_n):
        dist_n = []

        # transfer centers into list of lists
        cluster_centers = [cluster[1].to_list() for cluster in list(self.cluster_centers.items())]

        # extract numeric values from centers and transfer it to numpy
        cluster_centers = np.array([list(itemgetter(*idx_n)(cluster)) for cluster in cluster_centers], dtype='float32')

        # calculate distances
        dist_n = [np.linalg.norm(data_point - cluster) for cluster in cluster_centers]

        # find first two smallest number
        first_min, second_min = np.partition(dist_n, 1)[0:2]

        return dist_n, first_min, second_min

    def _dist_compute_c(self, data_point, idx_c):
        dist_c = []

        # transfer centers into list of lists
        cluster_centers = [cluster[1].to_list() for cluster in list(self.cluster_centers.items())]

        # extract numeric values from centers and transfer it to numpy
        cluster_centers = np.array([list(itemgetter(*idx_c)(cluster)) for cluster in cluster_centers], dtype='str')

        dist_c = [(cluster == data_point).sum() * self.categorical_weight for cluster in cluster_centers]

        return dist_c

    def _update_cluster_centers(self, idx_n, idx_c, columns):
        for cluster_index, cluster_data in self.classifications.items():
            cluster_data_df = pd.DataFrame(data=cluster_data, columns=columns)

            # divide the data as a numerical and categorical
            num_data = cluster_data_df[list(itemgetter(*idx_n)(columns))].to_numpy(dtype='float32')
            cat_data = cluster_data_df[list(itemgetter(*idx_c)(columns))]

            # calculate the mean of each column
            num_mean = num_data.mean(axis=0)

            # find the most frequent categorical data
            cat_frequent = list(cat_data.value_counts().idxmax())

            # update the cluster centers
            self.cluster_centers[cluster_index][idx_n] = num_mean
            self.cluster_centers[cluster_index][idx_c] = cat_frequent

    def _diff_between_cluster_centers(self, prev_clusters, idx_n, idx_c):
        diff = 0

        for cluster in range(len(prev_clusters)):
            data_num_prev = np.array(list(itemgetter(*idx_n)(list(prev_clusters[cluster]))))
            data_cat_prev = np.array(list(itemgetter(*idx_c)(list(prev_clusters[cluster]))))
            data_num_current = np.array(list(itemgetter(*idx_n)(list(self.cluster_centers[cluster]))))
            data_cat_current = np.array(list(itemgetter(*idx_c)(list(self.cluster_centers[cluster]))))
            num_diff = np.sum(abs(np.subtract(data_num_prev, data_num_current)))
            cat_diff = self.categorical_weight * np.sum(data_cat_prev == data_cat_current)
            diff += num_diff + cat_diff
        return diff

    def fit(self, data, idx_n, idx_c, data_names):
        for i in range(self.k):
            self.cluster_centers[i] = data.loc[i]

        # extract only numeric values and transfer it to numpy
        num_data = data[list(itemgetter(*idx_n)(data_names))].to_numpy(dtype='float32')
        cat_data = data[list(itemgetter(*idx_c)(data_names))].to_numpy(dtype='str')

        # first stop condition
        for counter in tqdm.tqdm(range(self.num_iter)):
            prev_cluster_centers = copy.deepcopy(self.cluster_centers)

            self.classifications = {key: [] for key in range(self.k)}
            for inx, data_point in data.iterrows():
                dist_n, first_min, second_min = self._dist_compute_n(num_data[inx], idx_n)

                # fast k prototype algorithm
                if second_min - first_min < len(idx_c) * self.categorical_weight:
                    dist_c = self._dist_compute_c(cat_data[inx], idx_c)
                    dist = np.add(dist_n, dist_c)
                else:
                    dist = dist_n

                self.classifications[np.argmin(dist)].append(list(data_point))
            self._update_cluster_centers(idx_n, idx_c, data_names)

            # second stop condition
            if counter > 0 and self._diff_between_cluster_centers(prev_cluster_centers, idx_n, idx_c) <= self.tol:
                break

    def predict(self, data, idx_n, idx_c, data_names):
        classifications = []

        num_data = data[list(itemgetter(*idx_n)(data_names))].to_numpy(dtype='float32')
        cat_data = data[list(itemgetter(*idx_c)(data_names))].to_numpy(dtype='str')

        for inx, data_point in data.iterrows():
            dist_n, first_min, second_min = self._dist_compute_n(num_data[inx], idx_n)

            if second_min - first_min < len(idx_c) * self.categorical_weight:
                dist_c = self._dist_compute_c(cat_data[inx], idx_c)
                dist = np.add(dist_n, dist_c)
            else:
                dist = dist_n

            classifications.append(np.argmin(dist))
        return classifications


data, data_num_idxs, data_cat_idxs, names, classes = arff_to_df_normalized(CONTENT)

fktp = FKPT(k=10, categorical_weight=0.2, num_iter=100, tol=0.01)
fktp.fit(data, data_num_idxs, data_cat_idxs, names)
classified_data = fktp.predict(data, data_num_idxs, data_cat_idxs, names)

accuracy, accuracy_ari = validation(classes, classified_data)

print(f"accuracy: {accuracy}")
print(f"accuracy_ari: {accuracy_ari}")

plot_accuracy(accuracy, list(classes.unique()))

print(classified_data)
