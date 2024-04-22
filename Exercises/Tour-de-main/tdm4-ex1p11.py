number_of_words : int = 0

curent_word : str = ""
stop        : str = 'stop'
att         : str = 'attention'
last_word   : str = curent_word


while curent_word != stop and last_word != att:
    
    last_word = curent_word
    
    number_of_words +=1
    curent_word = input("Donner un mots: ")
    

print(f"Tu as rentré : {number_of_words} mots ")

