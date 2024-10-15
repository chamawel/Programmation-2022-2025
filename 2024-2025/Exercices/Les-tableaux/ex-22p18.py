# Demander le mot rechercher
# Dire si le mot se trouve:
#   Dans les 5 permière valeur,
#   Dans les 5 suivantes,
#   Ou Plus loin dans le tableaux

wanted_word : str = input("Donner le mot pour stopper")
word_list : list = ["e","f","g","h","y","u","i","o","p"]
found     : int  = 0

for i in range(len(word_list)):
    if word_list[i] == wanted_word:
        found = i
    
        

if found < 5:
    print(f"5 premier ( {found} ) ")

elif found < 10:
    print(f"5 suivant ( {found} ) ")

else:
    print(f"plus loin ( {found} ) ")


       




    


    
