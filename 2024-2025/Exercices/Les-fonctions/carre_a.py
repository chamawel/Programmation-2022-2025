from turtle import forward, left, done

def draw_square(lenght: int) -> None:
    for sides in range(4):
        forward(lenght)
        left(90)



# MAIN
draw_square(100)
done()