from calcV2 import *

if __name__ == "__main__":
    
    first_n  : float  = float(input("Donnez vos nombre"))
    second_n : float  = float(input("Donnez vos nombre"))


    operation : str   = input("Que voullez vous faire? | Add | Sub | Mult | Div | ") 
    result    : float

    match operation:

        case "Add" | "add":
            result = calc.addition(first_n,second_n)

        case "Sub" | "sub":
            result = calc.addition(first_n,second_n)

        case "Mult" | "mult":
            result = calc.multiplication(first_n, second_n)

        case "Div" | "div":
            result = calc.divide(first_n,second_n)

        case _:
            raise ValueError(" ! Opération Non Trouvée")

    print(f"Le résultat vaut {result}")


