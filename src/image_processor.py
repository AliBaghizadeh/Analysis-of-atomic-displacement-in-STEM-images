from scipy.ndimage import rotate
import hyperspy.api as hs
import cv2

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def rotate(self, angle):
        self.image.map(rotate, angle=angle, reshape=False, output_dtype="uint8")

    def crop(self, roi_params=None):
        if roi_params:
            roi = hs.roi.RectangularROI(**roi_params)
            cropped_image = roi.interactive(self.image)
        else:
            self.image.plot()
            roi = hs.roi.RectangularROI()
            cropped_image = roi.interactive(self.image)
        return cropped_image

    def super_resolve(self, scale_factor=2):
        image_data = self.image.data
        height, width = image_data.shape
        new_dimensions = (width * scale_factor, height * scale_factor)
        super_res_image = cv2.resize(image_data, new_dimensions, interpolation=cv2.INTER_CUBIC)
        self.image.data = super_res_image

    def plot(self):
        self.image.plot()
