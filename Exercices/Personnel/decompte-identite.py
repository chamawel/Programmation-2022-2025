# #WOOAAA 
import time


def main():
    print("#########################")
    anser = input("Que vouler vous faire?\n1.Demander l'identiter (I) | 2.Faire un décompte de 3 à 0 (D) ")

    if anser == "I":
        DemandeIdentiter()
    if anser == "D":
     Decompte()
    else:
        print("Réponse Invalide recomencer!!")
        time.sleep(0.5)
        main()


def DemandeIdentiter() :    
    name = input("Votre nom?")
    firstname = input("Votre Prénom?")
    gender = input("Votre genre?")

    print(name + " " + firstname )
    print("Vous êtes un(e) " + gender +"!" )
    time.sleep(0.5)
    main()

def Decompte():
    number = int(input("Donner un nombre!"))
    while number >= 0 :
        print(number)
        number = number - 1
        time.sleep(1)
    time.sleep(0.5)
    main()

main()
