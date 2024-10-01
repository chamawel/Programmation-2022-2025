stop_word : str = input("Donner le mot pour stopper")
word_list : list = [""] * 20


for i in range(len(word_list)):
    if stop_word not in word_list:
        word_list[i] = input("Donner un mot")
    
    else:
        word_found = i


if word_found < 5:
    print("5 premier")
            

elif word_found < 10:
    print("5 suivant")
            
else:
    print("plus loin")
            

    


    
