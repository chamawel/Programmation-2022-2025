list    : list = [0]*20
current : int = 1
index = 0

while index < 20:
    if index <= 9:
        list[index] = current
        current     += 1
        index       += 1
    
    else:
        current     -= 1
        list[index] = current
        index       += 1

print(list)


