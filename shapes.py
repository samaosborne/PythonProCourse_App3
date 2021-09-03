def distance(x1, y1, x2, y2):
    """
    Gives the distance between two points, (x1, y1) and (x2, y2), in an array

    :param x1: x co-ordinate of first point
    :type x1: int
    :param y1: y co-ordinate of second point
    :type y1: int
    :param x2: x co-ordinate of first point
    :type x2: int
    :param y2: y co-ordinate of second point
    :type y2: int
    :return: distance between two points
    :rtype: float
    """

    return ((x2 - x1 + 0.5)**2 + (y2 - y1 + 0.5)**2) ** 0.5


class Rectangle:
    """
    Creates a coloured rectangle that can be drawn on a canvas object
    """

    def __init__(self, x, y, height, width, colour):
        """
        :param x: vertical position of rectangle from top of canvas in pixels
        :type x: int
        :param y: horizontal position of rectangle from left of canvas in pixels
        :type y: int
        :param height: height of rectangle in pixels
        :type height: int
        :param width: width of rectangle in pixels
        :type width: int
        :param colour: colour of rectangle
        :type colour: colour.Colour
        """

        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.colour = colour

    def draw(self, canvas):
        """
        Draws the rectangle onto a canvas

        :param canvas: canvas object on which to draw the rectangle
        :type canvas: canvas.Canvas
        """

        canvas.matrix[self.x:self.x+self.height, self.y:self.y+self.width] = self.colour.rgb_values


class Square:
    """
    Creates a coloured square that can be drawn on a canvas object
    """

    def __init__(self, x, y, side, colour):
        """
        :param x: vertical position of square from top of canvas in pixels
        :type x: int
        :param y: horizontal position of square from left of canvas in pixels
        :type y: int
        :param side: side length of square in pixels
        :type side: int
        :param colour: colour of square
        :type colour: colour.Colour
        """

        self.x = x
        self.y = y
        self.side = side
        self.colour = colour

    def draw(self, canvas):
        """
        Draws the square onto a canvas

        :param canvas: canvas object on which to draw the square
        :type canvas: canvas.Canvas
        """

        canvas.matrix[self.x:self.x+self.side, self.y:self.y+self.side] = self.colour.rgb_values


class Circle:
    """
    Creates a coloured circle that can be drawn on a canvas object
    """

    def __init__(self, x, y, radius, colour):
        """
        :param x: vertical position of centre of circle from top of canvas in pixels
        :type x: int
        :param y: horizontal position of centre of circle from left of canvas in pixels
        :type y: int
        :param radius: radius of circle in pixels
        :type radius: int
        :param colour: colour of circle
        :type colour: colour.Colour
        """

        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour

    def draw(self, canvas):
        """
        Draws the circle onto a canvas

        :param canvas: canvas object on which to draw the circle
        :type canvas: canvas.Canvas
        """

        canvas.matrix[self.x, self.y-self.radius:self.y+self.radius + 1] = self.colour.rgb_values
        canvas.matrix[self.x-self.radius:self.x+self.radius + 1, self.y] = self.colour.rgb_values
        for i in range(self.radius, 0, -1):
            for j in range(self.radius, 0, -1):
                if distance(self.x, self.y, self.x-i, self.y-j) <= self.radius:
                    canvas.matrix[self.x-i, self.y-j:self.y+j + 1] = self.colour.rgb_values
                    canvas.matrix[self.x+i, self.y-j:self.y+j + 1] = self.colour.rgb_values
                    break
