main_list : list = [32,5,12,8,3,75,2,15]

even_list : list = [0] * 4
odd_list  : list = [0] * 4

evens = 0
odds  = 0


for elem in main_list:       
    if elem %2 == 0:
        even_list[evens] = elem 
        evens +=1
        
    else:
        odd_list[odds]  = elem
        odds +=1
    
    
                
print(f"Paire:   {even_list }\nImpaire: {odd_list }")

