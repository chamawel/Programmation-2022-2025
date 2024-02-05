number_of_words = 0
curent_word = ""
stop = 'stop'

while curent_word != stop:
    number_of_words +=1
    curent_word = input("Donner un mots: ")
    
print(f"Tu as rentré : {number_of_words} mots ")

