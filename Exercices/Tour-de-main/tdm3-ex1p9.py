

number_given = float(input("Donnez un nombre"))
smallest = number_given
greatest = number_given
sum = number_given
c = 1

while c < 10:
    c +=1
    number_given = float(input("Donnez un nombre"))   
    sum += number_given

    if number_given < smallest:
        smallest = number_given
    
    elif number_given > greatest:
        greatest = number_given
    


print(f" {sum/10} moyenne , {smallest} plus petit nombre , {greatest} Plus grand nombre ")