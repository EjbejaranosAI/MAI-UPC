from sklearn.datasets import fetch_openml
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

# Dimension reduction and clustering libraries
import umap
import hdbscan
import sklearn.cluster as cluster
from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score
from Projects.IML_UB_MAI.IML_project_Work2.utils.arff_parser import arff_to_df_normalized
import time

tic = time.perf_counter()


dataset = 'datasets/vehicle.arff'
#dataset = 'datasets/cmc.arff'
#dataset = 'datasets/adult.arff'
df_normalized, data_names, classes = arff_to_df_normalized(dataset)

standard_embedding = umap.UMAP(random_state=42).fit_transform(df_normalized)

standard_embedding_max, standard_embedding_min = standard_embedding.max(), standard_embedding.min()
standard_embedding_normalize = (standard_embedding - standard_embedding_min) / (standard_embedding_max - standard_embedding_min)





color = ['#FF3333', '#AAFF33', '#33FFCA', '#FF9133', '#33BDFF', '#0400FF', '#D400FF', '#FF008D', '#FFF633']

for i, Class in enumerate(set(classes)):
    plt.scatter(standard_embedding_normalize[:, 0][classes == Class],standard_embedding_normalize[:, 1][classes == Class], cmap='Spectral', s=0.8, c = color[i])
plt.gca().set_aspect('equal', 'datalim')
plt.suptitle('UMAP REDUCER FOR VEHICLE DATASET')
plt.show()
#The following clustering was only to compare and visualize different groups and methods before applying UMAP
#Kmeans clustering
kmeans_labels = cluster.KMeans(n_clusters=4).fit_predict(df_normalized)

kmeans_labels_max, kmeans_labels_min = kmeans_labels.max(), kmeans_labels.min()
kmeans_labels_normalize = (kmeans_labels - kmeans_labels_min)/(kmeans_labels_max - kmeans_labels_min)



plt.scatter(standard_embedding_normalize[:, 0], standard_embedding_normalize[:, 1], c=kmeans_labels_normalize, s=0.8, cmap='Spectral');
plt.suptitle('UMAP REDUCER AND KMEANS CLUSTERING FOR VEHICLE DATASET ')
plt.show()

# UMAP Clustering

clusterable_embedding = umap.UMAP(
    n_neighbors=20,
    min_dist=0.0,
    n_components=4,
    random_state=42,
).fit_transform(df_normalized)

clusterable_embedding_max, clusterable_embedding_min = clusterable_embedding.max(), clusterable_embedding.min()
clusterable_embedding_normalize = (clusterable_embedding - clusterable_embedding_min)/(clusterable_embedding_max - clusterable_embedding_min)


for i, Class in enumerate(set(classes)):
    plt.scatter(clusterable_embedding_normalize[:, 0][classes == Class],clusterable_embedding_normalize[:, 1][classes == Class], cmap='Spectral', s=0.8, c = color[i])
plt.gca().set_aspect('equal', 'datalim')
plt.suptitle('UMAP CLUSTERING FOR VEHICLE DATASET')
plt.show()

toc = time.perf_counter()
print(f"Time to execute UMAP reduction and then clustering by UMAP : {toc - tic:0.4f} seconds")