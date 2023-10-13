import time

while True:
    u_input      = input("Donnez les âge (séparé par des espace: a b c)")
    u_input_list = u_input.split()
    print('liste',u_input_list)

    for i in range(len(u_input_list)):
        u_input_list[i] = int(u_input_list[i])


    result = u_input_list.index(min(u_input_list))

    if result == 0:
        print("Le premier joueur a priorité")
    elif result == 1:
        print("Le second joueur a priorité")
    else:
        print("Le dernier joueur a priorité")

    isquitting = input("Voulez-vos quitter ? (Y/N)")

    if isquitting == "Y" or isquitting == "y":
        exit("exiting Program ...")
    