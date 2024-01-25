"""
In the following tuple: ('F','i','a','b','b','e','r','g','a','s','t','e','d')
perform the following operation:
1.Add ! at the end of the tuple
2.Convert a tuple to string
3.Extract 'b','b' from the tuple
4.find out the occurrence of 'e' in the tuple
5.Check whether 'r' exist in the tuple
6.convert a tuple to the list
7.delete character 'b','b','e','r'  from the list
"""
tpl = ('F', 'i', 'a', 'b', 'b', 'e', 'r', 'g', 'a', 's', 't', 'e', 'd')
# 1.add ! at the end of the tuple
tpl1 = ()
tpl = tpl + ('!',)
print(tpl)
# 2.Convert a tuple to string
s = ''.join(tpl)
print(s)
# Count number of elements in list
e_size = tpl.count('e')
print(e_size)
# Whether r exists in tuple
print('r' in tpl)
# Convert the tuple to list
lst = list(tpl)
print(lst)
# delete character 'b','b','e','r'  from the list
tpl=tpl[:3]+tpl[7:]
print(tpl)
