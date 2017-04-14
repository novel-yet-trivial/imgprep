import skimage
import skimage.measure as measure
from matplotlib import pyplot as plt


class BoxFinder(object):
    """
    This object takes an RGB image as an input and then tries to detect a red box located in it.

    Params-  image_path: this is the path to the RGB image

    function __init__(self,img_path): This function reads the image, thresholds the grayscaled img, attempts to find
        the largest contoguous contour with a marching squares algorithm, and then passes the coordinate of the square
        (the (x,y) in pixels of the top-right corner, and also passes the dimensions of the square in pixels.

    function return_ROI(self): This function simply returns the coordinates of the box and its dimensions
    """
    def __init__(self,image_path, threshold=150):
        self.img_path = image_path

        img = plt.imread(self.img_path)  # Read the path
        img_red_thresh = img[:, :, 0] > threshold  # Find all pixels greater than threshold (arbitrary)
        img_contour = measure.find_contours(img_red_thresh, 0, fully_connected='high')  # Marching squares

        i = [len(x) for x in img_contour].index(max([len(x) for x in img_contour]))  # Returns index of biggest contour

        # Instantiates the largest x- and y-coordinates for each coordinate in the contour
        x_max = 0
        y_max = 0
        x_min = img_contour[i][0][0]
        y_min = img_contour[i][0][0]

        # This iteratively picks out the max and min values and assigns them
        for point in img_contour[i]:
            if point[0] > x_max:
                x_max = point[0]
            if point[0] < x_min:
                x_min = point[0]
            if point[1] > y_max:
                y_max = point[1]
            if point[1] < y_min:
                y_min = point[1]

        box_dim = (x_max - x_min, y_max - y_min)

        self.coordinate = (x_min, y_min)
        self.box_dim = box_dim

    def return_ROI(self):
        return self.coordinate, self.box_dim