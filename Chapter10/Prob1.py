"""
A set contains names which begins either with A or with B .write a program to
separate out the names into two sets, one containing names beginning with A and
another containing names beginning with B.
"""
my_set={'Abhishek','Bikas','Akash','Bhikhari','Ashish','Ashiq','Bechu','Ashok','Bhopal'}
# Creating an empty set A for A-type item
setA=set()
# Creating an empty set B for B-type item
setB=set()
for item in my_set:
    if item.startswith('A'):
        setA.add(item)
    else:
        setB.add(item)
print(my_set)
print(setA)
print(setB)