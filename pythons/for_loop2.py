'''for i in range(0, 10):
    print(i, ' ', end ='')
    if i % 2 == 1:
        continue
    print('hey its an even number')
    print("we love even numbers")
print("done")

#divisible by 3
for i in range(0, 100):
    print(i, ' ', end = ', ')
    if i % 3 != 0:
        continue
    print('oh yes! its divisible by 3')
print("done")
'''
#for loop with if else
# Only print code if all iterations completed over a list
print('Only print code if all iterations completed')
num = int(input('Enter a number to check for: '))
for i in range(0, 6):
    if i == num:
        break
    print(i, ' ', end='')
else:
    print()
    print('All iterations successful')