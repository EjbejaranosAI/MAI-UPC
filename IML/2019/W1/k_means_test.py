from collections import Counter
from random import uniform
import unittest
from k_means import KMeansClustering


class KMeansClusteringTestCase(unittest.TestCase):
    def test_2_clusters_with_2_dimensions(self):
        data = [
            [0.1, 0.15],
            [0.2, 0.25],
            [0.15, 0.11],
            [0.90, 0.95],
            [0.80, 0.85],
            [0.75, 0.80],
            [0.81, 0.79]
        ]
        k_means = KMeansClustering(data)
        clusters = k_means.clusterize(2)
        print(clusters)
        self.assertIs(clusters[0] == clusters[1] == clusters[2], True, "first cluster is incorrect")
        self.assertIs(clusters[3] == clusters[4] == clusters[5] == clusters[6], True, "second cluster is incorrect")
        self.assertNotEqual(clusters[0], clusters[3], "objects assigned to the same cluster")

    def test_3_clusters_with_3_dimensions(self):
        data = [
            [0.01, 0.02, 0.03],
            [0.02, 0.03, 0.04],
            [0.03, 0.04, 0.05],
            [0.50, 0.51, 0.52],
            [0.51, 0.52, 0.53],
            [0.52, 0.53, 0.54],
            [0.91, 0.92, 0.93],
            [0.92, 0.93, 0.94],
            [0.93, 0.94, 0.95]
        ]
        k_means = KMeansClustering(data)
        clusters = k_means.clusterize(3)
        print(clusters)
        self.assertIs(clusters[0] == clusters[1] == clusters[2], True, "first cluster is incorrect")
        self.assertIs(clusters[3] == clusters[4] == clusters[5], True, "second cluster is incorrect")
        self.assertIs(clusters[6] == clusters[7] == clusters[8], True, "third cluster is incorrect")
        self.assertIs(clusters[0] == clusters[3] == clusters[6], False, "objects assigned to the same cluster")

    def test_3_clusters_with_3_dimensions_2(self):
        data = [
            [0.01, 0.02, 0.03],
            [0.02, 0.03, 0.04],
            [0.03, 0.04, 0.05],
            [0.015, 0.025, 0.035],
            [0.025, 0.035, 0.045],
            [0.035, 0.045, 0.055],
            [0.50, 0.51, 0.52],
            [0.51, 0.52, 0.53],
            [0.52, 0.53, 0.54],
            [0.505, 0.515, 0.525],
            [0.515, 0.525, 0.535],
            [0.525, 0.535, 0.545],
            [0.91, 0.92, 0.93],
            [0.92, 0.93, 0.94],
            [0.93, 0.94, 0.95],
            [0.915, 0.925, 0.935],
            [0.925, 0.935, 0.945],
            [0.935, 0.945, 0.955]
        ]
        k_means = KMeansClustering(data)
        clusters = k_means.clusterize(3)
        print(clusters)
        self.assertIs(clusters[0] == clusters[1] == clusters[2] == clusters[3], True, "first cluster is incorrect")
        self.assertIs(clusters[0] == clusters[4] == clusters[5], True, "first cluster is incorrect")
        self.assertIs(clusters[6] == clusters[7] == clusters[8] == clusters[9], True, "second cluster is incorrect")
        self.assertIs(clusters[6] == clusters[10] == clusters[11], True, "second cluster is incorrect")
        self.assertIs(clusters[12] == clusters[13] == clusters[14] == clusters[15], True, "third cluster is incorrect")
        self.assertIs(clusters[12] == clusters[16] == clusters[17], True, "third cluster is incorrect")
        self.assertIs(clusters[0] == clusters[6] == clusters[12], False, "objects assigned to the same cluster")

if __name__ == '__main__':
    unittest.main()