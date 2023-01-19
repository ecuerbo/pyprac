'''
You should write a program to calculate prime number starting from 1 up to the
value input by the user.
If the user inputs a number below 2, print an error message.
For any number greater than 2 loop for each integer from 2 to that number and
determine if it can be divided by another number (you will probably need two for
loops for this; one nested inside the other).
For each number that cannot be divided by any other number (that is its a prime
number) print it out.
'''
number=input("please enter a number: ")
if number.isnumeric():
    num = int(number)
    if num <= 2:
        print("number must be greater than 2.")
    else:
        prime_num = True
        for i in range(2, num):
            for j in range(2, i):
                if i % j ==0:
                    prime_num = False
                    break
            if prime_num:
                print('prime number', i )
            prime_num = True       
else:
    print('must be a positive integer.')