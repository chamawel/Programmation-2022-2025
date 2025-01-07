string      : str = "Le ciel est bleu aujourd'hui!"

first_found : int = -1
last_found  : int = -1

wanted_char : str = input("Donnez une lettre: ")


for i in range(len(string)):
    if string[i] == wanted_char:
        last_found = i
    