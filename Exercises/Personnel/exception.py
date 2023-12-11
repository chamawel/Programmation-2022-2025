from colorama import Back, Fore, Style

while True:
    try:
        num = int(input("Donnez un nombre"))
        print(f"Votre nombre + 1 : {Back.GREEN} {num+1} {Back.RESET} ")
        break
    except ValueError:
        print(Fore.RED + "Vous devez entré un nombre")
        print(Fore.RESET)
    finally:
        print(f" {Style.BRIGHT} BOO {Style.RESET_ALL}")