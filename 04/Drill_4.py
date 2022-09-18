import turtle


x = 0
y = 0
count = 4
turtle.penup()

turtle.pendown()
while (y < 5):
    x = 0
    while(x < 5):
        count = 4
        while(count > 0):
            turtle.forward(100)
            turtle.left(90)
            count -=1
        x+=1
        turtle.forward(100)
    y+=1

    turtle.penup()
    turtle.goto(0 , y * 100)
    turtle.pendown()

turtle.exitonclick()
