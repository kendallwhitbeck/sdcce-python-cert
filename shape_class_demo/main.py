import Shape

rectangle = Shape.Rectangle(10, 20)
print(rectangle.area())

circle = Shape.Circle(10)
print(circle.area())

square = Shape.Square(10)
print(square.area())

shape4 = Shape.Triangle(10, 5)
print(shape4.area())

print("entering for loop:")
for shape in [rectangle, circle, square]:
    print(shape.area())

# print(Shape.count)

# TODO: why do these return the same count?
print(f"rectangle.count={rectangle.count}")
print(f"circle.count={circle.count}")

print(f"rectangle.type={rectangle.type}")
