from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture


class ClusterAnalyzer:
    def __init__(self, data, number_of_cores=4):
        """
        Initialize with data and number of cores for parallel processing.

        Parameters:
            data (ndarray): The data to cluster.
            number_of_cores (int): Number of CPU cores to use for clustering.
                                   Default is 1 (single-threaded).
        """
        self.data = data
        self.number_of_cores = number_of_cores

    def kmeans(self, n_clusters):
        """
        Perform KMeans clustering with the specified number of cores.

        Parameters:
            n_clusters (int): Number of clusters.

        Returns:
            ndarray: Cluster labels.
        """
        with parallel_backend("threading", n_jobs=self.number_of_cores):
            kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=42)
            return kmeans.fit_predict(self.data)

    def gmm(self, n_components):
        """
        Perform Gaussian Mixture Model clustering.

        Parameters:
            n_components (int): Number of components.

        Returns:
            ndarray: Cluster labels.
        """
        gmm = GaussianMixture(n_components=n_components, random_state=42)
        return gmm.fit_predict(self.data)

    def tsne(self, n_components=2):
        """
        Perform t-SNE dimensionality reduction.

        Parameters:
            n_components (int): Number of dimensions to reduce to.

        Returns:
            ndarray: Reduced data.
        """
        with parallel_backend("threading", n_jobs=self.number_of_cores):
            tsne = TSNE(
                n_components=n_components, random_state=42, perplexity=30, n_iter=300
            )
            return tsne.fit_transform(self.data)

