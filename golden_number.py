year = int(input("enter year today: "))
goldnum = (year+1)%19
if goldnum == 0:
    print("This year ", year, ", years since the birth of our Lord, ")
    print("The golden number is ", 19, ".")
else:
    print("This year ", year, ", years since the birth of our Lord, ")
    print("The golden number is ", goldnum, ".")
