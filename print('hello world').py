import turtle

turtle.pensize(10)
turtle.pencolor('red')
turtle.circle(105)

turtle.left(90)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.right(90)

turtle.fillcolor('blue')
turtle.begin_fill()
turtle.circle(55)
turtle.end_fill()

turtle.pensize(1)
turtle.pencolor('white')
turtle.fillcolor('white')

turtle.penup()
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(48)
turtle.left(180)
turtle.pendown()

turtle.begin_fill()
i=0
while i<5:
  turtle.forward(100)
  turtle.right(144)
  i+=1
turtle.end_fill()

turtle.hideturtle()