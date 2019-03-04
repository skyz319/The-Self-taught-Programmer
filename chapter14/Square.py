class Square:
    square_list = []
    def __init__(self, length):
        self.square_list.append(self)
        self.length = length

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.length, self.length, self.length, self.length)

    def isEqual(obj1, obj2):
        print(obj1 is obj2)

sq1 = Square(10)
sq2 = Square(11)
sq3 = Square(12)

print(sq1.square_list)

sq4 = Square(25)
print(sq4)

sq5 = sq4
print("sq5 isEqual sq4 ?\n", Square.isEqual(sq4, sq5))