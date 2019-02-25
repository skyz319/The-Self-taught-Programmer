# 打印列表中的每个元素
arr = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for i, v in enumerate(arr):
    print("index: %s, value: %s" %(i, v))

print("-----------------")

for v in arr:
    print(v)