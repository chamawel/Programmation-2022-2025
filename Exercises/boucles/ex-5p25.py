divided_number = int(input("Donner un nombre"))
divider        = 1

full_divisions = 0


while divider <= divided_number:
    divider += 1
    if divided_number % divider == 0:
        full_divisions +=1
        
        if full_divisions == 2:
            print("Il est Premier")
            break
        
        else:
            print("Il n'est pas premier")
            break

