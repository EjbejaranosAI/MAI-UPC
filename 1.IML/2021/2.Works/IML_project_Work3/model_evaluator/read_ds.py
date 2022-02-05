from utils.arff_parser import arff_to_df_normalized
from sklearn.preprocessing import normalize, StandardScaler
import pandas as pd
# load normalized data
#dataset_name = 'satimage'
#dataset_path = 'datasetsCBR'

# load normalized data
'''def _load_dataset(dataset_name, fold, mode):
    #dataset_path = f"/home/ejbejaranos/Desktop/MAI-UPC/IML2021/Projects/IML_UB_MAI/IML_project_Work3/tasetsCBR/{dataset_name}/{dataset_name}.fold.{fold:06}.{mode}.arff"
    dataset_path = 'datasetsCBR/satimage/satimage.fold.000000.train.arff'
    data, labels, column_names = arff_to_df_normalized(dataset_path)

    return data, labels, column_names'''


'''dataset_path = f'../datasetsCBR/satimage/satimage.fold.000000.train.arff'
data, labels, column_names = arff_to_df_normalized(dataset_path)

'''

def _load_dataset(dataset_name, fold, mode):
    X_data = []
    classes = []
    column_names = []
    dataset_path = f"../datasetsCBR/{dataset_name}/{dataset_name}.fold.{fold:06}.{mode}.arff"
    X_data, classes, column_names = arff_to_df_normalized(dataset_path)
    print(X_data)
    print(column_names)
    print(classes)
    return X_data, classes, column_names

_load_dataset('satimage', 0, 'train')
'''
def _preprocess_dataset(self, train_data, test_data, column_names):
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
'''