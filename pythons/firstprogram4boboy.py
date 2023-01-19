number1 = int(input("Please enter a number : "))
operator = str(input("Enter operator : "))
number2 = int(input("Please enter another number : "))

if operator=="+":
    add = number1 + number2
    print("Sum of number1 and number 2 is ", add)
elif operator=="-":
    sub = number1-number2
    print("Difference of number1 and  2 is", sub)
else:
    print("yak kahibayo")