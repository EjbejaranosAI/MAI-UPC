import numpy as np
import pandas as pd
import sklearn
from matplotlib import pyplot as plt, gridspec
from scipy.io import arff
from sklearn.preprocessing import normalize, StandardScaler


def arff_to_df_normalized(content):
    data = arff.loadarff(content)  # With this we can work with datasets in format arff
    # Create a new variable to store the names of the headings for each column
    data_names = []
    df = pd.DataFrame()
    # We extract the columns
    for i, row in enumerate(data[0]):
        if i == 0:
            for j in range(len(row)):
                data_names.append(row.dtype.descr[j][0].lower())
            df = pd.DataFrame(columns=data_names)

        df.loc[i] = pd.Series(np.asarray(row).tolist(), index=data_names)

    # Delete the non-numerical data
    df = df.drop(['class'], axis=1)
    # Normalize the data
    scalar = StandardScaler()
    df_scaled = scalar.fit_transform(df)
    df_normalized = normalize(df_scaled)
    df_normalized = pd.DataFrame(df_normalized)
    df_normalized.columns = df.columns
    return df_normalized, data_names
