import os
import hyperspy.api as hs

class ImageHandler:
    def __init__(self, path):
        """
        Initialize with the directory path for image files.

        Parameters:
            path (str): Directory containing the image files.
        """
        self.path = path
        self.images = self._load_images()

    def _load_images(self):
        """
        Scan the directory for supported image files.

        Returns:
            list: A list of image file names with extensions .dm3, .dm4, or .png.
        """
        return [file for file in os.listdir(self.path) if file.endswith((".dm3", ".dm4", ".png"))]

    def load_image(self, file_name):
        """
        Load a specific image file using HyperSpy.

        Parameters:
            file_name (str): Name of the image file to load.

        Returns:
            hyperspy.Signal: Loaded image as a HyperSpy signal object.
        """
        return hs.load(os.path.join(self.path, file_name))

    def save_image(self, image, file_name):
        """
        Save a processed image to the results directory.

        Parameters:
            image (hyperspy.Signal): The image to save.
            file_name (str): Name of the file to save the image as.
        """
        image.save(os.path.join(self.path, "results", file_name))

    def create_results_dir(self):
        """
        Create a results directory for saving outputs if it does not already exist.
        """
        os.makedirs(os.path.join(self.path, "results"), exist_ok=True)
