import turtle

def Top_move():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()
    
def Left_move():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()
    
def Bottom_move():
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.stamp()

def Right_move():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(Top_move, 'w')
turtle.onkey(Left_move, 'a')
turtle.onkey(Bottom_move, 's')
turtle.onkey(Right_move, 'd')

turtle.onkey(restart, 'Escape')
turtle.listen()
turtle.exitonclick()
