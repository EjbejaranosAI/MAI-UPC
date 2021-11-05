# Return most frequent element in the list
from matplotlib import pyplot as plt
from sklearn import metrics
import numpy as np

def most_frequent(list):
    return max(set(list), key = list.count)

# Validate clustering
def validation(class_names,labels):
    labels_dict = {}
    labels_index_dict = {}
    classes = []
    labels_list = []
    recall = []
    precision = []
    confusion = {}
    confusion_matrix = []

    # Create list with labels from clustering, and corresponding classes names
    for i, label in enumerate(labels):
        d = (label, class_names[i])
        classes.append(d)

    # Create dictionary which stores labels as keys and class names as lists
    for label,name in classes:
        try:
            labels_dict[label].append(name)
        except KeyError:
            labels_dict[label] = [name]

    # Calculate the most frequent class name for each key and assign them as label indexes
    for index in set(labels):
        if index != -1:
            try:
                labels_index_dict[index].append(most_frequent(labels_dict[index]))
            except KeyError:
                labels_index_dict[index] = most_frequent(labels_dict[index])

    # Change label indexes for the predicted class names
    for k, l in enumerate(labels):
        if l != -1:
            labels_list.append(labels_index_dict[l])
        else:
            labels_list.append('no_class')

    # Calculate precision and recall for each class
    for ll in set(class_names):
        recall_list = []
        precision_v = 0
        for ii in range(0, len(labels_list)):
            if labels_list[ii] == class_names[ii] and class_names[ii] == ll:
                recall_list.append(1)
                precision_v += 1
            elif  labels_list[ii] != class_names[ii] and class_names[ii] == ll:
                recall_list.append(0)
            elif  labels_list[ii] == ll and class_names[ii] != ll:
                precision_v += 1
        recall.append(recall_list.count(1)/len(recall_list))
        if precision_v != 0:
            precision.append(recall_list.count(1)/precision_v)
        else:
            precision.append(0)
    accuracy = [precision, recall]

    #  Compute confusion matrix
    for ll in set(class_names):
        for ii in range(0, len(labels_list)):
            if class_names[ii] == ll:
                try:
                    confusion[ll].append(labels_list[ii])
                except KeyError:
                    confusion[ll] = [labels_list[ii]]
    for jj in set(class_names):
        for kk in set(class_names):
            confusion_matrix.append(((jj, kk),confusion[jj].count(kk)))
    print(confusion_matrix)

    # Calculate adjusted rand index for each class
    accuracy_ari = metrics.rand_score(list(class_names), labels_list)
    return accuracy, accuracy_ari

# Plot accuracy on a bar plot where x = class_names, y = accuracy
def plot_accuracy(accuracy, class_names):
    labels = list(set(class_names))

    x = np.arange(len(labels))
    w = 0.25

    # Plot precision and recall on two adjacent bars
    fig, ax = plt.subplots()
    preicison = ax.bar(x - w/2, accuracy[0], w, label='precision', color = 'b')
    recall = ax.bar(x + w/2, accuracy[1], w, label='recall', color = 'g')

    ax.set_title('Precision and recall')
    ax.set_xlabel('Class name')
    ax.set_ylabel('Score')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.bar_label(preicison)
    ax.bar_label(recall)
    fig.tight_layout()
    plt.show()
