from turtle import forward, left, color, goto, penup, pendown, done

def draw_square(lenght: int) -> None:
    for sides in range(4):
        forward(lenght)
        left(90)


# MAIN
color("red")
penup()
goto(30,10)
pendown()
draw_square(100)

done()