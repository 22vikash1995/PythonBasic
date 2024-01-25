"""
Write a program to remove an empty tuple from the list of tuples
"""
tpl = [('vikash',), ('',), ('Vinay',),('',), ('vicky',),('',), ('viswas',)]
tpl1=()
for index ,n in enumerate(tpl):
    length=len(n[0])
    if length==0:
        pass
    else:
        tpl1=tpl1+n
print(tpl1)


