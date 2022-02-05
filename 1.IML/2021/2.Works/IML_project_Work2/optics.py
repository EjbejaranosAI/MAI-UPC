#Import the libraries to manage the project
from operator import itemgetter
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import OPTICS
from sklearn.preprocessing import normalize, StandardScaler
# Import function for parsing the data and validating the results
from utils.arff_parser import arff_to_df_normalized
from utils.validator import validation, plot_accuracy

# Read the dataset from a relative path
content = "datasets/adult.arff"

# Parse the arff file to a dataframe
df_normalized, data_names_num, data_names_cat, data_names, class_names = arff_to_df_normalized(content)

# Change the categorical data into numerical and normalize it
try:
    df_normalized[list(itemgetter(*data_names_cat)(data_names))] = df_normalized[list(itemgetter(*data_names_cat)(data_names))].astype('category')
    df_normalized[list(itemgetter(*data_names_cat)(data_names))] = df_normalized[list(itemgetter(*data_names_cat)(data_names))].apply(lambda x: x.cat.codes)
    scalar = StandardScaler()
    df_scaled = scalar.fit_transform(df_normalized[list(itemgetter(*data_names_cat)(data_names))])
    df_normalized[list(itemgetter(*data_names_cat)(data_names))] = normalize(df_scaled)
except:
    pass

# Various models with different metrics and approximations
optics_model_min_kd_tree = OPTICS(min_samples = 10, xi = 0.001, min_cluster_size = 0.05, eps = 0.5, metric = 'minkowski', algorithm = 'kd_tree' )
optics_model_min_low_cluster_kd_tree = OPTICS(min_samples = 100, xi = 0.01, min_cluster_size = 0.05, metric = 'minkowski', eps = 10, algorithm = 'kd_tree' )
optics_model_man_low_cluster_kd_tree = OPTICS(min_samples = 50, xi = 0.01, min_cluster_size = 0.05, metric = 'manhattan', eps = 4, algorithm = 'kd_tree' )
optics_model_man_kd_tree = OPTICS(min_samples = 10, xi = 0.001, min_cluster_size = 0.05, eps = 1, metric = 'manhattan', algorithm = 'kd_tree' )
optics_model_che_kd_tree = OPTICS(min_samples = 10, xi = 0.001, min_cluster_size = 0.05, eps = 0.5, metric = 'chebyshev', algorithm = 'kd_tree' )
optics_model_min_brute = OPTICS(min_samples = 10, xi = 0.001, min_cluster_size = 0.05, eps = 0.5, metric = 'minkowski', algorithm = 'brute' )
optics_model_min_low_cluster_brute = OPTICS(min_samples = 100, xi = 0.01, min_cluster_size = 0.05, eps = 2, algorithm = 'brute' )
optics_model_man_brute = OPTICS(min_samples = 10, xi = 0.001, min_cluster_size = 0.05, eps = 0.5, metric = 'manhattan', algorithm = 'brute' )
optics_model_che_brute = OPTICS(min_samples = 10, xi = 0.001, min_cluster_size = 0.05, eps = 0.5, metric = 'chebyshev', algorithm = 'brute' )
optics_model_min_ball_tree = OPTICS(min_samples = 10, xi = 0.001, min_cluster_size = 0.05, eps = 0.5, metric = 'minkowski', algorithm = 'ball_tree' )
optics_model_min_low_cluster_ball_tree = OPTICS(min_samples = 100, xi = 0.01, min_cluster_size = 0.05, eps = 2, algorithm = 'ball_tree' )
optics_model_man_ball_tree = OPTICS(min_samples = 10, xi = 0.001, min_cluster_size = 0.05, eps = 0.5, metric = 'manhattan', algorithm = 'ball_tree' )
optics_model_che_ball_tree = OPTICS(min_samples = 10, xi = 0.001, min_cluster_size = 0.05, eps = 0.5, metric = 'chebyshev', algorithm = 'ball_tree' )

# Choose the model to execute
optics = optics_model_man_low_cluster_kd_tree

# Perform optics clustering
optics.fit(df_normalized)

# Calculate reachability distance of all points
reachability = optics.reachability_[optics.ordering_]
# Label each point to a cluster
labels = optics.labels_[optics.ordering_]
# Create a space for all datapoints
space = np.arange(len(df_normalized))

# Calculate properties of clusters and data
j = 0
for i in optics.labels_:

    if i ==-1:
        j+=1
print ('number of datapoints:',len(optics.labels_),'\nnumber of clustered datapoints:',len(optics.labels_) - j,'\npercent of clustered datapoints:', (len(optics.labels_) - j)/len(optics.labels_))

# Perform validation of the OPTICS model
accuracy, accuracy_ari = validation(class_names, labels)
print('Adjusted Rand Index: ', accuracy_ari)

# Plot the accuracy based on the validation script
plot_accuracy(accuracy, class_names)

# Plot results
plt.figure()
ax1 = plt.subplot(2,1,1)
ax2 = plt.subplot(2,1,2)
ax2.set_aspect('equal', adjustable='box')

# Plot reachability distances
color = []
for c in range(0,len(set(labels))-1):
    color.append(np.random.rand(3,))

for i, Label in enumerate(range(0,len(set(labels))-1)):
    X_points = space[labels == Label]
    Y_reachability = reachability[labels == Label]
    ax1.scatter(X_points, Y_reachability, color=color[i], alpha=0.3, s = 6)

# Unclustered points
ax1.scatter(space[labels == -1], reachability[labels == -1], color = 'k', alpha=0.3, s = 6)
ax1.plot(space, np.full_like(space, optics.eps , dtype = 'float'),  color = 'k', linestyle = '--', alpha=0.5)
ax1.set_xlabel('datapoints')
ax1.set_ylabel('distance')
ax1.set_title('OPTICS reachability')

# Plot the clustering by taking two first columns as parameters
for i, Label in enumerate(range(0,len(set(labels))-1)):
    X_clustered = df_normalized[optics.labels_ == Label]
    ax2.scatter(X_clustered.iloc[:, 0], X_clustered.iloc[:, 1], color=color[i], alpha=0.7, s = 6)

# Unclustered points
ax2.scatter(df_normalized.iloc[optics.labels_ == -1, 0],
         df_normalized.iloc[optics.labels_ == -1, 1], color = 'k',
         s = 6, alpha=0.05)
ax2.set_title('OPTICS clusters')
ax2.set_xlabel(data_names[0])
ax2.set_ylabel(data_names[1])

# Show the results
plt.tight_layout()
plt.show()


