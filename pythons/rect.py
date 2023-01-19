'''
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
'''
import sys
def main():
    if len(sys.argv) != 3:
        exit("Needs 2 arguments: width length")

    width = int(sys.argv[1])
    length = int(sys.argv[2])

    if length <= 0:
        exit("length is not positive")

    if width <= 0:
        exit("width is not positive")

    area = length * width
    print('The area is ', area)


main()