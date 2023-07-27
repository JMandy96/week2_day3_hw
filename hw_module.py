from math import *

def sqft():
    length = int(input("length: "))
    width = int(input("width: "))
    area = length * width
    return area
print(sqft())

def circumference():
    r=int(input("radius: "))
    circumference = 2*pi*r
    return circumference
print(circumference())