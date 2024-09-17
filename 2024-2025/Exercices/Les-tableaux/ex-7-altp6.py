list = [0]*20

for i in range(len(list)):
    if i < 10:
        list[i] = i + 1
    else:
        list[i] = len(list) - i

print(list)