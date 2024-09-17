list : list = [0]*20


for i in range(len(list)):
    list[i] = len(list) - i

print(list)