"""
编写一个将字符串转换为 float 对象并返回该结果的函数。使用异常处理来捕获可能发生的异常。
"""

def strToFloat(str):
    """
    将字符串转为float,使用异常来捕获
    :param str:
    :return: float对象
    """
    try:
        float(str)
    except ValueError:
        print("must be number")

strToFloat("abc")