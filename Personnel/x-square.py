import turtle

if __name__ == "__main__":

    def x_square(x : int) -> int:
        return x ** 2 
    
    def draw_axis() -> None:
        #Drawing the X axis
        turtle.goto(-800,0)
        turtle.forward(1600)

        #Drawing the y axis
        turtle.goto(0,0)
        turtle.right(90)
        turtle.forward(800)
        turtle.right(180)
        turtle.forward(1600)


    starting_x  : int = int(input("donner le minimum"))
    end_x       : int = int(input("donner le maximum"))

    draw_axis()
   
    # Placing the turtle to draw the result
 
    turtle.color("red")
    turtle.penup()
    turtle.goto(starting_x , x_square(starting_x))

    # Drawing The Function

    for x in range(starting_x, end_x + 1):
       turtle.pendown()
       turtle.goto(x, x_square(x))
    
    turtle.done()
