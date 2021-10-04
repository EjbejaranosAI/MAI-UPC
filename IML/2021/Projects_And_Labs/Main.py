import numpy as np
import pandas as pd
from scipy.io import arff

content = "datasets/datasets/vehicle.arff"
data = arff.loadarff(content)
data_names = []
df = pd.DataFrame()
for i, row in enumerate(data[0]):
    if i == 0:
        for j in range(len(row)):
            data_names.append(row.dtype.descr[j][0])
        df = pd.DataFrame(columns=data_names)

    df.loc[i] = pd.Series(np.asarray(row).tolist(), index=data_names)

print(df.head())
