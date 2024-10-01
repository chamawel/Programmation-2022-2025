liste           : list = [-11,23,-43,18,-3,-725,-2,15]
first_elem      : int  = liste[0]

greatest        : int  = first_elem
greatests_index  : int  = 0

for i in range(len(liste)):
        if liste[i] > greatest:
            greatest = liste[i]
            greatests_index = i
            

    
     


    
    
print(f"Le plus grand élément est le {greatests_index} et vaut {greatest}")