from abc import ABC, abstractmethod

# 부모 클래스: 도형 (추상 클래스)
class Shape (ABC) :
    @abstractmethod 
    def get_size(self):
        pass

class Rectangle(Shape) :
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def get_size(self):
        return self. height * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def get_size(self):
        return 3.14 * self. radius