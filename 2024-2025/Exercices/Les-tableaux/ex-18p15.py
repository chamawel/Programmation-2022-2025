liste           : list = [32,5,12,8,3,75,2,15]
greatest        : int = 0
index           : int = 0     
greatest_index  : int = 0 

for elem in liste:
        if elem > greatest:
            greatest = elem
            greatest_index = index

        index +=1  
    
     
        

    
    
print(f"Le plus grand élément est le {greatest_index} et vaut {greatest}")