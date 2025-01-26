from random import randint
import turtle as t
t.colormode(255)
t.speed(0)
for i in range(360):
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))
    t.pensize(1)
    t.circle(100)
    t.left(1)