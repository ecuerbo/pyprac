'''Calculate the Factorial of a Number
Write a program that can find the factorial of any given number. For example, find
the factorial of the number 5 (often written as 5!) which is 1 * 2 * 3 * 4 * 5 and
equals 120.
The factorial is not defined for negative numbers and the factorial of Zero is 1;
that is 0! = 1.
Your program should take as input an integer from the user (you can reuse your
logic from the last chapter to verify that they have entered a positive integer value
using isnumeric()).
You should
1. If the number is less than Zero return with an error message.
2. Check to see if the number is Zero—if it is then the answer is 1—print this out.
3. Otherwise use a loop to generate the result and print it out.

number = input('Please input the number:')

if number.isnumeric():
    num = int(number)

    if num == 0:
        # Termination criteria
        print('0! factorial is 1')
    else:
        # Recursive element
        factorial = 1
        for i in range(1, num + 1):
            factorial = factorial * i
        print(number + '! factorial is', str(factorial))

else:
    print('Not an integer number')

'''

number = input("please enter a number: ")
if number.isnumeric():
    num = int(number)

    if num == 0:
        print('0! factorial is 1')
    else:
        factorial = 1
        for i in range(1, num+ 1):
            factorial = factorial * i
    print(number, '! factorial is', str(factorial))
else:
    print("not an integer number!")
