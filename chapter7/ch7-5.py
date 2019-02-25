# 将列表中各项相乘，并放入新列表
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]

result1 = []

for i in list1:
    for j in list2:
        result1.append(i * j)

print(result1)

print("------------------")

result2 = []
for i1, v1 in enumerate(list1):
    for i2, v2 in enumerate(list2):
        if i1 == i2:
            result2.append(v1 * v2)
print(result2)