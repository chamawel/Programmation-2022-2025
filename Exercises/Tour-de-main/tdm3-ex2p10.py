from colorama import *          # pip install colorama
just_fix_windows_console()      # Pour le CMD de windows

days = int(input("Combien de Jour ?"))                                          # Demande de n° d ejour du séjour
distance_train = int(input(f"Nmb de km en {Back.YELLOW}Train{Back.RESET} ?" ))  # Demande distance [Train] 
distance_foot = int(input(f"Nmb de km à {Back.CYAN}Pied{Back.RESET} ? " ))      # Demande distance [Pied]
print(f"Moyenne de Km ce jour : {(distance_foot + distance_train) /2 } ")       # Affichage [mayenne] 

greatest_distance_f = distance_foot 

total_distance_t = distance_train
total_distance_f = distance_foot


current_day = 1

while current_day < days:
    
    try:
       
        print(f" \n {Fore.BLUE} --- Jour Suivant --- {Fore.RESET} \n ")
        
        # // Demande des distances //
        distance_train = int(input(f"Nmb de km en {Back.YELLOW}Train{Back.RESET} ?" ))
        distance_foot = int(input(f"Nmb de km à {Back.CYAN}Pied{Back.RESET} ?" ))
        
        # // Check si le N° de Km et le + grand //
        if distance_foot > greatest_distance_f:
            greatest_distance_f = distance_foot

        # // Affichage De la Moyenne/Jour
        print(f"Moyenne de Km ce jour : {(distance_foot + distance_train) /2 } ")
        
        # // Somme Des Distances //
        total_distance_t += distance_train
        total_distance_f += distance_foot
        current_day += 1
    
    except ValueError: # // En cas d'erreur //

        print(f"{Fore.RED}/!\ | Vous devez entré un nombre {Fore.RESET}  ")
        current_day = 0
        total_distance_f = 0
        total_distance_t = 0
        

        print("Les valeur ont été réinitialisée")
    

print(f"Tom et Pierre on parcourus : {Back.CYAN}{total_distance_f}Km{Back.RESET} à pied et {Back.YELLOW}{total_distance_t}Km{Back.RESET} en train. La plus grande distance parcourue a pied est de {Back.CYAN} {greatest_distance_f}km {Back.RESET55} ") 