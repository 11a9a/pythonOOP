# Using Abstract Base Classes to enforce class constraints


from abc import ABC, abstractmethod
import math

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return math.pi * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side ** 2


c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
