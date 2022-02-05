from operator import itemgetter
import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import IncrementalPCA as PCA_incremental_sklearn
from sklearn.decomposition import PCA as PCA_sklearn
from utils import arff_parser


class PCA:
    def __init__(self, reduced_components):
        # number of components we want to reduce the data to
        self.reduced_components = reduced_components
        self.data_mean_sub = None
        self.new_components = None

    def fit(self, data):
        # subtract the mean vector from the dataset
        self.data_mean_sub = data - np.mean(data, axis=0)
        # calculate the covariance matrix of the dataset
        covariance_mat = np.cov(self.data_mean_sub, rowvar=False)
        # compute the eigen values and eigen vectors of the covariance matrix
        eigen_val, eigen_vec = np.linalg.eig(covariance_mat)
        eigen_vec = eigen_vec.transpose()
        print('Eigen values:', eigen_val)
        # return indexes of the eigen values in descending order (highest variability first)
        eigen_index = np.argsort(eigen_val)[::-1]
        # sort the eigen vectors by highest variability
        eigen_vec_sort = eigen_vec[eigen_index]
        # return declared "reduced_components" number of eigen vectors
        self.new_components = eigen_vec_sort[0:self.reduced_components]

    def transform(self):
        # reduce the dimensionality of the data bu creating a dot product
        data_reduced = np.dot(self.data_mean_sub, self.new_components.transpose())
        data_reduced = data_reduced.transpose()
        return data_reduced


def run_reduction():
    # import the data and convert it to a pandas dataframe
    content = "datasets/adult.arff"
    df_normalized, data_names, classes = arff_parser.arff_to_df_normalized(content)

    # Perform dimensionality reduction by our PCA class
    model = PCA(2)
    model.fit(df_normalized)
    data_reduced = model.transform()

    # Perform dimensionality reduction by sklearn PCA class
    model_sklearn = PCA_sklearn(2)
    model_sklearn.fit(df_normalized)
    data_reduced_sklearn = model_sklearn.transform(df_normalized)
    data_reduced_sklearn = data_reduced_sklearn.transpose()

    # Perform dimensionality reduction by sklearn Incremental PCA class
    model_sklearn_incremental = PCA_incremental_sklearn(2)
    model_sklearn_incremental.fit(df_normalized)
    data_reduced_sklearn_incremental = model_sklearn_incremental.transform(df_normalized)
    data_reduced_sklearn_incremental = data_reduced_sklearn_incremental.transpose()

    # transpose data for visualisation purposes
    df_normalized = df_normalized.transpose()

    # visualise data
    plt.figure()
    ax1 = plt.subplot(2, 2, 1)
    ax1.set_title('First two dimensions')
    ax1.set_aspect('equal', adjustable='box')
    ax2 = plt.subplot(2, 2, 2)
    ax2.set_title('Dimensions reduced by PCA')
    ax2.set_aspect('equal', adjustable='box')
    ax3 = plt.subplot(2, 2, 3)
    ax3.set_title('Dimensions reduced by PCA-sklearn')
    ax3.set_aspect('equal', adjustable='box')
    ax4 = plt.subplot(2, 2, 4)
    ax4.set_title('Dimensions reduced by IncrementalPCA-sklearn')
    ax4.set_aspect('equal', adjustable='box')

    # assign colours to every class
    colors = ['#FF3333', '#AAFF33', '#33FFCA', '#FF9133', '#33BDFF', '#0400FF', '#D400FF', '#FF008D', '#FFF633']
    color = []
    for c in range(0, len(set(classes))):
        color.append(colors[c])

    alpha = 0.6
    size = 5
    # plot the datapoints with respect to their classes
    for i, Class in enumerate(set(classes)):
        ax1.scatter(df_normalized.iloc[0][classes == Class], df_normalized.iloc[1][classes == Class], color=color[i], alpha=alpha, s=size)
        ax2.scatter(data_reduced[0][classes == Class], data_reduced[1][classes == Class], color=color[i], alpha=alpha, s=size)
        ax3.scatter(data_reduced_sklearn[0][classes == Class], data_reduced_sklearn[1][classes == Class], color=color[i], alpha=alpha, s=size)
        ax4.scatter(data_reduced_sklearn_incremental[0][classes == Class], data_reduced_sklearn_incremental[1][classes == Class], color=color[i],
                    alpha=alpha, s=size)

    # show plots
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    run_reduction()