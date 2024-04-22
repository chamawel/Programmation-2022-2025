i_number = int(input("Donnez un nombre"))
exponant = int(input("Donnez l'exposant"))
number = 1
c = 0

while c < exponant:
    number = number * i_number
    c += 1
    

print(f" {i_number} exposant {exponant} vaut : {number} ") 


