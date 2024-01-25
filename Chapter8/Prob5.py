"""
write a program to generate and store in a list 20 random numbers
in the range 10 to 100. From the list delete all those number which
have value between 20 and 50. Print the remaining list.
"""
import random

# Creating an empty list
my_list = []
# generating random number between 10 and 100
i = 1
while i <= 20:
    num = random.randint(10, 100)
    my_list.append(num)
    i += 1
print(my_list)

# removing number having value between10 and 50
for num in my_list:
    if num >20 and num < 50:
        my_list.remove(num)
print(my_list)
my_list.sort()
print(my_list)
