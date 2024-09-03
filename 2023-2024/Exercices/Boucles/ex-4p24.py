from random import randrange
question = 20
lifes = 2
score = 0
c = 0

while c < question:
    c += 1
    randrange_1 = randrange(2,11)
    randrange_2 = randrange(2,11)
    user_respond = int(input(f"Que vaut {randrange_1} x {randrange_2} "))
    
    if user_respond == randrange_1*randrange_2:
        score +=1
        print("Bravo")
        
    else:
        print(f"raté, la bonne réponse était {randrange_1*randrange_2}  ")
        lifes -=1

        if lifes == 0:
            print(f"Perdu !")
            break

print(f"votre score : {score} ")

