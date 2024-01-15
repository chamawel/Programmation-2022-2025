# si le resultat de numéro % 2 == 0 , Alors il est paire.
while True:
    max_number = int(input("Donnez le maximum"))    # max_number est le nombre donnant la limite de la boucle
    checked_number = 0                              # checked_number est le nombre qui sera ajouter si paire
    result = 0                                      # result est le résultat.

    while checked_number < max_number:
        checked_number += 1

        if checked_number%2 == 0:
            result += checked_number
    
    print(f"Le résultat de la somme des nombres paire entre 1 et {max_number} est de : {result} ")

    isexiting = input("partir ? (Y/N)")

    if isexiting == "Y" or isexiting =="y":
        exit("Closing program") 
    else:
        print("continuing")
