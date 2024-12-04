import numpy as np
from topotem.polarisation import plot_polarisation_vectors
from sklearn.decomposition import PCA

class DisplacementAnalyzer:
    def __init__(self, sublatticeBa, sublatticeTi, image, sampling, unit, path, name):
        """
        Initialize with Ba and Ti sublattices, image metadata, and save path.

        Parameters:
            sublatticeBa (atomap.Sublattice): Reference (Ba) sublattice.
            sublatticeTi (atomap.Sublattice): Target (Ti) sublattice.
            image (hyperspy.Signal): Original image data.
            sampling (float): Sampling scale.
            unit (str): Unit of the image axes (e.g., nm or Å).
            path (str): Path to save plots.
            name (str): File name prefix for saving results.
        """
        self.sublatticeBa = sublatticeBa
        self.sublatticeTi = sublatticeTi
        self.image = image
        self.sampling = sampling
        self.unit = unit
        self.path = path
        self.name = name
        self.polarization_data = None

    def calculate_displacement(self, z1, z2):
        """
        Calculate polarization vectors for the Ti sublattice relative to Ba.

        Parameters:
            z1, z2 (list): Zone axes of interest.

        Returns:
            tuple: x, y positions and u, v displacement vectors.
        """
        polarization = self.sublatticeBa.get_polarization_from_second_sublattice(z1, z2, self.sublatticeTi)
        vector_list = polarization.metadata.vector_list
        x, y, u, v = zip(*vector_list)
        self.polarization_data = np.array([x, y, u, v]).T
        return x, y, u, v

    def denoise(self, method="pca", **kwargs):
        """
        Apply denoising techniques to displacement vectors.

        Parameters:
            method (str): Denoising method ('pca', 'svd', 'kernel_pca', or 'none'). Default is 'pca'.

        Returns:
            tuple: Denoised x, y positions and u, v displacement vectors.
        """
        ...
