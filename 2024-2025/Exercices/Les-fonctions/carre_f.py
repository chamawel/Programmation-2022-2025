from turtle import forward, left, color, goto, penup, pendown, done

def draw_square(lenght: int, s_color : str, x_cord : int, y_cord : int) -> None:
    penup()
    goto(x_cord,y_cord)
    pendown()

    for sides in range(4):
        color(s_color)
        forward(lenght)
        left(90)

def draw_all_squares(first_square : int,seccond_square : int) -> None:

    draw_square(first_square, "green", 30, 10)

    draw_square(seccond_square, "red", -90, 10)



# MAIN

draw_all_squares(75,50)
done()

