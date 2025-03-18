from random import randrange

def modif(index_list : list, random_list : list, x : int, y : int) -> list:
    """
        randomize 'random_list' content according to the indexes inside of 'indexlist' and the value of x and y

        index_list -> a list of indexes

        random_list -> the list that will be randomized

        x -> min value a number possibly can be 

        y -> max value a number possibly can be
    """
    
    # RANDOMIZING LIST
    for i in range(len(random_list)):
        if i in index_list:
            random_list[i] = randrange(x, y+1)
        
    # RETURNING VALUES
    return random_list

