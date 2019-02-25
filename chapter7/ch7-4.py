
key = 53

while True:
    userInput = input("in put number(0~99):")
    if int(userInput) < 0 or int(userInput) > 99:
        print("Number is error! must be: 0 ~ 99")
        continue
    if int(userInput) == key:
        print("Congratulation! Anser is ", key)
        break
    print("No! try angin!")