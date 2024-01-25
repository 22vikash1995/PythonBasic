def my_function(fName, lName):
    print(fName, lName)


my_function("Vikash", "Kumar")


# taking tuple as argument in function
def my_fun(*tuple):
    print(tuple)


my_fun("Vikash", "Vicky", "Vijay")


# Arbitrary argument **args
def myFun(**students):
    print(students["LastName"])


myFun(FirstName="Vikash", LastName="Kumar")


# Function with default argument
def fun_default(author="Vikash"):
    print("Autghor name is:" + author)


fun_default("Vicky")
fun_default("Viswas")
fun_default("Suman")
fun_default()

# passing the list of items in function
fruits = ['Apple', 'Banana', 'PineApple', 'Pomegranate']


def fun_fruits(item):
    for item in fruits:
        print(item)


fun_fruits(fruits)


# function with return value
def add(a, b):
    return a + b


print(add(4, 5))
