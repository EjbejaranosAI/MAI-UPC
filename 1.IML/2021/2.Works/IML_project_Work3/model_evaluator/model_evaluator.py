import numpy as np

from ib.ib import IB
from ib.voting_policies import most_voted, plurality_voted, borda_voted
from utils.data_preprocess import load_dataset, preprocess_dataset
from utils.feature_selection import selectionIBLAlgorithm
from utils.utils import calculate_mean, calculate_variance
from utils.validation_tests import rank_data, nemenyi_test


class ModelEvaluator:
    def __init__(self, dataset):
        self.time = 0
        self.perfomance = {}
        self.k_perfomance = {}
        self.dataset = {}
        self.number_of_folds = 10

        self.configuration_matrices = {}
        self.configuration_mapping = {}

        self.dataset_name = dataset

        self.accuracy = []
        self.memories = []

        # options
        self.k_options = [1, 3, 5, 7]
        self.distance_algorithms = {'HVDM': 'HVDM', 'Eucledian': None, 'cityblock': 'cityblock', 'canberra': 'canberra'}
        self.voting_policies = {'borda_voted': borda_voted, 'most_voted': most_voted, 'plurality_voted': plurality_voted}

        # load folds
        for fold in range(self.number_of_folds):
            # load data
            self.dataset[fold] = {}

            train_data, train_labels, column_names = load_dataset(dataset, fold, 'train')
            test_data, test_labels, _ = load_dataset(dataset, fold, 'test')

            train_data, test_data = preprocess_dataset(train_data, test_data, column_names)

            self.dataset[fold]['train_data'] = train_data
            self.dataset[fold]['train_labels'] = train_labels
            self.dataset[fold]['test_data'] = test_data
            self.dataset[fold]['test_labels'] = test_labels

            print(f'Fold {fold + 1} Loaded')

    def evaluate_model(self, algorithm):
        accuracy = []
        memories = []
        self.time = 0
        self.perfomance[algorithm] = {}

        for fold in range(self.number_of_folds):
            model = IB(algorithm)

            # load data
            train_data, train_labels = self.dataset[fold]['train_data'], self.dataset[fold]['train_labels']
            test_data, test_labels = self.dataset[fold]['test_data'], self.dataset[fold]['test_labels']

            # fit and predict data
            model.fit_and_predict(train_data, train_labels)
            model.fit_and_predict(test_data, test_labels)

            # calculate test accuracy and save
            accuracy.append(model.calculate_accuracy())

            # get memories used
            memories.append(model.get_memory())

            # save evaluation time
            self.time += model.time

            # print results
            print(f"\n\nAlgorithm:{algorithm} \tFold:{fold + 1} \n")
            model.print_results()

        self.perfomance[algorithm]['accuracy'] = calculate_mean(accuracy)
        self.perfomance[algorithm]['variance'] = calculate_variance(accuracy)
        self.perfomance[algorithm]['time'] = self.time
        self.perfomance[algorithm]['memory'] = calculate_mean(memories)

        # print evaluation results
        self._print_evaluation_results(algorithm, accuracy)

    def find_best_configuration(self, algorithm):
        self.accuracy = []
        self.memories = []
        self.configuration_matrices = {}
        self.configuration_mapping = {}

        self.time = 0

        inx = 1
        for k in self.k_options:
            for distance_alg in self.distance_algorithms.keys():
                for voting_policy in self.voting_policies.keys():
                    self.k_perfomance[inx] = {}

                    self.k_perfomance[inx]['options'] = {}
                    self.k_perfomance[inx]['result'] = {}
                    accuracy = []
                    memories = []
                    time = 0
                    for fold in range(self.number_of_folds):
                        model = IB(algorithm)

                        # load data
                        train_data, train_labels = self.dataset[fold]['train_data'], self.dataset[fold]['train_labels']
                        test_data, test_labels = self.dataset[fold]['test_data'], self.dataset[fold]['test_labels']

                        # fit and predict data
                        model.fit_and_predict(train_data, train_labels, k, self.distance_algorithms[distance_alg],
                                              self.voting_policies[voting_policy])
                        model.fit_and_predict(test_data, test_labels, k, self.distance_algorithms[distance_alg],
                                              self.voting_policies[voting_policy])

                        # calculate test accuracy and save
                        accuracy.append(model.calculate_accuracy())

                        # get memories used
                        memories.append(model.get_memory())

                        # save evaluation time
                        time += model.time

                        # print results
                        # print(f"\n\nModel:{algorithm} \tFold:{fold} \n")
                        # model.print_results()

                    self.configuration_mapping[inx] = {'k': k, 'distance_algorithm': distance_alg,
                                                       'voting_policy': voting_policy}
                    self.configuration_matrices[inx] = accuracy

                    self.k_perfomance[inx]['options'] = {'k': k, 'distance_algorithm': distance_alg,
                                                         'voting_policy': voting_policy}
                    self.k_perfomance[inx]['result']['accuracy'] = calculate_mean(accuracy)
                    self.k_perfomance[inx]['result']['variance'] = calculate_variance(accuracy)
                    self.k_perfomance[inx]['result']['time'] = time
                    self.k_perfomance[inx]['result']['memory'] = calculate_mean(memories)
                    print(f'following configurations executed: {self.k_perfomance[inx]["options"]}, '
                          f'mean accuracy: {self.k_perfomance[inx]["result"]["accuracy"]}')
                    inx += 1
        ranked_data = rank_data(self.configuration_matrices)
        nemenyi = nemenyi_test(self.configuration_matrices)

    def find_best_ib(self):
        scores = {}
        for algorithm in self.perfomance.keys():
            result = self.perfomance[algorithm]

            scores[algorithm] = result['accuracy'] * 0.9 - result['variance'] * 0.24 * 100 + \
                                (1 / (result['memory'])) * 0.001 + (1 / (result['time'])) * 0.001
        best_algorithm = max(scores, key=lambda x: scores[x])
        print(f'\n\n\nBest Algorithm for "{self.dataset_name}" dataset is: {best_algorithm}')
        return max(scores, key=lambda x: scores[x])

    def select_features(self, method, number_of_features):
        data = self.dataset[0]['train_data']
        labels = self.dataset[0]['train_labels']
        feature_indices, weights_features, scores = selectionIBLAlgorithm(data, labels, method, number_of_features)
        print(f'--------------------------The weights for this dataset with feature selections are: -----------{weights_features}--------------------')
        print(f'--------------------------The relative scores for this dataset with feature selections are: --{scores}----------------------------------')
        for fold in range(self.number_of_folds):
            # load data

            self.dataset[fold]['train_data_fs'] = self.dataset[fold]['train_data'][:, feature_indices]
            self.dataset[fold]['test_data_fs'] = self.dataset[fold]['test_data'][:, feature_indices]

            print(f'Created new data with new Features for Fold: {fold + 1}')

    def k_ibl(self, algorithm, k, voting_policy, distance_alg, feature_selection):
        accuracy = []
        memories = []
        time = 0

        if feature_selection:
            train_data_property_name = 'train_data_fs'
            test_data_property_name = 'test_data_fs'
        else:
            train_data_property_name = 'train_data'
            test_data_property_name = 'test_data'

        for fold in range(self.number_of_folds):
            model = IB(algorithm)

            # load data
            train_data, train_labels = self.dataset[fold][train_data_property_name], self.dataset[fold]['train_labels']
            test_data, test_labels = self.dataset[fold][test_data_property_name], self.dataset[fold]['test_labels']

            # fit and predict data
            model.fit_and_predict(train_data, train_labels, k, self.distance_algorithms[distance_alg],
                                  self.voting_policies[voting_policy])
            model.fit_and_predict(test_data, test_labels, k, self.distance_algorithms[distance_alg],
                                  self.voting_policies[voting_policy])

            # calculate test accuracy and save
            accuracy.append(model.calculate_accuracy())

            # get memories used
            memories.append(model.get_memory())

            # save evaluation time
            time += model.time

        mean_accuracy = calculate_mean(accuracy)
        mean_memory = calculate_mean(memories)

        print(f'following configurations executed: k: {k}, voting policy: {voting_policy}, distance algorithm: {distance_alg} '
              f'mean accuracy: {mean_accuracy * 100}%, memory: {mean_memory * 100}%, time used: {time}, feature selection: {feature_selection}')

    # print evaluation results
    def _print_evaluation_results(self, algorithm, accuracy):
        print('\n\n\n')
        print(f'Final Results of the {algorithm} Algorithm:')
        print(f'Mean accuracy of the model is: {sum(accuracy) * 100 / len(accuracy)}%')
        print(f'Execution time for evaluation is: {self.time}')
