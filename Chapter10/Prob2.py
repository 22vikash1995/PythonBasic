"""
What will be the output of the following program?
a={10,20,30,40,50,60,70}
b{33,44,51,10,20,50,30,33}
"""
a = {10, 20, 30, 40, 50, 60, 70}
b = {33, 44, 51, 10, 20, 50, 30, 33}
# print (a|b)
print("a|b =", a | b)
print("a&b", a & b)
print("a-b", a - b)
print("b-a", b - a)
print("a^b", a ^ b)
print("a>=b", a >= b)
print("a<=b", a <= b)
