def boxVolume(lenght : float = -1, height : float = -1, depth : float = -1) -> float: 
    if height == -1:
        return lenght**3
    
    elif depth == -1:
        return lenght**2 * height
    
    else:
        return lenght * height * depth



# Main
print(boxVolume())
print(boxVolume(5.2))           # lenght**3
print(boxVolume(5.2, 3))        # lenght**2 * height
print(boxVolume(5.2, 3, 7.4))   # lenght * height * depth