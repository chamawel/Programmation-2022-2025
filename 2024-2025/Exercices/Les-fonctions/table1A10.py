from random import randrange

def gen_calc(table : int) -> None:
    for _ in range(10):
        rand = randrange(1,11)
        result = rand * table

        calc = int(input(f"Que vaut {rand} * {table}"))

        if calc == result:
            return "Correct"
        
        else:
            return "Incorrect"

# MAIN
for i in range(10):
    print(gen_calc(i + 1))