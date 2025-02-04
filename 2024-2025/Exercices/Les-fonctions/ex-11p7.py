def boxVolume(lenght : float = -1, height : float = -1, depth : float = -1) -> float:
    if lenght != -1 and height != -1 and depth != -1:
        return lenght * height * depth

    elif lenght != -1 and height != -1:
        return  lenght**2 * height

    elif lenght != -1:
       return lenght**3 

    else:
        return -1

# Main
print(boxVolume())
print(boxVolume(5.2))
print(boxVolume(5.2, 3))
print(boxVolume(5.2, 3, 7.4))