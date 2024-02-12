number = int(input("Donnez un nombre"))
exponant = int(input("Donnez l'exposant"))
i_number = number
c = 1

while c < exponant:
    c += 1
    number = number * i_number
    

print(f" {i_number} exposant {exponant} vaut : {number} ") 


