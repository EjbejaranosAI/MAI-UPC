from operator import itemgetter

import numpy as np
import pandas as pd
from scipy.io import arff
from sklearn.preprocessing import normalize, StandardScaler, LabelEncoder


def arff_to_df_normalized(content) -> object:
    global num_columns
    data = arff.loadarff(content)  # With this we can work with datasets in format arff
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
        # if only we have "class"
        else:
            cat_data = [row[data_names_cat[0]].decode('UTF-8') if isinstance(row[data_names_cat[0]], np.bytes_) else row[data_names_cat[0]]]

        df_num.loc[i] = pd.Series(num_data, index=num_columns)
        df_cat.loc[i] = pd.Series(cat_data, index=cat_columns)

        df.loc[i] = pd.Series(list(row), index=data_names)


    # encode every categorical data
    for index in data_names_cat[:-1]:
        df[data_names[index]] = LabelEncoder().fit_transform(df[data_names[index]])

    # Delete the non-numerical data
    class_names = df.pop('class')

    # remove "class" from data names
    data_names = data_names[:-1]

    # Normalize the data
    scalar = StandardScaler()
    df_scaled = scalar.fit_transform(df)
    df_normalized = normalize(df_scaled)
    df_normalized = pd.DataFrame(df_normalized, columns=data_names)
    return df_normalized, data_names, class_names
