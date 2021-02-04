snowing = input('Is it snowing? Enter True or False: ')
temp = float(input('Enter temperature: '))
if temp < 0:
    print('It is freezing')
    if snowing:
        print('Put on boots')
    print('Time for Hot Chocolate')
print('Bye')