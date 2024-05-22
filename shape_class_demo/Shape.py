# Shape.py
# Shape is a superclass or parent class for the derived classes (aka subclasses)
class Shape:
    # Static member variables (shared by all shape and derivatives)
    TYPE_CIRCLE = 1
    TYPE_SQUARE = 2
    TYPE_RECTANGLE = 3
    TYPE_TRIANGLE = 4
    count = 0

    # Constructor method
    def __init__(self, type):
        self.type = type

# Circle is derived from Shape; Circle is a subclass of Shape <-- Inheritance
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(Shape.TYPE_CIRCLE)
        self.radius = radius
        Shape.count += 1

    def area(self):
        return self.radius ** 2 * 3.14

# Square is derived from Shape
class Square(Shape):
    def __init__(self, side):
        super().__init__(Shape.TYPE_SQUARE)
        self.side = side
        Shape.count += 1

    def area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(Shape.TYPE_RECTANGLE)
        self.length = length
        self.width = width
        Shape.count += 1

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(Shape.TYPE_TRIANGLE)
        self.base = base
        self.height = height
        Shape.count += 1

    def area(self):
        return self.base * self.height / 2

