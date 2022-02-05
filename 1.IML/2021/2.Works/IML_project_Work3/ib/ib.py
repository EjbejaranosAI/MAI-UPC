import math
import random

import numpy as np
import time
from scipy.spatial import distance

from ib.distance_metrics import HVDM


class IB:
    def __init__(self, algorithm):
        self.algorithm_mapping = {'ib1': self._ib1, 'ib2': self._ib2, 'ib3': self._ib3}  # algorithm mappings

        self.algorithm = self.algorithm_mapping[algorithm]

        self.cd = []  # concept description
        self.cd_classes = []  # concept description labels
        self.correct_num = 0  # correctly classified data
        self.dataset_size = 0  # dataset dataset_size
        self.total_size = 0
        self.time = 0  # execution time

        # those are for ib3
        self.accuracies = {}
        self.frequencies = {}

    def fit_and_predict(self, dataset, class_labels, k=1, distance_metric=None, voting_algorithm=None):
        self.correct_num = 0
        self.dataset_size = len(dataset)
        self.total_size += len(dataset)
        self.cd.append(dataset[0])  # append first data in cd because at the start it is empty
        self.cd_classes.append(class_labels[0])  # append first label in the cd because at the start it is empty

        # for ib3 only
        # init first instance of cds accuracy metric
        self.accuracies[str(dataset[0])] = {'correct': 0, 'incorrect': 0}
        # increase the number of frequency for first instance in CD
        self.frequencies[class_labels[0]] = 1

        start_time = time.perf_counter()  # define starting time

        self.algorithm(dataset, class_labels, k, distance_metric, voting_algorithm)  # fit and predict data

        end_time = time.perf_counter()  # define ending time
        self.time = end_time - start_time  # calculate the overall time

    def _ib1(self, dataset, class_labels, k=1, distance_metric=None, voting_algorithm=None):

        # zip data and labels and iterate over them
        for index, (data_point, label) in enumerate(zip(dataset[1:], class_labels[1:])):

            distance_matrix_sorted, min_indices = self._find_k_similar(data_point, self.cd, k, distance_metric)
            vote_label = self._vote(min_indices, distance_matrix_sorted, self.cd_classes, voting_algorithm)

            # if it is correctly classified increase the number
            if label == vote_label:
                self.correct_num += 1

            # because we already have first data point in cd we are not adding it any more

            self.cd.append(data_point)
            self.cd_classes.append(label)

    def _ib2(self, dataset, class_labels, k=1, distance_metric=None, voting_algorithm=None):
        # zip data and labels and iterate over them
        for index, (data_point, label) in enumerate(zip(dataset[1:], class_labels[1:])):

            # find the index of most similar one
            distance_matrix_sorted, min_indices = self._find_k_similar(data_point, self.cd, k, distance_metric)
            vote_label = self._vote(min_indices, distance_matrix_sorted, self.cd_classes, voting_algorithm)

            # if it is correctly classified increase the number
            if label == vote_label:
                self.correct_num += 1
            # if it is incorrectly classified add in the cd
            else:
                self.cd.append(data_point)
                self.cd_classes.append(label)

    def _ib3(self, dataset, class_labels, k=1, distance_metric=None, voting_algorithm=None):

        number_of_instances_processed = self.total_size - self.dataset_size

        # zip data and labels and iterate over them and skip the first one because we already added them in CD
        for length, (data_point, label) in enumerate(zip(dataset[1:], class_labels[1:])):

            if label not in self.frequencies:
                self.frequencies[label] = 0

            # length + 1 because we skipped the first one
            acceptable_instances, acceptable_instances_labels, not_acceptable_instances, not_acceptable_instances_labels \
                = self._get_acceptable_instances(0.9, number_of_instances_processed + length + 1)

            if len(acceptable_instances) == 0:
                random_index = random.randint(0, len(self.cd) - 1)
                acceptable_instance = self.cd[random_index]
                acceptable_instance_label = self.cd_classes[random_index]
            else:
                # find the index of most similar one
                distance_matrix_sorted, min_indices = self._find_k_similar(data_point, acceptable_instances, k, distance_metric)
                similar_index = self._vote(min_indices, distance_matrix_sorted, acceptable_instances_labels, voting_algorithm)

                acceptable_instance = acceptable_instances[similar_index]
                acceptable_instance_label = acceptable_instances_labels[similar_index]

            if label == acceptable_instance_label:
                self.accuracies[str(acceptable_instance)]['correct'] += 1
                self.frequencies[label] += 1
                self.correct_num += 1
            else:
                self.accuracies[str(acceptable_instance)]['incorrect'] += 1
                self.cd.append(data_point)
                self.cd_classes.append(label)

                self.accuracies[str(data_point)] = {'correct': 0, 'incorrect': 0}

            # length + 2 because we already classified
            self.cd, self.cd_classes = self._update_cd(self.frequencies, 0.7, number_of_instances_processed + length + 2)

    def _calculate_boundaries(self, p, z, n):
        min_boundary = (p + z ** 2 / (2 * n) - z * (math.sqrt((p * (1 - p) / n) + (z ** 2 / (4 * n ** 2))))) / (1 + z ** 2 / n)
        max_boundary = (p + z ** 2 / (2 * n) + z * (math.sqrt((p * (1 - p) / n) + (z ** 2 / (4 * n ** 2))))) / (1 + z ** 2 / n)
        return [min_boundary, max_boundary]

    def _get_acceptable_instances(self, z, n):
        acceptable_instances = []
        acceptable_instances_labels = []
        not_acceptable_instances = []
        not_acceptable_instance_labels = []
        for cd_point, cd_label in zip(self.cd, self.cd_classes):
            try:
                accuracy_p = self.accuracies[str(cd_point)]['correct'] / (
                        self.accuracies[str(cd_point)]['correct'] + self.accuracies[str(cd_point)]['incorrect'])
            except ZeroDivisionError:
                accuracy_p = 0
            instance_accuracy = self._calculate_boundaries(accuracy_p, z, n)

            frequency_p = self.frequencies[cd_label] / n
            class_observed_frequency = self._calculate_boundaries(frequency_p, z, n)

            if instance_accuracy[0] > class_observed_frequency[1]:
                acceptable_instances.append(cd_point)
                acceptable_instances_labels.append(cd_label)
            else:
                not_acceptable_instances.append(cd_point)
                not_acceptable_instance_labels.append(cd_label)

        return acceptable_instances, acceptable_instances_labels, not_acceptable_instances, not_acceptable_instance_labels

    def _update_cd(self, frequencies, z, n):
        new_cd = []
        new_cd_labels = []
        for cd_point, cd_label in zip(self.cd, self.cd_classes):
            try:
                accuracy_p = self.accuracies[str(cd_point)]['correct'] / (
                        self.accuracies[str(cd_point)]['correct'] + self.accuracies[str(cd_point)]['incorrect'])
            except ZeroDivisionError:
                accuracy_p = 0
            instance_accuracy = self._calculate_boundaries(accuracy_p, z, n)

            frequency_p = frequencies[cd_label] / n
            class_observed_frequency = self._calculate_boundaries(frequency_p, z, n)

            # dont remove and save
            if not instance_accuracy[1] < class_observed_frequency[0]:
                new_cd.append(cd_point)
                new_cd_labels.append(cd_label)
            else:
                # remove from accuracies
                del self.accuracies[str(cd_point)]
        return new_cd, new_cd_labels

    def _find_similar(self, data_point, cd):
        # find euclidean distance between data point and entire cd
        distance_matrix = np.linalg.norm(np.array(cd) - data_point, axis=1)

        # find the index of the most similar one
        min_index = np.argmin(distance_matrix)
        return min_index

    def _find_k_similar(self, data_point, cd, k, distance_metric=None):
        # find euclidean distance between data point and entire cd
        if distance_metric is None:
            distance_matrix = np.linalg.norm(np.array(cd) - data_point, axis=1)
        elif distance_metric == 'HVDM':
            distance_matrix = HVDM(np.array(cd), data_point)
        else:
            distance_matrix = distance.cdist([data_point], np.array(cd), metric=distance_metric)[0]

        # sort distance matrix
        distance_matrix_sorted = np.sort(distance_matrix)[:k]
        # find the indexes of the most similar ones
        min_indices = np.argsort(distance_matrix)[:k]

        return distance_matrix_sorted, min_indices

    def _vote(self, min_indices, distance_matrix_sorted, cd_classes, voting_algorithm):
        if voting_algorithm is None:
            label = cd_classes[min_indices[0]]
        else:
            label = voting_algorithm(distance_matrix_sorted, cd_classes, min_indices)
        return label

    # calculate accuracy
    def calculate_accuracy(self):
        return self.correct_num / self.dataset_size

    def print_results(self):
        print(f"accuracy: {self.calculate_accuracy() * 100} %")
        print(f"execution time: {self.time}")
        print(f"used memory: {len(self.cd)} / {self.total_size}")

    def get_memory(self):
        return len(self.cd) / self.total_size
