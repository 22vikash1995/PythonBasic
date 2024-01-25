'''
Create a list of five odd numbers
2.create a list of five even numbers
3.combine the both list
4.add prime numbers 11,17,29,at the beginning of the combined list
5.Reports how many elements are present in th list
6.Replace last 3 numbers in the list with 100,200,300
7.Delete al the numbers in the list
8.Delete the list
'''
# 1.create odd num list
odd_num = [3, 5, 7, 9, 13]
# 2.create even num list
even_num = [2, 4, 6, 8, 10]
# 3.combine the both list
my_list = odd_num.__add__(even_num)
print(my_list)
# 4.add nums 11,17,29 at the beginning of the list
num_list = [11, 17, 29]
final_list = num_list.__add__(my_list)
print(final_list)
# 5.Reports how many elements in the list
size=len(final_list)
print(size)
# 6. Replace last three numbers in the list with 100,200,300
'''
    First way:
    final_list[-1] = 300
    final_list[-2] = 200
    final_list[-3] = 100
    print(final_list)

'''
# second way to replacing the last items in the list
final_list[size-3:size]=[100,200,300]
print(final_list)
# 7.Delete all the items from the list
final_list.clear()
print(final_list)
# 8.Delete the list
'''' 
del final_list
print(final_list)
'''
