asked_letter : str = input("Donner une lettre minuscule: ")

if len(asked_letter) == 1 and asked_letter >= "a":

    if asked_letter < "k":
        print(f"la lettre {asked_letter} est avant K")

    elif  asked_letter ==  "k":
        print("La lettres est K")

    else:
        print(f"la lettre {asked_letter} est après K")

else:
    print("/!\ Vous pouvez seulement entré une lettre minuscule ")