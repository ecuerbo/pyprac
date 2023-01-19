#to display the sum of n numbers using a list

numbers=[]
num = int(input('How many numbers: '))
for n in range(num):
    x = float(input("Enter number: "))
    numbers.append(x)
print("Sum of numbers in the given list is : ", round(sum(numbers), 2))