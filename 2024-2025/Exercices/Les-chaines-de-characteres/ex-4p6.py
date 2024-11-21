string          : str = "acouta event da perlar, mecha event d'evelar"
transformed_str : str = ""

for i in range(len(string)):
    if string[i] == "a":
        transformed_str += "e"
    
    elif string[i] == "e":
        transformed_str += "a"
    
    else:
        transformed_str += string[i]

print(transformed_str)
        