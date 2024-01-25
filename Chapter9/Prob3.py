"""
A list contains names of boys and girls as its elements. Boy's names are stored as a tuple
 and girls name are stored as tuple. write python program to find outnumber of boys and girls in the
 list.
"""
my_list = [('Vikash',),( 'Vivek',),( 'Vishwas',),( "Vicky",),( 'Vinay',),('Vijay',), "pooja", 'archana', 'Ambika', 'Amrita', "Ashiq"]
boys = 0
girls = 0
for item in my_list:
    if isinstance(item,tuple):
        boys+=1
    else:
        girls+=1

print('Boys: ',boys)
print('Girls',girls)