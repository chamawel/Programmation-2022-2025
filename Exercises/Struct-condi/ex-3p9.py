import time

while True:

    # | AVEC LISTE  (plus stylé) |

    # u_input      = input("Donnez les âge (séparé par des espace: a b c)")
    # u_input_list = u_input.split()
    # print('liste',u_input_list)

    # for i in range(len(u_input_list)):
    #     u_input_list[i] = int(u_input_list[i])

    # print("Liste Convertie",u_input_list)


    # result = u_input_list.index(min(u_input_list))

    # print(f"Le joueur avec la priorité est le joueur {result+1} " )

    # isquitting = input("Voulez-vos quitter ? (Y/N)")

    # if isquitting == "Y" or isquitting == "y":
    #     exit("exiting Program ...")

    # | SANS LISTE (vachement moins cool) |
    
    a = int(input("age 1er joueur"))
    b = int(input("age 2eme joueur"))
    c = int(input("age 3eme joueur"))

    if   a < b <c :
        print("Le joueur 1 est prioritaire")
        
    elif b < a <c:
        print("Le joueur 2 est prioritaire")
        
    elif c < b <a :
        print("Le joueur 3 est prioritaire")
        
    else:
        print("Il y a une égalité")

    isquitting = input("Voulez-vos quitter ? (Y/N)")

    if isquitting == "Y" or isquitting == "y":
        exit("exiting Program ...")
    
    time.sleep(1)