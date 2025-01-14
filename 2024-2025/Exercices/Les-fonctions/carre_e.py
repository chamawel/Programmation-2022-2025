from turtle import forward, left, color, goto, penup, pendown, done

def draw_square(lenght: int, s_color : str) -> None:
    for sides in range(4):
        color(s_color)
        forward(lenght)
        left(90)

def draw_all_squares() -> None:
    penup()
    goto(30,10)
    pendown()
    draw_square(100, "green")

    penup()
    goto(-90,10)
    pendown()
    draw_square(100, "red")

    penup()
    goto(-90,-100)
    pendown()
    draw_square(100, "blue")

    penup()
    goto(30,-100)
    pendown()
    draw_square(100, "yellow")


# MAIN

draw_all_squares()

