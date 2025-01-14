from random import randrange

def gen_calc(table : int) -> None:
        rand = randrange(1,11)
        result = rand * table

        calc = int(input(f"Que vaut {rand} * {table}"))

        if calc == result:
            return "Correct"
        
        else:
            return "Incorrect"


# MAIN
table       : int = int(input("Quelle Table?"))
n_of_calcs  : int = int(input("Combien de calcul?"))
for i in range(n_of_calcs):
    print(gen_calc(table))