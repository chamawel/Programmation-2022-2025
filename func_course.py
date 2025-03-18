def course() -> list:
    """
        l'utilisateur choisit 5 article et les 'scannes' ou non
    
        Affiche 'cadi'

        return 'items_scannes'

        n_of_items définit le n° d'article qui pourront être choissit
    """
    # CONFIG
    n_of_items : int = 5

    # LISTS
    cadi          : list = []
    items_scannes : list = []

    # PROCESS LOOP
    for i in range(n_of_items):
        item          : str = input("prenez un item: ")
        is_scanning   : str = input("Voulez-vous scanner l'item? (Y/N)")

        if is_scanning == "Y" or is_scanning == "y":
            cadi.append(item)
            items_scannes.append(item)

        else:
            cadi.append(item)
        
    # DISPLAYING AND RETURNING VALUES    
    print(f"Votre cadi: \n{cadi}\n")
    return items_scannes

