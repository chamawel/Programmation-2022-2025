# / Imports /

from random import randrange
from colorama import *          # pip install colorama
just_fix_windows_console()      # Pour le CMD de windows

# / Variables / 

index         : int = 1
picked_number : int = randrange(1,7)
sum           : int = picked_number
last_num      : int = picked_number

print(f"Le Lancé n° {Back.YELLOW} {index} {Back.RESET} vaut {Back.GREEN} {picked_number} {Back.RESET} \n -> la somme totale de tout les lancé est de {Back.CYAN} {sum} {Back.RESET} \n ")


# / Main Loop /

while last_num !=5 and picked_number != 6 :

    last_num = picked_number
    index +=1
    picked_number = randrange(1,7)
    sum += picked_number
    
    
    print(f"Le Lancé n° {Back.YELLOW} {index} {Back.RESET} vaut {Back.GREEN} {picked_number} {Back.RESET} \n -> la somme totale de tout les lancé est de {Back.CYAN} {sum} {Back.RESET} \n ")
