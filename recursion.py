#Python program to print the numbers from a given n till 0 using recursion
def print_till_zero(n):
    if(n==0):
        return
    print(n)
    n=n-1
    print_till_zero(n)
print_till_zero(9)