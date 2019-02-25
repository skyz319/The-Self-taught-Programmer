# 对串进行切片，只保留逗号前的字符
str = "It was bright cold day in April, and eht clocks wrer striking thirteen."
index = str.find(",")
result = str[:index]
print(result)