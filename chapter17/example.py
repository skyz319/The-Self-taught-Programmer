import re

l = "Beautiful is better than ugly."
# IGNORECASE 忽略大小写
matches = re.findall("beautiful", l, re.IGNORECASE)

print(matches)

zen = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
123?341234.sd31324-33
__one__ 
__two__ 
__three__"""

# 匹配开始位置
print("匹配开始位置:")
m1 = re.findall("^If", zen, re.MULTILINE)
print(m1)
# 匹配末尾位置
print("匹配末尾位置:")
m2 = re.findall("idea.$", zen, re.MULTILINE)
print(m2)

# 匹配多个字符
print("匹配多个字符:")
str1 = "Two, too"
m3 = re.findall("t[ow]o", str1, re.IGNORECASE)
print(m3)

# 匹配数字
print("匹配数字:")
m4 = re.findall("\d", zen, re.IGNORECASE)
print(m4)

# 贪婪匹配
print("非贪婪匹配:")
m5 = re.findall("__.*?__", zen)
print(m5)

print("挑战1:")
m6 = re.findall("Dutch", zen)
print(m6)