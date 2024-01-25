import platform
import datetime

# knowing the which operating system is installed on machine
x = platform.system()  # gives platform name like windows,linux,or dos
print(x)
# Date time
time = datetime.datetime.now()
print("\n", time)
print("Current year is:",time.year)
# %A shows current day name
print("Current Day  is:",time.strftime("%A"))
# %B shows current month name
print("Current Month is:",time.strftime("%B"))
