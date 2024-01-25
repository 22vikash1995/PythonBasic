"""
Write the python program to perform the following operation:
1.Pack first 10multiples of 10 into a tuple
2.Unpack the tuple into 10 distinct variables,each holding one value.
3.Unpack the tuple such that first value gets stored in variable x
   and last value in y,and all values in between into disposable variable _.
4.Unpack the tuple such that the first value gets stored in variable i
    and last value in j, and all values in between into a single disposable variable _ .
"""

tpl = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
a, b, c, d, e, f, g, h, i, j = tpl
print(tpl)
x, _, _, _, _, _, _, _, _, y = tpl
print(x, y,_)
i, *_, j = tpl
print(i, j, _)
print(tpl)
