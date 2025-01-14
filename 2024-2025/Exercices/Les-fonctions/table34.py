from random import randrange



def generate_calc_3(rand : int) -> int:
    respond = int(input(f"Que vaut {rand} * 3"))

    if respond == rand * 3:
        return "Correct"

    else:
        return "Incorrect"

def generate_calc_4(rand : int) -> int:
    respond = int(input(f"Que vaut {rand} * 4"))

    if respond == rand * 4:
        return "Correct"
    else:
        return "Incorrect"



# MAIN
for _ in range(10):
    randint = randrange(0,11)
    print(generate_calc_3(randint))
    randint = randrange(0,11)
    print(generate_calc_4(randint))

    

