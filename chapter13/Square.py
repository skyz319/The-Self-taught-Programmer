from chapter13.Shape import *

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def calculate_perimeter(self):
        return 4 * self.length

    def change_size(self, length):
        tmp = self.length
        try:
            self.length += length
        except ValueError:
            print("invalid number")

        if self.length < 0:
            print("length error, length is recovered!")
            self.length = tmp

    def what_am_i(self):
        print("I am Square shape")