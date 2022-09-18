import turtle


x = 0
y = 0
count = 4
turtle.penup()

turtle.pendown()
while (x < 5):
    y = 0
    while(y < 5):
        count = 4
        while(count > 0):
            turtle.forward(100)
            turtle.left(90)
            count -=1
        y+=1
        turtle.forward(100)
    x+=1

    turtle.penup()
    turtle.goto(0 , x * 100)
    turtle.pendown()

turtle.exitonclick()
