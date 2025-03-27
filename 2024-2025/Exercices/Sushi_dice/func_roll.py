from random import *

def rollDices(player_set, dices_rolled=[0,1,2,3,4,5]):
    """
    Player_set   => les dès du joueur
    Dices_rolled => les dès à rouler (liste)
    """

    for i in range(len(player_set) + 1):
        if i in dices_rolled:
            player_set[i-1] = randrange(1,7)


    return player_set



