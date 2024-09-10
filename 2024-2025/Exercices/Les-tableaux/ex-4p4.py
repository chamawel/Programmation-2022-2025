list    : list = [0]*20
current : int = 1
index = 0

while current <= 20:
    list[index] = current
    index    +=1
    current +=1

print(list)