
def mult() :
    print("#####-Multiplication-#####")
    f_number_m=int(input("Donnez un nombre "))
    s_number_m=int(input("Donnez en un 2eme "))
    result_m= f_number_m*s_number_m
    print("Le résultat est: ",str(result_m))
    
    menu()



def addi() :
    print("#####-addition-#####")
    f_number_a=int(input("Donnez un nombre "))
    s_number_a=int(input("Donnez en un 2eme "))
    result_a= f_number_a + s_number_a
    print("Le résultat est:",str(result_a))
    
    menu()


def soustr() :
    print("#####-soustraction-#####")
    f_number_s=int(input("Donner un nombre "))
    s_number_s=int(input("Donner en un 2eme "))
    result_s=f_number_s - s_number_s
    print("Le résultat est",str(result_s))
    menu()



def divis() :
    print("#####-division Entière-#####")
    f_number_d=int(input("Donner un nombre "))
    s_number_d=int(input("Donner en un 2eme "))
    result_d= f_number_d//s_number_d
    print("le résultat est",str(result_d))
    menu()


def menu():
    print("########--MENU--#######")
    print("""Quelle opération voulez vouf faire:
          Mutiplication: saisis 1
          Addition : saisis: 2 
          Soustraction : saisis 3 
          Division entière : saisis 4 
          Stop : 5""")
    choice=input("Quel est ton choix?")
    
    if choice == "1":
        mult()


    elif choice=="2":
        addi()


    elif choice=="3":
        soustr()


    elif choice=="4":
        divis()


    elif choice=="5":
        print("Fin des abricot 👋")
        exit()
        
    else:
        print("Erreur:Réponse non valide")

menu()

