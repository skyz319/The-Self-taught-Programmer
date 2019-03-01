# coding=utf-8

# Python导入模块的方式有两种：import moudle 和 from moudle import,
# 区别是前者所有导入的东西使用时需要加上模块名限定，而后者不要。

from chapter13.Rectangle import *
import Square

from chapter13.Rider import *
from chapter13.Horse import *

rec = Rectangle(10, 20)
print(rec.calculate_perimeter())
rec.what_am_i()

squ = Square.Square(10)
print(squ.calculate_perimeter())
squ.change_size(15)
print(squ.calculate_perimeter())
squ.change_size(-40)
print(squ.calculate_perimeter())
squ.what_am_i()

print("--------------")

rider = Rider("jack")
rider.riderHorses()
horse1 = Horse("No.1")
horse1.who_am_i()
horse2 = Horse("No.2")
horse3 = Horse("No.3")

rider.horses.append(horse1)
rider.horses.append(horse2)
rider.horses.append(horse3)

rider.riderHorses()


