'''
 Perform the following operation on a list of names:
 1-create a list of 5 names-'Anil','Amol','Aditya','Avi','Alka'
 ->Insert a name 'Anuj' before aditya
 ->Append a name 'Zulu'
 ->Delete 'Avi' from the list
 ->Replace 'Anil' with 'AnilKumar'
'''
my_list = ['Anil', 'Aditya','Amol', 'Avi', 'Alka']
# insert Amol before Aditya
# getting the index of Aditya
i = my_list.index('Aditya')
my_list.insert(i, 'Anju')
# ->Append a name 'Zulu'
my_list.append("Zulu")
print(my_list)
my_list.remove('Avi')
print(my_list)
# Replace Anil with Anilkumar
# getting the index of Anil in list
i = my_list.index('Anil')
my_list[i] = "Anilkumar"
print(my_list)
# sort the list
my_list.sort()
print(my_list)
# reverse the sorted list
my_list.reverse()
print(my_list)
