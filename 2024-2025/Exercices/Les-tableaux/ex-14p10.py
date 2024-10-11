liste : list = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],

]



for row in range(4):
    for column in range(6):
        
        liste[row][column] = 5 + (row * 3 ) + (column * 4)  
        
    
    print(liste[row])



