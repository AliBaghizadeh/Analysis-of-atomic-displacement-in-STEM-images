from scipy.ndimage import rotate
import hyperspy.api as hs
import cv2

class ImageProcessor:
    def __init__(self, image):
        """
        Initialize with an image object for processing.

        Parameters:
            image (hyperspy.Signal): The image to process.
        """
        self.image = image

    def rotate(self, angle):
        """
        Rotate the image by a specified angle.

        Parameters:
            angle (float): The angle to rotate the image, in degrees.
        """
        self.image.map(rotate, angle=angle, reshape=False, output_dtype="uint8")

    def crop(self, roi_params=None):
        """
        Crop the image interactively or based on specified ROI parameters.

        Parameters:
            roi_params (dict, optional): Dictionary specifying the rectangular ROI boundaries
                                         (e.g., {'left': x1, 'right': x2, 'top': y1, 'bottom': y2}).

        Returns:
            hyperspy.Signal: Cropped image as a HyperSpy signal.
        """
        if roi_params:
            roi = hs.roi.RectangularROI(**roi_params)
            cropped_image = roi.interactive(self.image)
        else:
            self.image.plot()
            roi = hs.roi.RectangularROI()
            cropped_image = roi.interactive(self.image)
        return cropped_image

    def super_resolve(self, scale_factor=2):
        """
        Enhance image resolution using cubic interpolation.

        Parameters:
            scale_factor (int): The factor by which to upscale the image. Default is 2.
        """
        image_data = self.image.data
        height, width = image_data.shape
        new_dimensions = (width * scale_factor, height * scale_factor)
        super_res_image = cv2.resize(image_data, new_dimensions, interpolation=cv2.INTER_CUBIC)
        self.image.data = super_res_image

    def plot(self):
        """
        Plot the image using HyperSpy's plotting functionality.
        """
        self.image.plot()
