'''
def print_msg():
    print("hello world!")

print_msg()


def print_my_msg(msg):
    print(msg)
print("GO HOME!")
print("i'm done with shiiit")



def square(n):
    return n*n

square( 879)

# Store result from square in a variable
result = square( 4)
print(result)
# Send the result from square immediately to another function
print(square( 5))
# Use the result returned from square in a conditional expression
if square(3) < 15:
    print(' Still less than 15 ')

def swap(a, b):
    return b, a

result = swap(3, 6)
print(result)
a = 2
b = 3
x, y = swap(a, b)
print(x, ',', y)

def greeter(name,message = 'Live Long and Prosper'):
    print('Welcome', name, '-', message)

greeter("Elbon")
greeter("Elbon", "go away")

def greeter(name,
        title = 'Dr',
        prompt = 'Welcome',
        message = 'Live Long and Prosper'):
    print(prompt, title, name, '-', message)

greeter(message = 'We like Python too.', name = 'So')

'''
def greeter(*args):
    for name in args:
        print('Welcome', name, '!')
greeter('John', 'Denise', 'Phoebe', 'Adam', 'Gryff', 'Jasmine')