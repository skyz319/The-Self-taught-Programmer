
# 打开文件
st = open("a.txt", "w")
print(st)
# 写入内容
st.write("aaaaaaaaaaaaaaaaaaaaaa")
# 使用open后，需显示使用close进行关闭
st.close()

# 自动关闭文件
with open("a.txt", "w") as f:
    f.write("bbbbbbbbbbbbbbbbbbbb")

# 读取文件
with open("a.txt", "r") as f:
    print(f.read())

import csv
# 写csv文件
with open("st.csv", "w") as f:
    # 参数：文件对象， 分隔符
    w = csv.writer(f, delimiter=",")

    w.writerow(["one",
                "two",
                "three"])

    w.writerow(["four",
                "five",
                "six"])

# 读csv文件
with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
