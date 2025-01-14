from random import randrange

def generate_calc_result(x : int) -> int:
    return 3 * x


# MAIN
for _ in range(10):
    randint = randrange(0,11)
    calc = int(input(f"Que Vaut {randint} * 3 :"))

    if calc == generate_calc_result(randint):
        print("Correct")
    else:
        print("Incorrect")