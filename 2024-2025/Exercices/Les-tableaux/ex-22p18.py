wanted_word : str = input("Donner le mot pour stopper")
word_list : list = [""] * 20
found     : int

for i in range(len(word_list)):
        word_list[i] = input("Donner un mot")

        if word_list[i] == wanted_word:
             found = i



if found < 5:
    print("5 premier")

elif found < 10:
    print("5 suivant")

else:
    print("plus loin")

            




    


    
