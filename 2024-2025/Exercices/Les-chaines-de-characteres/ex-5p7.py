string       : str = "Le chien de madame Dupond est un labrador"

no_space_str : str = ""
bar_str      : str = ""

num_of_words : int = 1
question     : str


for i in range(len(string)):
    
    if string[i] == " ":
        no_space_str += ""
        bar_str      += "|"
        num_of_words += 1

    else:
        no_space_str += string[i]
        bar_str      += string[i]


question = int(input("Combien de mots comporte la phrase: " + no_space_str))

if question == num_of_words:
    print("Bonne Réponse !")

else:
    print(f"Mauvaise réponse, voici une phrase découpée:\n{bar_str}")