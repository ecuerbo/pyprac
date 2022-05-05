#Area of a rectangle
def rect():
    length = int(input("Length: "))
    width = int(input("Width: "))
    if (length<=0 or width<=0):
        print("One of the sides is 0 or negative. Try again.")
    else:
        area = length*width
        print("The area is ", area)
rect()