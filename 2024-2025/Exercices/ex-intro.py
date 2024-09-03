# TDM3 + FLOATS
# On Demande une Hauteur,
# On fini par donner la + grande hauteur et la + petite



skyscrapers         : int = int(input("Combien d'immeubles voulez-vous messuré?"))
height              : float = float(input("Donner Une hauter (cm) pour Commencer (entré 0 pour fermé) "))

smallest_height     : float = height
greatest_height     : float = height
current_skyscraper  : int = 1




try:
    while current_skyscraper < skyscrapers:
        height = float(input("Donner Une hauter (cm) pour Commencer (entré 0 pour fermé) "))

        if height < smallest_height:
            smallest_height = height
            
        elif height > greatest_height:
            greatest_height = height
        
        current_skyscraper +=1

except ValueError:
    print("Erreur,Entré des nombre SVP")
    
        
    
print(f"le plus grand:{greatest_height} et le + petit: {smallest_height}")








