from experiment import Experiment


if __name__ == '__main__':

    # Define pairs for dataset-name vs real-number-of-classes
    datasets = [('vote', 2), ('cmc',3), ('satimage',6)]

    # Run the experiments for the aforementioned datasets
    for dataset in datasets:
        name, n_clusters = dataset
        Experiment(name, n_clusters).basic_experiment()
        Experiment(name, n_clusters).c_incremental_experiment()
        Experiment(name, n_clusters).agglomerative_experiment()
        Experiment(name, n_clusters).fuzzy_experiment()
