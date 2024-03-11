number = int(input("Donnez un nombre"))
exponant = int(input("Donnez l'exposant"))
i_number = number
c = 1

if exponant == 0:
    number = 1

else:    
    while c < exponant:
        c += 1
        number = number * i_number
    

print(f" {i_number} exposant {exponant} vaut : {number} ") 


