import numpy as np
from PIL import Image


class Canvas:
    """
    Creates a canvas object with a coloured background which allows shapes to be drawn on it
    """

    def __init__(self, height, width, colour):
        """
        :param height: height of canvas in pixels
        :type height: int
        :param width: width of canvas in pixels
        :type width: int
        :param colour: colour of background of canvas
        :type colour: colour.Colour
        """

        self.height = height
        self.width = width
        self.colour = colour

        # Create array representing pixels, each with the background colour
        self.matrix = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.matrix[:] = self.colour.rgb_values

    def make(self, filepath):
        """
        Creates image from canvas in it's current state, including shapes drawn on it

        :param filepath: path in current directory together with name and file-type
        :type filepath: str
        """

        img = Image.fromarray(self.matrix, "RGB")
        img.save(filepath)
