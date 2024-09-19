liste : list = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],

]



for row in range(len(liste)):
    for column in range(6):
        
        liste[row][column] = 5 + (row * 4) + (column * 4)  
        
    
    print(liste[row])



