# 将列表进行处理，变成字符串，单词间用空格分隔，但最后一个单词与句号间不能有空格
arr = ["The", "fox", "jumped", "over", "the", "fence", "."]
result = " ".join(arr[:6]) + arr[6]
print(result)