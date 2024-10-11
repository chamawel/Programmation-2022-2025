list_of_nums              : list = [0] * 20
multiples_of_five         : int = 0
multiples_of_five_and_two : int = 0

fill_index                : int = 0

# On remplit la liste

while multiples_of_five < 3:
    list_of_nums[fill_index] = int(input("Donner un nombre"))

# Mult de 5 ?
    if list_of_nums[fill_index] %5 == 0:
        multiples_of_five += 1
    #Mult de 5 ET de 2 ?
        if list_of_nums[fill_index] %2 == 0:
            multiples_of_five_and_two += 1

    fill_index +=1




print(f"il y avait {multiples_of_five_and_two} multiple de deux et cinq")


