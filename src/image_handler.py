import os
import hyperspy.api as hs

class ImageHandler:
    def __init__(self, path):
        self.path = path
        self.images = self._load_images()

    def _load_images(self):
        return [file for file in os.listdir(self.path) if file.endswith((".dm3", ".dm4", ".png"))]

    def load_image(self, file_name):
        return hs.load(os.path.join(self.path, file_name))

    def save_image(self, image, file_name):
        image.save(os.path.join(self.path, "results", file_name))

    def create_results_dir(self):
        os.makedirs(os.path.join(self.path, "results"), exist_ok=True)
