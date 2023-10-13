import time 

def verify(place):


    if place < 5:
        price = 7
    
    elif place <= 10:
        price = 6
    
    else:
        price = 4.5
    
    return price


while True:

    place_u = int(input("how many places do you want? | 0 to close program "))

    if place_u == 0:
        time.sleep(1)
        exit("Exiting Program...")

    else:
        print(f"Cela coutera: { verify(place_u)*place_u } €")

    time.sleep(1)

    

