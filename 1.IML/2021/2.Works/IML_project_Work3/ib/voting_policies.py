import numpy as np


def most_voted(distances, cd_classes, min_indices):
    labels = []
    votes_ind = []
    # load sorted distances (data_point from cd)
    mean_distances = []
    votes_dup = []
    # Append the labels sorting by min indices (from min distance to max distance)
    for m in min_indices:
        labels.append(cd_classes[m])
    # Retrieve the indices of the labels
    for l in set(labels):
        votes_ind.append([i for i, x in enumerate(labels) if x == l])
    # Calculate the most occurences from the labels
    votes_len = [len(i) for i in votes_ind]
    # check if there are ties
    for v in votes_ind:
        if len(v) == max(votes_len):
            distance = []
            for iv in v:
                distance.append(distances[iv])
            mean_distances.append(np.mean(distance))
            votes_dup.append(v)
    # resolve the ties by precedence of the labels with the lowest mean distances
    where_min = np.where(mean_distances == min(mean_distances))
    most_voted_label = votes_dup[where_min[0][0]]
    return labels[most_voted_label[0]]


def plurality_voted(distances, cd_classes, min_indices):
    labels = []
    # Append the labels sorting by min indices (from min distance to max distance)
    for m in min_indices:
        labels.append(cd_classes[m])
    k = len(distances)
    for kk in range(k):
        votes_ind = []
        labels = labels[:k]
        # Retrieve the indices of the labels
        for l in set(labels):
            votes_ind.append([i for i, x in enumerate(labels) if x == l])
        # Calculate the most occurences from the labels
        votes_len = [len(i) for i in votes_ind]
        duplicate = []
        # Check if there are duplicates
        for v in votes_ind:
            if len(v) == max(votes_len):
                duplicate.append(1)
        # If there are duplicates, reduce the number of k
        if len(duplicate) > 1:
            k = k - 1
        else:
            # If there are no ties, append the label with most votes
            where = votes_len.index(max(votes_len))
            final_index = votes_ind[where][0]
            return labels[final_index]


def borda_voted(distances, cd_classes, min_indices):
    labels = []

    # Append the labels sorting by min indices (from min distance to max distance)
    for m in min_indices:
        labels.append(cd_classes[m])
    k = len(distances)
    for i in range(k):
        duplicate = []
        scores = []
        scores_sum = []
        labels = labels[:k]
        lbls = list(set(labels))
        # Create a scoring list
        for kk in range(k):
            score = k - (kk + 1)
            scores.append(score)
        scores = np.array(scores)
        # For every vote append the score by assigning k - 1 to the best, and 0 to the worst
        for l in lbls:
            ind = np.where(labels == l)
            scores_sum.append(np.sum(scores[ind]))
        for s in scores_sum:
            # Check if there are ties
            if s == max(scores_sum):
                duplicate = np.append(duplicate, 1)
        # If there are ties reduce the k number
        if len(duplicate) > 1:
            k = k - 1
        # If there are no ties, append the label with the highest score
        else:
            if len(scores_sum) > 1:
                where = np.where(max(scores_sum))
                final_label = lbls[where[0][0]]
                min_index = where[0][0]
            else:
                final_label = lbls[0]
                min_index = 0
            return labels[min_index]

