user_number     = int(input("Donnez un nombre"))            #Nombre donner par l'utilisateur
user_multplier  = int(input("Donnez le multiplicateur"))    #Multiplicateur donner par l'utilisateur
user_number_iv  = user_number                               #Valeur Innitial de 'user_number'
c = 1                                                       #Valeur s'encrémentant pour stopper la boucle


while c < user_multplier:
    user_number += user_number_iv
    c += 1

print(f"Le résultat de votre calcul vaut {user_number}" )