import numpy as np
from topotem.polarisation import plot_polarisation_vectors
from sklearn.decomposition import PCA

class DisplacementAnalyzer:
    def __init__(self, sublatticeBa, sublatticeTi, image, sampling, unit, path, name):
        self.sublatticeBa = sublatticeBa
        self.sublatticeTi = sublatticeTi
        self.image = image
        self.sampling = sampling
        self.unit = unit
        self.path = path
        self.name = name
        self.polarization_data = None

    def calculate_displacement(self, z1, z2):
        polarization = self.sublatticeBa.get_polarization_from_second_sublattice(z1, z2, self.sublatticeTi)
        vector_list = polarization.metadata.vector_list
        x, y, u, v = zip(*vector_list)
        self.polarization_data = np.array([x, y, u, v]).T
        return x, y, u, v

    def plot_vector_magnitude(self, x, y, u, v):
        plot_polarisation_vectors(
            x, y, u, v, image=self.image.data, sampling=self.sampling, units=self.unit
        )
