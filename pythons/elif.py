savings =float(input('Enter how much you have in savings: ')) 
if savings == 0 :
    print("Sorry no savings")
elif savings < 500:
    print('Well done')
elif savings < 1000:
    print('Thats a tidy sum ')
elif savings < 10000:
    print('Welcome Sir!')
else:
    print('Thank you')