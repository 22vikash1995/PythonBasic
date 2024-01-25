print("List Example.....")
fruits = ['Banana', 'Apple', 'Orange', 34, False]
print("List is:\n", fruits)
print(len(fruits))
print(fruits[0])
print(type(fruits))
# creating list with list constructor i.e list()
list1 = list(('vikash', 'vicky', 'vivek', 'sheetal', 'sahil'))
print(list1[-1])
# merge two list items
fruitItem = ['banana', 'watermelon', 'guava', 'apple']
vegItem = ['Potato', 'brinjal', 'radish', 'tomato']
fruitItem.extend(vegItem)
print(fruitItem)
for item in range(len(fruitItem)):
    print(fruitItem[item])

if 'banana' in fruitItem:
    print("Yes banana is existed in list at:", fruitItem[0])

print("Items showing range")
for i in range(len(fruitItem)):
    print(fruitItem[i])
# for loop in short
print("For loop in short\n")
[print(item) for item in fruitItem]

# create new list from existing list
student = ['vikash', 'vicky', 'vishal', 'vinit', 'Sahil', 'Sheetal', 'Shital', 'Shivam', 'Shivani', 'Shivangi']
newList = []
for name in student:
    if 'vi' in name:
        newList.append(name)

print(newList)

# print new list using
newItemList = [name for name in student if "v" in name]
print(newItemList)
student.sort()
print(student)

# copy list to another using copy method
myList = student.copy()
print("Copied list items are:\n", myList)

# copying the list items using list() method
myNewList=list(student)
print("copied items using list method:\n",newItemList)
# join two list by using '+' operator
mergedList=myList+myNewList
print("join list by '+' operator\n",mergedList)

# join two lists using append methods
list1=['a','b','c','d']
list2=[1,2,3,4]
for item in list2:
    list1.append(item)
print("join list by using 'append()'\n",list1)
# join two list by using extends()
list1.extend(list2)
print("join list by using 'extend()'\n",list1)
