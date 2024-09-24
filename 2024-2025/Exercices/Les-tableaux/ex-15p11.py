liste : list =[

    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],

]

for row in range(5):
    for column in range(7):
        
        liste[row][column] = 1 + (row * 4) + (column * 2)
    
    print(liste[row])