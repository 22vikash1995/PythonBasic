x = lambda a, b: a + b
print(x(6, 5))


# lambda in function
def lambFun(n):
    return lambda a: a * n


myLambFun = lambFun(5)
print(myLambFun(6))
