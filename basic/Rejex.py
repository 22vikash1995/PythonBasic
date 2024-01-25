import re

text = "The rain is Spain"
x = re.search("^The.*Spain$", text)

if x:
    print("Yes! condition matches")
else:
    print("Not match")

try:
    print("this is try block")
except:
    print("This is except block")

try:
    print(z)
except NameError:
    print("Variable z is not defined")
except:
    print("Something went wrong")

try:
    print("This is try block")
except:
    print("This is except block")
finally:
    print("This is finally block")



