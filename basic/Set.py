setItem = {'Vikash', 'Vicky', 'viswas', 'vinay', 'Vicky'}
print(setItem)
if "Vicky" in setItem:
    print("Exits!")
else:
    print("item not existed!")
for item in setItem:
    print(item)

# add new item in set
setItem.add("Vishal")
print(setItem)
# merge two sets using update()
set1 = {'a', 'b', 'c', 'd','d'}
set2 = {'e', 'f', 'g', 'h'}
set1.update(set2)
print(set1)
# remove item from set using remove()
set1.remove("a")
print(set1)
# remove item by using discard()
set1.discard("f")
print(set1)
# remove item from set using pop()
set1.pop()
print(set1)
# union()
set1.union(set2)
print(set1)

# print the common item from both sets by using intersection_update()
x={'1','2','3','4'}
y={'1','2','5','6'}
x.intersection_update(y)
print(x)

