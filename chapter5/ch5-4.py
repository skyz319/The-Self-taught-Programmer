me = {
    "height": 176,
    "likeColor": "Black",
    "author": "J.K. rowling"
}

key = input("type search key: ")
if key in me:
    print("", key, "is ", me[key])
else:
    print("key: ", key, "is not find")
