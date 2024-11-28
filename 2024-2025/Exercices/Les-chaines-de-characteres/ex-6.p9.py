asked_letter : str = input("Donner une lettre minuscule: ")

if len(asked_letter) == 1 and ord(asked_letter) >= ord("a"):

    if ord(asked_letter) < ord("k"):
        print(f"la lettre {asked_letter} est avant K")

    elif ord(asked_letter) == ord("k"):
        print("La lettres est K")

    else:
        print(f"la lettre {asked_letter} est après K")

else:
    print("/!\ Vous pouvez seulement entré une lettre minuscule ")

