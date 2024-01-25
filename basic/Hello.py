print("Hello world")
a=10
b=20
print("Numbers before swapping are:\n")
print("The value of a is:",a)
print("The Value of is:",b)

a=a+b
b=a-b
a=a-b
print("The Numbers after swapping without using third varribles\n")
print("The value of a is:",a)
print("The Value of b is:",b)

def myFunction():
    name ="Vikash Kumar"
    if(len(name)==0):
        return True
    else:
        return False
    

print(myFunction())    