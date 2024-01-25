'''
write a program to maintain names and cell numbers of 4 persons and then print them systematically in a
tabular form.
'''

'''
contacts = {
    'Vikash': 8810271698,
    'Vivek': 6204123875,
    'Sheetal': 9540556468,
    'Rohit': 88102475865
}

for item, cellno in contacts.items():
    print(f'{item:10}:{cellno:10d}')

print("Square of numbers are:")
for n in range(1,41,1):
    print(f'square of {n} is:-> {n**2:<5}')
    '''

'''
 below example is for
'''

'''
n = input()
n = int(n)
if n % 2 != 0:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")

'''

print("Square of numbers are:\n")
for n in range(1,21):
    print(f'{n:>5}->{n**3:>10}')