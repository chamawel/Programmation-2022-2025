import turtle
import math

if __name__ == "__main__":

    def x_square(x : int) -> int:
        return x ** 2  
    
    def draw_axis() -> None:
        #Drawing the X axis
        turtle.goto(-800,0)
        turtle.forward(1600)
        turtle.penup()

        #Drawing the y axis
        turtle.goto(0,-800)
        turtle.pendown()

        turtle.left(90)
        turtle.forward(1600)


    starting_x  : int = int(input("donner le minimum"))
    end_x       : int = int(input("donner le maximum"))

    draw_axis()
    turtle.width(3)
   
    # Placing the turtle to draw the result
 
    turtle.color("red")
    turtle.penup()
    turtle.goto(starting_x * 50 , x_square(starting_x) * 50)

    # Drawing The Function

    for x in range(starting_x, end_x + 1):
        try:
            turtle.pendown()
            turtle.goto(x * 50, x_square(x) * 50)

        except ZeroDivisionError:
            continue
    turtle.done()
