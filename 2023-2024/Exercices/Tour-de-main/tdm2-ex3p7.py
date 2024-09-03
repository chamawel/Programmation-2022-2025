from colorama import *          # pip install colorama
just_fix_windows_console()      # Pour le CMD de windows

distance_train = int(input(f"Nmb de km en {Back.YELLOW}Train{Back.RESET} ?" ))
distance_foot = int(input(f"Nmb de km à {Back.CYAN}Pied{Back.RESET} ? " ))

total_distance_t = 0
total_distance_f = 0
current_day = 0

while current_day < 30:
    
    try:
        current_day += 1
        print(f" \n {Fore.BLUE} --- Jour Suivant --- {Fore.RESET} \n ")
        distance_train = int(input(f"Nmb de km en {Back.YELLOW}Train{Back.RESET} ?" ))
        distance_foot = int(input(f"Nmb de km à {Back.CYAN}Pied{Back.RESET} ?" ))
        
        
        total_distance_t += distance_train
        total_distance_f += distance_foot
    
    except ValueError:
        print(f"{Fore.RED}/!\ | Vous devez entré un nombre {Fore.RESET}  ")
        current_day = 0
        total_distance_f = 0
        total_distance_t = 0

        print("Les valeur ont été réinitialisée")
    

print(f"Tom et Pierre on parcourus : {Back.CYAN}{total_distance_f}Km{Back.RESET} à pied et {Back.YELLOW}{total_distance_t}Km{Back.RESET} en train  ")