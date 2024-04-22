import math

def calcDelta(a,b,c):
   return b**2-4*(a*c)

def resolve(a,b,c):
    delta = calcDelta(a,b,c)

    if delta < 0 :

        result = "aucunes racines"

    elif delta == 0:

        result = "Une racine"

    else:

        result = "Deux racines"
        
    return result

while True:
    
    
    u_a = float(input("Donnez 'a' "))

    u_b = float(input("Donnez 'b' "))

    u_c = float(input("Donnez 'c' "))

    print(f"La fonction connais {resolve(u_a,u_b,u_c)} ")

    isquitting = input("Voulez-vos quitter ? (Y/N)")

    if isquitting == "Y" or isquitting == "y":
        exit("exiting Program ...")
    
    
