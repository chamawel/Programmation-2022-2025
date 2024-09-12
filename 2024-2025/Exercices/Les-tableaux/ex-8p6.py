list    : list = [0]*20                                                      
char    : int = 97
index   : int = 0


while index < 20:
    list[index] = chr(char)
    index += 1
    char  += 1

print(list)

