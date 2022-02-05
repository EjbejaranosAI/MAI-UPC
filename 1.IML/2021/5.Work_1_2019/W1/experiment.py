from agglomerative import Agglomerative
from file_manager import FileManager
from fuzzy_c_means import FuzzyCMeans
from k_means import KMeansClustering
from k_modes import KModes
from k_prototpyes import KPrototypes
import numpy as np
from preprocessor import Preprocessor
from validator import Validator
from enum import Enum


TABLE_INDEX = 0

class Experiment:

    def __init__(self, dataset_name, real_number_of_classes):
        self.name = dataset_name
        self.clusters = real_number_of_classes
        self.dataset, self.meta = FileManager().load_arff(self.name)
        self.exp_name = None
        self.metrics = {}
        self.ground_truth = None
        self.numerical = None
        self.nominal = None
        self.mixed = None
        self.validator = None

    def basic_experiment(self):
        self.__experiment_init()
        self.exp_name = "basic"
        print()
        self.__exp_iteration()
        self.__aggregate_results()
        print("\nExperimentation finished successfully.\n\n")

    def c_incremental_experiment(self):
        self.__experiment_init()
        print()
        for c in range(2, self.clusters+3):
            # Explore results for C in the range [2, real_classes+1]
            self.exp_name = "inc_c={}".format(c)
            self.__exp_iteration(c)
        for model, metrics in self.metrics.items():
            self.__process_model_metrics(model, metrics)
        print("\nExperimentation finished successfully.\n\n")

    def agglomerative_experiment(self):
        self.__experiment_init()
        self.exp_name = "agglom"
        for aff in Agglomerative.Affinity:
            for link in Agglomerative.Linkage:
                if not self.__ahc_valid_combination(aff, link):
                    continue
                print()
                self.__train_ahc_model(self.clusters, aff, link)
        self.__aggregate_results()
        print("\nExperimentation finished successfully.\n\n")

    def fuzzy_experiment(self):
        self.__experiment_init()
        self.exp_name = "fuzzy"
        print()
        fuzzy = FuzzyCMeans(self.numerical, v=False)
        fuzzy_coefficients = [1.4, 1.6, 1.8, 2.0, 2.2, 2.4]
        assignations, centroids, metrics = fuzzy.experiment(self.clusters, fuzzy_coefficients)
        for i in range(len(assignations)):
            print(" * * Processing... (m={})".format(fuzzy_coefficients[i]))
            title = "FCM (m={})".format(fuzzy_coefficients[i])
            self.__validate(assignations[i], title, centroids[i])
            print()
        self.__aggregate_fuzzy_results(metrics, fuzzy_coefficients)
        print("\nExperimentation finished successfully.\n\n")

    def __experiment_init(self):
        num_rows = len(self.dataset.index)
        print("Experimentation: \033[1m{}\033[0m (N={})\n".format(self.name, num_rows))
        self.__preprocess()
        FileManager().save_csv(self.numerical, self.name)
        _, gt_indices = np.unique(self.ground_truth, return_inverse=True)
        self.validator.plot_pca()
        self.validator.visualize(gt_indices, "Ground Truth")
        self.validator.internal_index_cal(gt_indices)
        self.validator.internal_index_db(gt_indices)
        self.metrics = {}

    def __preprocess(self):
        p = Preprocessor(self.dataset)
        p.preprocess()
        self.ground_truth = p.get_classification_data().values
        real_c = len(set(self.ground_truth))
        if real_c != self.clusters:
            self.__wrong_c_value_warning(real_c)
        self.numerical = p.get_numerical()
        self.nominal = p.get_nominal()
        self.mixed = p.get_mixed()
        self.validator = Validator(self.name, self.numerical, self.ground_truth)

    def __wrong_c_value_warning(self, true_c):
        message = "Incorrect number of ground-truth clusters: said {} but was {}"
        message = message.format(self.clusters, true_c)
        print()
        print("--------------------------------")
        print("       WARNING")
        print("       {}".format(message))
        print("--------------------------------")
        print()

    def __train_ahc_model(self, c, aff=None, link=None, exp_name=None):
        if aff is None:
            aff = Agglomerative.Affinity.euclidean
        if link is None:
            link = Agglomerative.Linkage.average
        numerical = self.numerical.to_numpy()
        model = Agglomerative(numerical, c, ahc_affinity=aff, ahc_linkage=link)
        assignations = model.clusterize()
        self.validator.plot_dendrogram(model.model_name(), model.get_model(), model.get_model().labels_)
        self.__validate(assignations, model.model_name())

    def __train_k_means_model(self, num_clusters):
        model = KMeansClustering(self.numerical.to_numpy())
        assignations, centroids = model.clusterize(num_clusters)
        self.__validate(assignations, model.model_name(), centroids)

    def __train_k_modes_model(self, num_clusters):
        model = KModes(self.nominal.to_numpy())
        assignations, _ = model.clusterize(num_clusters)
        self.__validate(assignations, model.model_name())

    def __train_k_proto_model(self, num_clusters):
        model = KPrototypes(self.mixed)
        assignations, _ = model.clusterize(num_clusters)
        self.__validate(assignations, model.model_name())

    def __train_fcm_model(self, c, m):
        model = FuzzyCMeans(self.numerical, m)
        assignations, centroids = model.clusterize(c)
        self.__validate(assignations, model.model_name(), centroids)

    def __exp_iteration(self, c=None):
        if c is None:
            c = self.clusters
        self.__train_ahc_model(c)
        print()
        self.__train_k_means_model(c)
        print()
        self.__train_k_modes_model(c)
        print()
        self.__train_k_proto_model(c)
        print()
        for m in [1.4, 2.0]:
            self.__train_fcm_model(c, m)
            print()

    def __process_model_metrics(self, model, metrics):
        coord = list(range(2, self.clusters + 3))
        title = "{} Performance-vs-C".format(model)
        # The only interesting metrics, while varying C, are the internal indices
        dav = metrics[self.Measurements.DAVIES.name]
        self.validator.plot_measurement(dav, "Davies-Bouldin Index", "C", title, coord)
        cal = metrics[self.Measurements.CALINSKI.name]
        self.validator.plot_measurement(cal, "Calinski-Harabasz Index", "C", title, coord)

    def __ahc_valid_combination(self, aff, link):
        aff_is_cosine = aff is Agglomerative.Affinity.cosine
        link_is_ward = link is Agglomerative.Linkage.ward
        if aff_is_cosine and link_is_ward:
            return False
        return True

    def __aggregate_fuzzy_results(self, metrics, fuzzy_coefficient):
        title = "{} - Fuzzy c-Mean - Performance by Fuzzy Coefficient 'm'".format(self.name)
        meas_name = "Partition Coefficient"
        self.validator.plot_measurement(metrics['ii'], meas_name, "m", title, c=fuzzy_coefficient)
        title = "{} - Fuzzy c-Mean performance by iteration".format(self.name)
        labels = ["m={}".format(m) for m in fuzzy_coefficient]
        self.validator.plot_measurements(metrics['iter'], labels, meas_name, "Iteration", title)

    def __aggregate_results(self):
        global TABLE_INDEX
        models = []
        acc_values = []
        ran_values = []
        dav_values = []
        cal_values = []
        for model, metrics in self.metrics.items():
            models.append(model)
            acc_values.append(metrics[self.Measurements.ACCURACY.name][0])
            ran_values.append(metrics[self.Measurements.RAND.name][0])
            dav_values.append(metrics[self.Measurements.DAVIES.name][0])
            cal_values.append(metrics[self.Measurements.CALINSKI.name][0])
        title = "{} Performance-vs-Algorithm".format("Accuracy (External Index)")
        self.validator.plot_bar(acc_values, "Accuracy", "Models", title, tick_labels=models)
        title = "{} Performance-vs-Algorithm".format("Adjusted Rand (External Index)")
        self.validator.plot_bar(ran_values, "Adjusted Rand Index", "Models", title, tick_labels=models)
        title = "{} Performance-vs-Algorithm".format("Davies-Bouldin (Internal Index)")
        self.validator.plot_bar(dav_values, "Davies-Bouldin Index", "Models", title, tick_labels=models)
        title = "{} Performance-vs-Algorithm".format("Calinski-Harabasz (Internal Index)")
        self.validator.plot_bar(cal_values, "Calinski-Harabasz Index", "Models", title, tick_labels=models)
        TABLE_INDEX += 1
        csv_file_name = "{}_{}_table_algo_comparison_c={}".format(TABLE_INDEX, self.name, self.clusters)
        self.validator.save_measurement(self.metrics, csv_file_name)

    def __validate(self, assignations, model_name, centroids=None):
        experiment_title = model_name + " " + self.exp_name
        self.validator.visualize(assignations, experiment_title, centroids)
        if model_name not in self.metrics:
            self.metrics[model_name] = {}
            for measurement in self.Measurements:
                self.metrics[model_name][measurement.name] = []
        accuracy = self.validator.external_validation_accuracy(assignations)
        self.metrics[model_name][self.Measurements.ACCURACY.name].append(accuracy)
        rand = self.validator.external_validation_adj_rand(assignations)
        self.metrics[model_name][self.Measurements.RAND.name].append(rand)
        davies = self.validator.internal_index_db(assignations)
        self.metrics[model_name][self.Measurements.DAVIES.name].append(davies)
        calinski = self.validator.internal_index_cal(assignations)
        self.metrics[model_name][self.Measurements.CALINSKI.name].append(calinski)

    class Method(Enum):
        AHC = "Agglomerative Clustering",
        K_MEANS = "k-Means Clustering",
        K_MODES = "k-Modes Clustering",
        K_PROTO = "k-Prototype Clustering",
        FUZZY = "Fuzzy c-Means Clustering"

    class Measurements(Enum):
        ACCURACY = "Accuracy (External Index)",
        CALINSKI = "Calinski-Harabasz (Internal Index)",
        DAVIES = "Davies-Bouldin (Internal Index)",
        RAND = "Adjusted Rand (External Index)"
