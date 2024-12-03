string      : str = "aaaaaaabbeeeeebbbbccc"
last_char   : str = string[0]

final_str   : str = string[0]

for i in range(len(string)):
    
    if last_char != string[i]:
        final_str += string[i]
        last_char = string[i]


print(final_str)
