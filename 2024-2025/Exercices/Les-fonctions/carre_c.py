from turtle import forward, left, right, color, goto, penup, pendown, done
lenght = 100
colors : list = ["green","yellow", "blue", "red"]


for square_color in colors:
    color(square_color)
    
    for sides in range(4):
        forward(lenght)
        left(90)
    
    right(90)
    penup()
    forward(10)
    pendown()



done()