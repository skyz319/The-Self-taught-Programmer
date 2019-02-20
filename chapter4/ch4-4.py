"""
编写一个带两个函数的程序。 第一个函数应接受一个整数为参数， 并返回该整数除以 2 的值。
第二个函数应接受一个整数作为参数，并返回该整数乘以 4 的值。调用第一个函数，将结果保存至变量，
并将变量作为参数传递给第二个函数
"""

def func(x):
    """
    接受一个整数，并返回该整数除以2的值
    :param x:
    :return: 整除结果
    """
    return x // 2

def func2(x):
    """
    接受一个整数，并返回该整数除以2的值
    :param x:
    :return: 浮点结果
    """
    return x / 2

# print("整除结果:", func(10))
# print("浮点结果:", func2(9))

def func3(x):
    """
    返回x除以4的值
    :param x:
    :return:
    """
    return x // 4

a = func(80)
print(func3(a))