string      : str = "salut Remy"
wanted_char : str = "a"

found_at    : int = -1

for i in range(len(string)):
    if string[i] == wanted_char:
        found_at = i

print(f"La lettre '{wanted_char}' se trouve en position {found_at} dans la chaine de characteres")