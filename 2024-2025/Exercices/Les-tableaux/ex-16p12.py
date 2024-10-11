liste : list =[

    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],


]

for row in range(5):
    for column in range(5):
        liste[row][column] = 2 * (row) * (column + 1) 
    
    print(liste[row])