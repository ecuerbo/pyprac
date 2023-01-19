def add(x,y):
    print(x+y)
def subtract(x,y):
    print(x-y)
def multiply(x,y):
    print(x*y)
def divide(x,y):
    print(x/y)
print("Enter two number")
n1 = input()
n2 = input()
print("Enter the opeartion +,-,*,/ ")
op=input()
if op=='+':
    add(int(n1),int(n2))
elif op=='-':
    subtract(int(n1),int(n2))
elif op=='':
    multiply(int(n1),int(n2))
elif op=='/':
    divide(int(n1),int(n2))
else:
    print(" Invalid entry")