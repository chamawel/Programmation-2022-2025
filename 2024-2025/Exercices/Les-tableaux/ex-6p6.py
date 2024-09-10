list    : list = [0]*20
current : int = 20
index = 0

while current > 0:
    list[index] = current
    index    +=1
    current -=1

print(list)