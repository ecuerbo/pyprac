# find the largest number in a list without using built-in functions
numbers = [3,8,1,7,2,9,5,4,467]
big = numbers[0]
for i in range(len(numbers)):
    if ((numbers[i])>big):
        big = numbers[i]
        position = i
print("The largest element is ", big, " which is found at position ", position)
