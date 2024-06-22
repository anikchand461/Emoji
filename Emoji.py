# Emoji

from turtle import *
import turtle

s = Screen()
speed('fast')
hideturtle()

#main circle
up()
goto(-200,0)
down()
pensize(8)
begin_fill()
fillcolor('yellow')
seth(-90)
circle(200)
end_fill()

#mouth
up()
goto(-155,0)
down()
begin_fill()
fillcolor('#5D2520')
seth(-90)
circle(155,180)
seth(200)
circle(-450,40)
end_fill()

#tongue
up()
goto(-65,-22)
down()
begin_fill()
fillcolor('#D1908e')
seth(-90)
fd(140)
circle(65,180)
fd(140)
seth(188)
circle(-450,16)
end_fill()

#eyes
up()
goto(-120,90)
down()
pensize(7)
seth(-90)
begin_fill()
fillcolor('white')
circle(50)
end_fill()

up()
goto(-100,80)
down()
pensize(5)
begin_fill()
fillcolor('black')
circle(25)
end_fill()

up()
goto(50,75)
seth(65)
pensize(9)
down()
circle(-35,130)

s.mainloop()
