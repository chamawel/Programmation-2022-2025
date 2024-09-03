# / Imports /

from random import randrange
from colorama import *          # pip install colorama
just_fix_windows_console()      # Pour le CMD de windows

# / Variables / 

index         : int = 1
one_is_rolled : int = 0

picked_number : int = randrange(1,7)
last_num      : int = picked_number



print(f"Le Lancé n° {Back.YELLOW} {index} {Back.RESET} vaut {Back.GREEN} {picked_number} {Back.RESET} \n")


# / Main Loop /

while last_num != 5 or picked_number != 6 :
    
    last_num = picked_number
    index +=1
    picked_number = randrange(1,7)

    if picked_number == 1:
        one_is_rolled += 1
    
    
    
    print(f"Le Lancé n° {Back.YELLOW} {index} {Back.RESET} vaut {Back.GREEN} {picked_number} {Back.RESET} le N° 1 a été roullé : {Back.CYAN} {one_is_rolled} fois {Back.RESET} \n")
