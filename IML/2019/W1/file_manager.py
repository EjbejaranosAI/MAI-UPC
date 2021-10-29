import os
from scipy.io import arff
import pandas as pd


class FileManager:

    def load_arff(self, dataset_name):
        dataset_path = self.__get_dataset_file_path(dataset_name)
        data, meta = arff.loadarff(dataset_path)
        df = pd.DataFrame(data)
        return df, meta

    def save_csv(self, content_data_frame, csv_file_name):
        content_data_frame.to_csv("./temp/{}.csv".format(csv_file_name))

    def experiment_dir(self, dataset_name):
        experiment_dir = "./temp/{}".format(dataset_name)
        if not os.path.exists(experiment_dir):
            os.makedirs(experiment_dir)
        return experiment_dir

    def __get_dataset_file_path(self, dataset_name):
        root_dir = os.path.dirname(__file__)
        datasets_dir = os.path.join(root_dir, './resources/datasets')
        return os.path.join(datasets_dir, dataset_name + '.arff')
