num_of_reds   = 0
num_of_blues_ = 0
seen = ""
stop = "S"

while seen != stop :

    if seen == "R":
        num_of_reds += 1

    elif seen == "B":
        num_of_blues_ += 1

    seen = input("De quelle couleur est la voiture :")

print(f"Il y a {num_of_reds} voitures rouges et {num_of_blues_} voitures bleues ")