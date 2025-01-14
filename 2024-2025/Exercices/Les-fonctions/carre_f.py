from turtle import forward, left, color, goto, penup, pendown, done

def draw_square(lenght: int, s_color : str) -> None:
    for sides in range(4):
        color(s_color)
        forward(lenght)
        left(90)

def draw_all_squares(first_square : int,seccond_square : int) -> None:
    penup()
    goto(30,10)
    pendown()
    draw_square(first_square, "green")

    penup()
    goto(-90,10)
    pendown()
    draw_square(seccond_square, "red")



# MAIN

draw_all_squares(75,50)
done()

