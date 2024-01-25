try:
    f = open("List.py")
    try:
        f.write("hello vikash this written by me")
    except:
        print("Something went wrong while writing the file")
    finally:
        f.close()
except:
    print("Something went wrong white opening the file")

# generate exception
# int python exception is throw by using 'raise' keyword
# x = -1
# if x < 0:
#     raise Exception("Number can not be less than zero")

x = "hello"
if not type(x) is int:
    raise TypeError("This is not an integer value")
