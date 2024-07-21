from turtle import *


#we want to paint a house

#step 1: draw a square

speed(30)
width(7)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a dor

forward(70)
color("black")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto(140, 150)
pendown()

left(30)
forward(20)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(40)

penup()
goto(40, 130)
pendown()


forward(20)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(40)







exitonclick()
