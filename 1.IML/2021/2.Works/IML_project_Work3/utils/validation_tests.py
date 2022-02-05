from scikit_posthocs import posthoc_nemenyi_friedman
from scipy import stats
import numpy as np
from scipy.stats import rankdata


def friedman_test(configuration_file):
    configuration_array = np.array([array for index, array in configuration_file.items()])
    return stats.friedmanchisquare(configuration_array)


def nemenyi_test(configuration_file):
    configuration_array = np.array([array for index, array in configuration_file.items()])
    return posthoc_nemenyi_friedman(configuration_array.transpose())


def t_test(array):
    tpvalues = []
    pairs_items = ([(array[i], array[j]) for i in range(len(array)) for j in range(i + 1, len(array))])
    indices = [i + 1 for i in range(len(array))]
    pairs_indices = ([(indices[i], indices[j]) for i in range(len(indices)) for j in range(i + 1, len(indices))])
    print(pairs_items)
    print(pairs_indices)
    for pi, pii in zip(pairs_items, pairs_indices):
        t, p = stats.ttest_ind(pi[0], pi[1])
        tpvalues.append((t, p))
        print(f'For pair {pii[0]} and {pii[1]}, the p-value was {p} and t-value was {t}')
    return tpvalues


def rank_data(configuration_file):
    configuration_array = np.array([array for index, array in configuration_file.items()])
    ranked_data = rankdata(configuration_array, method='average', axis=0).reshape(configuration_array.shape)
    # for reversing rankings
    return len(configuration_array) - ranked_data
