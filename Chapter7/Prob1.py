'''
1. write a program to receive radius of a circle, length and breadth of a rectangle in one call to input()
method. Calculate and print the circumference of the circle and perimeter of rectangle.
'''
import math
import math as mth

radius, length, breadth = input("Enter the radius of circle, length and breadth of rectangle \n").split()
radius = int(radius)
length = int(length)
breadth = int(breadth)
circumference_of_circle = 2 * math.pi * radius
circumference_of_rectangle = 2 * (length + breadth)
area_of_circle = mth.pi * radius * radius
area_of_rectangle = length * breadth
print("Area of Circle is:\n", area_of_circle)
print("Area of Rectangle is:\n", area_of_rectangle)
print("Circumference of Circle is:\n", circumference_of_circle)
print("Circumference of Rectangle is:\n", circumference_of_rectangle)
