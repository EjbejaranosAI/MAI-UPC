from operator import itemgetter

import numpy as np
import pandas as pd
from scipy.io import arff
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import normalize, StandardScaler

DATASET_PATH = 'datasetsCBR'


def load_dataset(dataset_name, fold, mode):
    dataset_path = f"{DATASET_PATH}/{dataset_name}/{dataset_name}.fold.{fold:06}.{mode}.arff"
    data, labels, column_names = arff_to_df_normalized(dataset_path)
    labels = [label.decode("utf-8") for label in labels.to_numpy()]
    return data, np.array(labels), column_names


def preprocess_dataset(train_data, test_data, column_names):
    # remove columns that has more than 80% nans
    train_data = train_data.dropna(thresh=len(train_data) * 0.8, axis=1)
    train_data = train_data.fillna(train_data.mean())

    data_names = [name for name in column_names if name in train_data.columns]

    # scale and normalize
    scalar = StandardScaler()
    df_scaled = scalar.fit_transform(train_data)
    df_normalized = normalize(df_scaled)
    train_data = pd.DataFrame(df_normalized, columns=data_names)

    test_data = test_data[data_names]
    test_data = test_data.fillna(test_data.mean())

    scalar = StandardScaler()
    df_scaled = scalar.fit_transform(test_data)
    df_normalized = normalize(df_scaled)
    test_data = pd.DataFrame(df_normalized, columns=data_names)

    return train_data.to_numpy(), test_data.to_numpy()


def arff_to_df_normalized(content) -> object:
    global num_columns
    data = arff.loadarff(content)  # With this we can work with datasets in arff format
    # Create a new variable to store the names of the headings for each column
    data_names = []
    data_names_num = []
    data_names_cat = []
    df_num = pd.DataFrame()
    df_cat = pd.DataFrame()
    df = pd.DataFrame()

    # We extract the columns
    for i, row in enumerate(data[0]):
        if i == 0:
            for j in range(len(row)):
                data_names.append(row.dtype.descr[j][0].lower())
                if isinstance(row[j], np.bytes_):
                    data_names_cat.append(j)
                else:
                    data_names_num.append(j)
            num_columns = list(itemgetter(*data_names_num)(data_names)) if len(data_names_num) > 0 else []
            cat_columns = list(itemgetter(*data_names_cat)(data_names)) if len(data_names_cat) > 1 else [data_names[data_names_cat[0]]]

            df_num = pd.DataFrame(columns=num_columns)
            df_cat = pd.DataFrame(columns=cat_columns)
            df = pd.DataFrame(columns=data_names)
        num_data = list(itemgetter(*data_names_num)(row))

        # if we have more classes besides "class"
        if len(data_names_cat) > 1:
            cat_data = [categorical.decode('UTF-8') if isinstance(categorical, np.bytes_) else categorical for categorical in
                        itemgetter(*data_names_cat)(row)]
        # if we only have "class"
        else:
            cat_data = [row[data_names_cat[0]].decode('UTF-8') if isinstance(row[data_names_cat[0]], np.bytes_) else row[data_names_cat[0]]]

        df_num.loc[i] = pd.Series(num_data, index=num_columns)
        df_cat.loc[i] = pd.Series(cat_data, index=cat_columns)

        df.loc[i] = pd.Series(list(row), index=data_names)

    # encode every categorical data
    for index in data_names_cat[:-1]:
        df[data_names[index]] = LabelEncoder().fit_transform(df[data_names[index]])

    # Delete the non-numerical data
    labels = df.pop('class')

    # remove "class" from data names
    data_names = data_names[:-1]

    return df, labels, data_names
