def checkDices(player_set,chosen_val):
    """
    player_set => les dés du joueur 
    chosen_val => la valeur a laquelle TOUT les dés doivent être =
    """
    for i in range(len(player_set)):
        if player_set[i]!=chosen_val and player_set[i]!=6:
            return False
    
    return True
