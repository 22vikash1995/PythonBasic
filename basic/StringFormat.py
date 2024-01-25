mystr = "I am vikash. my age is {} years"
print(mystr.format(26.6))

price = 78.668956
txt = "The price is {:.2f}"
print(txt.format(price))

try:
    f = open("hello.txt")
    try:
        f.read()
    except:
        print("Error in file writing")
except:
    print("Something wrong in file Opening")
