from random import randint
question = 20
lifes = 2
score = 0
c = 0

while c < question:
    c += 1
    randint_1 = randint(2,10)
    randint_2 = randint(2,10)
    user_respond = int(input(f"Que vaut {randint_1} x {randint_2} "))
    
    if user_respond == randint_1*randint_2:
        score +=1
        print("Bravo")
        
    else:
        print(f"raté, la bonne réponse était {randint_1*randint_2}  ")
        lifes -=1

        if lifes == 0:
            print(f"Perdu !")
            break

print(f"votre score : {score} ")

