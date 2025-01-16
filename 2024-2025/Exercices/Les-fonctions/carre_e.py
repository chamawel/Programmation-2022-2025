from turtle import forward, left, color, goto, penup, pendown, done

def draw_square(lenght: int, s_color : str, x_cord : int, y_cord : int) -> None:
        """Draw a square with the following caracteristics.
            Lenght  : n° of px of the sides 
            s_color : square color
            x_cord  : x coordonate where the square starts
            y_cord  : y coordonate where the square starts
        """
        
        penup()
        goto(x_cord,y_cord)
        pendown()
        
        for sides in range(4):
            color(s_color)
            forward(lenght)
            left(90)

def draw_all_squares() -> None:
    """Call 'draw_square' four times to create the windows logo.
    """

    draw_square(100, "green", 30, 10)

    draw_square(100, "red", -90, 10)

    draw_square(100, "blue", -90, -100)

    draw_square(100, "yellow", 30, -100)


# MAIN

draw_all_squares()
done()

