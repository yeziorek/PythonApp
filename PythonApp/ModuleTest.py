import mods
from functions import iterator

print('Select function:')
print('1 - Class Iteration For')
print('2 - Module data read test')
x = int(input())
print(' You have selected ' + str(x))

if x == 1:
    print(iterator())
elif x == 2:
    mods.greeting("Jonathan")
else:
    print('Incorrect number or you have fucked up')