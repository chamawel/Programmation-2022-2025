divided_number = int(input("Donner un nombre"))
divider        = 1

full_divisions = 1


while divider <= divided_number:
    divider += 1
    if divided_number % divider == 0:
        
        if full_divisions %2 == 0 :
            print("Il est Premier")
            
        
        else:
            print("Il n'est pas premier")
            
        
    full_divisions +=1
        
        
