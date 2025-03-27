    # ! IMPORTS

from random import randrange
from func_check import checkDices
from func_roll  import rollDices


def main() -> str:
    player_set : list = [0] * 6
    dices_to_roll : list
    chosen_val : int
    
    # ! INNIT LOOP
    chosen_val = int(input("»» Donner une valeur de victoire entre 1-6 et lancer les dés »» "))
    player_set = rollDices(player_set)
    print(f" »» Voici vos dés »»\n  {player_set}\n")
    
    if checkDices(player_set,chosen_val) is True:
        return " »» VICTOIRE !!! »»"

    # ! GAME LOOP
    while True:
        chosen_val    = int(input("»» Donner une valeur de victoire entre 1-6 et lancer les dés »» "))
        dices_to_roll = list(input("»» Quell dés voulez-vous rouller? »» "))
        dices_to_roll = sorted(map(int, dices_to_roll)) 
        
        player_set = rollDices(player_set,dices_to_roll)
        print(f" »» Voici vos dés »»\n  {player_set}\n")
        
        if checkDices(player_set,chosen_val) is True:
            return " »» VICTOIRE !!! »»"
    
    

if __name__ == "__main__":
    print(main())

