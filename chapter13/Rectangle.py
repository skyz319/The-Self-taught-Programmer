from chapter13.Shape import *

class Rectangle(Shape):
    def __init__(self, length, wide):
        self.length = length
        self.wide = wide

    def calculate_perimeter(self):
        """
        计算周长
        :return: 该图形的周长
        """
        return 2 * (self.length + self.wide)