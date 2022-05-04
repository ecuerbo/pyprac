from http.client import PRECONDITION_REQUIRED
from re import X
from tkinter import N


year = int(input("Please enter year after 2022: "))
x = (year-1986)/75

if x>1:
    next = 1986+75*x
    print("Next appearance of Halley's comet will be on: ",next)
else:
    print("Next appearance of Halleys comet will be on 2061. ")