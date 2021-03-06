from Circle import Circle
from Rectangle import Rectangle
from Triangle import Triangle
from Square import Square
circle = Circle(12)
square = Square(12)
triangle = Triangle(2, 3, 4)
rectangle = Rectangle(2, 5)
print("Rectangle area - " + str(rectangle.get_area()))
print("Rectangle perimeter - " + str(rectangle.get_perimeter()))
print("Triangle area - " + str(round(triangle.get_area(), 2)))
print("Triange perimeter - " + str(triangle.get_perimeter()))
print("Circle area - " + str(round(circle.get_area())))
print("Circle perimeter - " + str(circle.get_perimeter()))
print("Square area - " + str(square.get_area()))
print("Square perimeter - " + str(square.get_perimeter()))
