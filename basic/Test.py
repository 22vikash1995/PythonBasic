# Write a program to accept radius , length and breadth of rectangle in single input function
import math as mth

radius, length, breadth = input("Enter the radius, length,breadth\n").split()
circle_area = (mth.pi) * int(radius) * int(radius)
rectangle_area = int(length) * int(breadth)
print("Area of circle is \n:", circle_area)
print("Area of rectangle is \n:", rectangle_area)
