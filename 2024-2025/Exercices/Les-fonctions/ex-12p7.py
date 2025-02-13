def replaceChar(phrase : str, char1 : str, char2 : str, start : int = 0, end : int = -1) -> str:
    """This Function replaces a char by another 
    """

    if end == -1:
        end = len(phrase)

    transformed_phrase : str = ""

    for i in range(start,end):
        if phrase[i] == char1:
            transformed_phrase += char2
        
        else:
            transformed_phrase += phrase[i]

    return transformed_phrase
 
phrase = "aeaeaeaeaeaeaeae"

print(replaceChar(phrase,"e","b"))