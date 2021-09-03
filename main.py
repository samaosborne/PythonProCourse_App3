from canvas import Canvas
from colour import Colour
from shapes import Rectangle, Square, Circle
import random

# Create canvas of user given dimensions and colour
canvas_height = int(input("Enter canvas height (all sizes are in pixels): "))
canvas_width = int(input("Enter canvas width: "))
canvas_colour_raw = input("Enter canvas background colour (hex code, HTML names or RGB values separated by spaces): ")
canvas_colour = Colour(canvas_colour_raw)

canvas = Canvas(canvas_height, canvas_width, canvas_colour)

shapes = {"r": "rectangle", "s": "square", "c": "circle"}

draw = input("Would you like to (d)raw shapes or add them (r)andomly? ")
if draw == "d":
    # Draw any number of shapes of given dimensions, position and colour
    while True:
        shape_type = input("Would you like to draw a (r)ectangle, (s)quare or (c)ircle? ").lower()
        x = int(input(f"How far down should the {shapes[shape_type]} be? "))
        y = int(input(f"How far right should the {shapes[shape_type]} be? "))
        shape_colour_raw = input(f"What colour should the {shapes[shape_type]} be? ")
        shape_colour = Colour(shape_colour_raw)
        if shape_type == "r":
            rect_height = int(input("How tall should the rectangle be? "))
            rect_width = int(input("How wide should the rectangle be? "))
            shape = Rectangle(x, y, rect_height, rect_width, shape_colour)
        elif shape_type == "s":
            square_side = int(input("How long should the sides of the square be? "))
            shape = Square(x, y, square_side, shape_colour)
        else:
            circle_radius = int(input("What should the radius of the circle be? "))
            shape = Circle(x, y, circle_radius, shape_colour)
        shape.draw(canvas)
        more = input("Would you like to add another shape? (y)es or (n)o: ").lower()
        if more == "n":
            break
else:
    number_shapes = int(input("How many shapes should be randomly drawn? "))
    for _ in range(number_shapes):
        shape_type = random.choice(list(shapes.keys()))
        x = random.choice(range(canvas.height))
        y = random.choice(range(canvas.width))
        shape_colour = Colour(" ".join(str(random.choice(range(256))) for _ in range(3)))
        if shape_type == "r":
            rect_height = random.choice(range(1, canvas.height-y+1))
            rect_width = random.choice(range(1, canvas.width-x+1))
            shape = Rectangle(x, y, rect_height, rect_width, shape_colour)
        elif shape_type == "s":
            square_side = random.choice(range(1, min(canvas.height-y, canvas.width-x)+1))
            shape = Square(x, y, square_side, shape_colour)
        else:
            circle_radius = random.choice(range(min(x, canvas.height-x, y, canvas.width-y)))
            shape = Circle(x, y, circle_radius, shape_colour)
        shape.draw(canvas)

name = input("What would you like to call your picture? ")
canvas.make(f"files/{name}.png")
