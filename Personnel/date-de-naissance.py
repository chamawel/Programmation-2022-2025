import datetime
print("Bonjour")
nom     : str = input("Donnez votre nom:")
prenom  : str = input("Donnez votre prenom:")
date    : str   = str(datetime.datetime.now())
age     : int = int(input("Donnez votre âge: "))
print(f"Bonjour {prenom} {nom} !\nVous ête né en {int(date[:4]) - age }")
