import turtle
from time import sleep

if __name__ == "__main__":
    turtle.color("red")

    turtle.begin_fill()
    turtle.pensize(3)

    #Right side
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50,200)

    #Left side
    turtle.right(140)
    turtle.circle(50,200)
    turtle.forward(133)

    turtle.end_fill()
    
    turtle.done()
    