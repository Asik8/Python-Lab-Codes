import math

class Shape:
    def calculate_area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2

def get_dimension(prompt):
    while True:
        try:
            dimension = float(input(prompt))
            if dimension > 0:
                return dimension
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

shape_type = input("Enter the shape type (square, rectangle, circle): ").lower()

if shape_type == "square":
    side = get_dimension("Enter the side length of the square: ")
    shape = Square(side)
elif shape_type == "rectangle":
    length = get_dimension("Enter the length of the rectangle: ")
    width = get_dimension("Enter the width of the rectangle: ")
    shape = Rectangle(length, width)
elif shape_type == "circle":
    radius = get_dimension("Enter the radius of the circle: ")
    shape = Circle(radius)
else:
    print("Invalid shape type.")
    exit()

print("Area of the", shape_type, "is:", shape.calculate_area())
