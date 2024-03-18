# / Imports /

from random import randrange
from colorama import *          # pip install colorama
just_fix_windows_console()      # Pour le CMD de windows

# / Variables / 

index = 0
picked_number = 0
sum = 0

# / Main Loop /

while picked_number != 6:
    index +=1
    picked_number = randrange(1,7)
    sum += picked_number
    print(f"Le Lancé n° {Back.YELLOW} {index} {Back.RESET} vaut {Back.GREEN} {picked_number} {Back.RESET} \n -> la somme totale de tout les lancé est de {Back.CYAN} {sum} {Back.RESET} \n ")
