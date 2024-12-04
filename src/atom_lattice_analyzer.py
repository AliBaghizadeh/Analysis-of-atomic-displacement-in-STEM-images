import atomap.api as am
from atomap.tools import remove_atoms_from_image_using_2d_gaussian

class AtomLatticeAnalyzer:
    def __init__(self, image):
        """
        Initialize with the image to analyze.

        Parameters:
            image (hyperspy.Signal): The image containing atom lattice structures.
        """
        self.image = image

    def find_sublattice(self, separation_range, separation, color='red', pca=True):
        """
        Find and initialize a sublattice.

        Parameters:
            separation_range (tuple): Range of feature separation for peak detection.
            separation (float): Atom separation value for sublattice initialization.
            color (str): Color of sublattice markers. Default is 'red'.
            pca (bool): Whether to use PCA for peak detection. Default is True.

        Returns:
            atomap.Sublattice: Detected sublattice object.
        """
        _ = am.get_feature_separation(self.image, separation_range=separation_range, pca=pca)
        atom_positions = am.get_atom_positions(self.image, separation=separation)
        sublattice = am.Sublattice(atom_position_list=atom_positions, image=self.image.data, color=color)
        return sublattice

    def refine_sublattice_positions(self, sublattice, percent_to_nn=0.25, mask_radius=None):
        """
        Refine atom positions in the sublattice using center-of-mass and Gaussian methods.

        Parameters:
            sublattice (atomap.Sublattice): The sublattice to refine.
            percent_to_nn (float): Adjustment parameter for refinement. Default is 0.25.
            mask_radius (float, optional): Mask radius for Gaussian refinement.
        """
        sublattice.find_nearest_neighbors()
        sublattice.refine_atom_positions_using_center_of_mass(percent_to_nn=percent_to_nn)
        if mask_radius is not None:
            sublattice.refine_atom_positions_using_2d_gaussian(mask_radius=mask_radius)
        else:
            sublattice.refine_atom_positions_using_2d_gaussian()

    def construct_zone_axes(self, sublattice):
        """
        Construct zone axes based on the given sublattice.

        Parameters:
            sublattice (atomap.Sublattice): The sublattice to analyze.

        Returns:
            list: Zone axes average distances.
        """
        sublattice.construct_zone_axes()
        return sublattice.zones_axis_average_distances

    def find_second_sublattice(self, sublattice, zone_axes):
        """
        Find the second sublattice using zone axes alignment.

        Parameters:
            sublattice (atomap.Sublattice): The reference sublattice (e.g., Ba).
            zone_axes (list): Zone axes for sublattice alignment.

        Returns:
            tuple: Atom positions and intensity-subtracted image.
        """
        atom_positions = sublattice.find_missing_atoms_from_zone_vector(zone_axes)
        image_atoms_subtracted = remove_atoms_from_image_using_2d_gaussian(sublattice.image, sublattice)
        return atom_positions, image_atoms_subtracted

    def plot_sublattice(self, sublattice):
        """
        Plot the detected sublattice.

        Parameters:
            sublattice (atomap.Sublattice): The sublattice to plot.
        """
        sublattice.plot()

