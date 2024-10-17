# Afficher combien de multiple de 3 il y a dans dans le tableaux
# Et combien sont aussi multiple de deux et trois.

list_of_nums                : list = [3,5,12,20,9] 
multiples_of_three          : int  = 0
multiples_of_three_and_two  : int  = 0


for i in range(len(list_of_nums)):
    if list_of_nums[i]  %3 == 0: #check mult de 3
        multiples_of_three += 1
        
        if list_of_nums[i] %2 == 0:
            multiples_of_three_and_two += 1 

    



print(f"il y avait:\n{multiples_of_three} multiple(s) de trois,\n{multiples_of_three_and_two} multiple(s) de deux et trois")


