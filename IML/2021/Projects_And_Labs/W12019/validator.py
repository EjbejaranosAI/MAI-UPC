from collections import Counter
import numpy as np
from scipy.cluster.hierarchy import dendrogram
from sklearn.metrics import (
    accuracy_score,
    adjusted_rand_score,
    calinski_harabasz_score,
    confusion_matrix,
    davies_bouldin_score
)
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
import pandas as pd
from file_manager import FileManager


figure_index = 0


class Validator:

    def __init__(self, name, dataset, ground_truth):
        self.name = name
        self.dataset = dataset
        self.ground_truth = ground_truth
        self.pca = PCA(n_components=2)
        # Compute the PCA-transformation for the input data
        self.pc = self.pca.fit_transform(self.dataset.to_numpy())

    def __save_figure_png(self, figure_name):
        global figure_index
        figure_index += 1
        exp_dir = FileManager().experiment_dir(self.name)
        serial_n = "{}_{:03d}_{}".format(self.name, figure_index, figure_name)
        file_name = "{}/{}.png".format(exp_dir, serial_n)
        plt.savefig(file_name)
        plt.close()

    def external_validation_accuracy(self, clustering_result):
        clustering = self.__map_values_by_frequency(clustering_result)
        ground_truth = self.__map_values_by_frequency(self.ground_truth)
        accuracy = -1
        optimal_rotation = None
        for rotation in self.__get_label_rotations(clustering):
            new_accuracy = accuracy_score(ground_truth, rotation)
            if new_accuracy > accuracy:
                optimal_rotation = rotation
                accuracy = new_accuracy
        print("   - Confusion matrix:")
        self.__pretty_print_confusion_matrix(ground_truth, optimal_rotation)
        print("   - Accuracy (External Index): {0:.3f}".format(accuracy))
        return accuracy

    def __pretty_print_confusion_matrix(self, ground_truth, clustering):
        """
        Code extracted from Internet
        """
        matrix = confusion_matrix(ground_truth, clustering)
        s = [[str(e) for e in row] for row in matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print("          " + '\n          '.join(table))

    def __get_label_rotations(self, clustering):
        n = len(clustering)
        labels = list(set(clustering))
        l = len(labels)
        rotations = [clustering]
        for i in range(1, l):
            new_values = labels[i:] + labels[:i]
            mapping = {}
            new_rotation = []
            for j in range(l):
                mapping[labels[j]] = new_values[j]
            for k in range(n):
                current_value = clustering[k]
                mapped_value = mapping[current_value]
                new_rotation.append(mapped_value)
            rotations.append(new_rotation)
        return rotations

    def external_validation_adj_rand(self, clustering_result):
        clustering = self.__map_values_by_frequency(clustering_result)
        ground_truth = self.__map_values_by_frequency(self.ground_truth)
        index = adjusted_rand_score(ground_truth, clustering)
        print("   - Adjusted Rand (External Index): {0:.3f}".format(index))
        return index

    def internal_index_cal(self, clustering_result):
        index = calinski_harabasz_score(self.dataset.to_numpy(), clustering_result)
        print("   - Calinski-Harabasz (Internal Index): {0:.3f}".format(index))
        return index

    def internal_index_db(self, clustering_result):
        index = davies_bouldin_score(self.dataset.to_numpy(), clustering_result)
        print("   - Davies-Bouldin (Internal Index): {0:.3f}".format(index))
        return index

    def plot_dendrogram(self, title, model, labels):
        """
        Code extracted from Internet
        """
        if len(labels) > 1000:
            return None
        children = model.children_
        distance = np.arange(children.shape[0])
        no_of_observations = np.arange(2, children.shape[0] + 2)
        linkage_matrix = np.column_stack([children, distance, no_of_observations]).astype(float)
        dendrogram(linkage_matrix, labels=labels)
        plt.title("Dendrogram: {}".format(title))
        self.__save_figure_png("dendrogram_{}".format(title).lower().replace(' ', '_'))

    def plot_pca(self):
        # Plot PCA variance ratio
        aux_pca = PCA(n_components=len(self.dataset.columns))
        _ = aux_pca.fit_transform(self.dataset.to_numpy())
        features = range(aux_pca.n_components_)
        plt.bar(features, aux_pca.explained_variance_ratio_, color='#640039')
        plt.xlabel('PCA Features')
        plt.ylabel('Variance %')
        plt.xticks(features)
        plt.title("Principal Component Analysis")
        self.__save_figure_png("pca_variance")

    def save_measurement(self, measurement_dictionary, name):
        FileManager().save_csv(pd.DataFrame.from_dict(measurement_dictionary), name)
        return None

    def plot_measurement(self, meas_value, meas_label, iter_label, title, c=None):
        if c is None:
            plt.plot(meas_value, c=self.COLORMAP[0])
        else:
            plt.plot(c, meas_value, c=self.COLORMAP[0])
        plt.ylabel(meas_label)
        plt.xlabel(iter_label)
        plt.title(title)
        figure_name = "measurement_{}_{}_{}".format(title, meas_label, iter_label)
        self.__save_figure_png(figure_name.lower().replace(' ', '_'))

    def plot_bar(self, heights, ylabel, xlabel, title, tick_labels=None):
        y_pos = np.arange(len(heights))
        plt.bar(y_pos, heights, align='center')
        if tick_labels is not None:
            plt.xticks(y_pos, tick_labels, fontsize=6, ha="center")
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        plt.title(title)
        figure_name = "measurement_{}_{}_{}".format(title, ylabel, xlabel)
        self.__save_figure_png(figure_name.lower().replace(' ', '_'))

    def plot_measurements(self, values, labels, yl, xl, title, c=None):
        for i in range (len(values)):
            if c is None:
                plt.plot(values[i], label=labels[i], c=self.COLORMAP[i])
            else:
                plt.plot(c, values[i], label=labels[i], c=self.COLORMAP[i])
        plt.ylabel(yl)
        plt.xlabel(xl)
        plt.title(title)
        plt.legend()
        figure_name = "measurement_{}_{}_{}".format(title, yl, xl)
        self.__save_figure_png(figure_name.lower().replace(' ', '_'))

    def visualize(self, clustering, title, centroids=None):
        # Visualize the clustering partition using the PCA-transformation
        print("   - Visualizing...")
        components = pd.DataFrame(self.pc)
        fig, ax = plt.subplots()
        ax.scatter(
            components[0],
            components[1],
            alpha=.1,
            c=self.COLORMAP[clustering]
        )
        if centroids is not None:
            centroids_comp = self.pca.transform(centroids)
            ax.scatter(
                centroids_comp[:, 0],
                centroids_comp[:, 1],
                marker='*',
                s=200,
                c='#050505'
            )
        plt.xlabel('Eigenvektor 1')
        plt.ylabel('Eigenvektor 2')
        plt.title(title)
        lower_under_title = title.lower().replace(' ', '_')
        figure_name = "clustering_{}".format(lower_under_title)
        self.__save_figure_png(figure_name)

    COLORMAP = np.array([
        'r',
        'g',
        'b',
        'c',
        'm',
        'y',
        'k',
        '#7D6E00',
        '#4E7500',
        '#640039',
        '#1F0055',
        '#544A00',
        '#344E00',
        '#430026',
        '#150039',
        '#bcbd22',
        '#17becf'
    ])

    def __map_values_by_frequency(self, values):
        result = np.empty(np.array(values).shape)
        mapping = {}
        i = 0
        for value, _ in Counter(values).most_common():
            mapping[value] = i
            i += 1
        for i, value in enumerate(values):
            result[i] = mapping[value]
        return result
