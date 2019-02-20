# 创建一个由元组构成的列表，每个元组包含居住或旅游过的城市的经纬度
cityList1 = [
    ("ChengDu", 30.5895656853, 104.0365147591),
    ("ChongQing", 29.5647100000, 106.5507300000),
    ("WeiZhou", 21.0493388750, 109.1431617737),
]

print("CityList1: ", cityList1)

cityList2 = []
chengDu = ("ChengDu", 30.5895656853, 104.0365147591)
chongQing = ("ChongQing", 29.5647100000, 106.5507300000)
weiZhou = ("WeiZhou", 21.0493388750, 109.1431617737)

cityList2.append(chengDu)
cityList2.append(chongQing)
cityList2.append(weiZhou)

print("CityList2: ", cityList2)