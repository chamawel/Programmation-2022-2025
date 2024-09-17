list : list = [0]*20

char : int = ord("a")

for i in range(len(list)):
    list[i] = chr(char + i)

print(list)