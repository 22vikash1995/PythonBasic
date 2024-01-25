# Tuple is used to store multiple items to a single list.its items are stored in small bracket i.e '()'.
# A tuple is collection which is ordered and unchangeable.It allows duplicate values.
tuples = ('vikash', "vicky", 'vinay')
print("This is tuple's items\n", tuples)
# tuple length
print("Length of tuple is:", len(tuples))
# tuple with single item
singleTuple = ('Vikash',)
print("Tuple having only one item:", singleTuple)
# tuple having single item without 'comma' at end of item , is not consider as tuple by python.
tuples1 = ("Vikas")
print(tuples1)
# Creating tuple with tuple constructor
newTuple = tuple(('vikas', 'vicky', 'vinay', 'vishwas'))
print("Tuple with tuple constructor \n", newTuple)
print(newTuple[1])
# Unpacking the tuple
myTuple=('vikash','vicky','viswas','vicky')
(firstItem,secondItem,*thirdItem)=myTuple
print("This is third item: ",thirdItem)
print("This is first item: ",firstItem)
print("This is second item: ",secondItem)
print(myTuple.count("vicky"))
print(myTuple.index("vicky"))