"""
A list contains tuples containing roll number ,name, and age of student.
write a python program to gather all the names from the list into another list.
"""
lst=[('101','Vikash',27),('102','Vikas',25),('103','Vicky',26)]
emp=[]
for name in lst:
    emp=emp+[name[1]]

print(emp)