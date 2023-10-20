import time

def calcPrice(quantity) :
    if quantity < 100 :
        price = 50
    elif quantity <300 :
        price = 45
    else:
        price = 40
    
    return price

while True:
    u_quantity = int(input("Combien de Casseroles Voullez-vous ? | 0 to close Program"))

    if u_quantity == 0:
        exit("Exiting Program ...")

    else:
        print(f"Le prix à payer pour {u_quantity} casseroles est {calcPrice(u_quantity)*u_quantity} €")
    
    time.sleep(1)
