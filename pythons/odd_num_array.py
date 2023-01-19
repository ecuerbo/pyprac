numbers = [8,3,1,6,2,4,5,9]
count = 0
for i in range(len(numbers)):
    if(numbers[i]%2!=0):
        count = count+1
print("The number of odd numbers in the list are: ", count)