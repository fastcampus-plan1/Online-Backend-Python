class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self) :
        return 3.14 * self.radius * self.radius

class Square(Shape) :
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__ (self, base, height):
        self. base = base
        self.height = height
    def area(self) :
        return 0.5 * self. base * self. height

shapes = [Circle(3), Square(4), Triangle(3, 5)]
for shape in shapes:
    print (f"Area of {shape. __class__.__name__} is {shape.area()}")