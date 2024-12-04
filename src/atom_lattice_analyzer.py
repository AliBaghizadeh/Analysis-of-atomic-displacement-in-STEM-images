import atomap.api as am
from atomap.tools import remove_atoms_from_image_using_2d_gaussian

class AtomLatticeAnalyzer:
    def __init__(self, image):
        self.image = image

    def find_sublattice(self, separation_range, separation, color='red', pca=True):
        _ = am.get_feature_separation(self.image, separation_range=separation_range, pca=pca)
        atom_positions = am.get_atom_positions(self.image, separation=separation)
        sublattice = am.Sublattice(atom_position_list=atom_positions, image=self.image.data, color=color)
        return sublattice

    def refine_sublattice_positions(self, sublattice, percent_to_nn=0.25, mask_radius=None):
        sublattice.find_nearest_neighbors()
        sublattice.refine_atom_positions_using_center_of_mass(percent_to_nn=percent_to_nn)
        if mask_radius is not None:
            sublattice.refine_atom_positions_using_2d_gaussian(mask_radius=mask_radius)
        else:
            sublattice.refine_atom_positions_using_2d_gaussian()

    def plot_sublattice(self, sublattice):
        sublattice.plot()
