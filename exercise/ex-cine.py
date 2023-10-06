import time 

def verify(place):


    if place < 5:
        return place * 7
    
    elif place <= 10:
        return place *6
    
    else:
        return place * 4.5


while True:

    place_u = int(input("how many places do you want? | 0 to close program "))

    if place_u == 0:
        time.sleep(1)
        exit("Bye")

    else:
        print(f"Cela coutera: { verify(place_u) } €")

    time.sleep(1)

    

