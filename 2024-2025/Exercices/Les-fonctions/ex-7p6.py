def charInStr(char : str, string : str) -> int:
    times_found = 0
    for _ in range(len(string)):
        if string[_] == char:
            times_found += 1
    
    return times_found

# Main

print(charInStr("e","Cette phrase est un exemple"))