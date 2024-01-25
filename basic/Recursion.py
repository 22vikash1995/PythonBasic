def my_fun(k):
    if(k>0):
        result = k+my_fun(k - 1)
        print(result)
    else:
        result=0
    return result


print("Recursion result is:")
my_fun(4)
