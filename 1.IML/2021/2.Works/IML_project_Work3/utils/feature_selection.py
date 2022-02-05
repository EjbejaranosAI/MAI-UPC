import numpy as np
from skrebate import ReliefF
from sklearn.feature_selection import mutual_info_classif, SelectKBest


def selectionIBLAlgorithm(data, labels, method, number_of_features):
    if method == 'i_gain':
        selector = SelectKBest(mutual_info_classif, k=number_of_features)
        selector.fit(data, labels)
        cols = selector.get_support(indices=True)
        scores = selector.scores_
    elif method == 'relief':
        featuresWeights = ReliefF(n_features_to_select=number_of_features, n_neighbors=20, n_jobs=-1)
        featuresWeights.fit_transform(data, labels)
        cols = np.array(featuresWeights.top_features_[0:number_of_features])
        scores = featuresWeights.feature_importances_
    weights = np.zeros(data.shape[1])
    weights[cols] = 1.0

    return cols, weights, scores
