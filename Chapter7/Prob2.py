'''
 write a program to receive 3 integers using one input() call. The three integers signify starting value
 ending value and step value for a range. The program should use these values to print the number ,its
 square and its cube, all properly right-aligned and same output is left-aligned.
'''

start, end, step = input("Enter the start, end ,and step value \n").split()
start = int(start)
end = int(end)
step=int(step)
# right aligned
for n in range(start, end, step):
    print(f'{n:>5}{n**2:>4}{n**3:>5}')
print()

for n in range(start,end,step):
    print(f'{n:<5}{n**2:<4}{n**3:<5}')

