from sklearn.cluster import AgglomerativeClustering
from enum import Enum


class Agglomerative:

    def __init__(self, data, c, ahc_affinity=None, ahc_linkage=None):
        self.data = data
        self.affinity = ahc_affinity
        if self.affinity is None:
            self.affinity = self.Affinity.euclidean
        self.linkage = ahc_linkage
        if self.linkage is None:
            self.linkage = self.Linkage.ward
        self.ahc = AgglomerativeClustering(
            n_clusters=c,
            affinity=self.affinity.name,
            linkage=self.linkage.name
        )

    def model_name(self):
        title = "AHC (a={},l={})"
        aff = self.affinity.name[:2]
        lin = self.linkage.name[:2]
        return title.format(aff, lin)

    def clusterize(self):
        print(" * Clustering data with {}...".format(self.model_name()))
        return self.ahc.fit_predict(self.data)

    def get_model(self):
        return self.ahc

    class Affinity(Enum):
        euclidean = 1,
        cosine = 2

    class Linkage(Enum):
        single = 1,
        complete = 2,
        average = 3,
        ward = 4
