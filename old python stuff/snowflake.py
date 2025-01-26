from turtle import *
shape("classic")
speed(10)
pencolor("white")
pensize(13)
Screen().bgcolor("aquamarine")
def vshape():
    right(25)
    forward(125)
    backward(125)
    left(50)
    forward(125)
    backward(125)
    right(25)
def snowflakeArm():
    for x in range(0, 5):
        forward(80)
        vshape()
    backward(400)
def snowflake():
    for x in range(0, 10):
        snowflakeArm()
        right(36)
snowflake()
