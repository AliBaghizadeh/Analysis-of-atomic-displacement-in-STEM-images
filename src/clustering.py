from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

class ClusterAnalyzer:
    def __init__(self, data):
        self.data = data

    def kmeans(self, n_clusters):
        return KMeans(n_clusters=n_clusters).fit_predict(self.data)

    def gmm(self, n_components):
        return GaussianMixture(n_components=n_components).fit_predict(self.data)
