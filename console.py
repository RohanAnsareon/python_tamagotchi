import os
import time

from pet import Pet


def clear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

pet = Pet()

clear()
print(pet)

while pet.get_health() > 0:
    time.sleep(2)

    clear()
    pet.spend()

    print(pet)
else:
    clear()
    print('GAME OVER!')
