from turtle import *

def amogus(color):
  speed(0)
  pencolor(color)
  fillcolor(color)
  begin_fill()
  circle(20, 90)
  forward(60)
  circle(20, 90)
  left(90)
  forward(140)
  circle(-20, 180)
  forward(20)
  left(90)
  forward(40)
  left(90)
  forward(20)
  circle(-20, 180)
  forward(140)
  circle(-60, 180)
  forward(100)
  end_fill()
  penup()
  pencolor('cyan')
  right(90)
  forward(120)
  right(90)
  forward(100)
  pendown()
  fillcolor('cyan')
  begin_fill()
  right(90)
  forward(50)
  circle(-15, 180)
  forward(50)
  circle(-15, 180)
  end_fill()

posX = -450
posY = 350
while posY >= -400:
    penup()
    goto(posX, posY)
    pendown()
    amogus('red')
    posX += 200
    if posX > 650:
        posX = -450
        posY -= 250

exitonclick()