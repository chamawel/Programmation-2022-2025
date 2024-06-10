def sumOfnumber(n : int) -> int:
    return n*(n-1) / 2


def main() -> None:
    number : int = int(input("Donnez la longeur de la suite")) 
    print(f"La somme des nombre de 1 jusqu'à {number} est de {sumOfnumber(number):,}")



if __name__ == "__main__":
    main()
