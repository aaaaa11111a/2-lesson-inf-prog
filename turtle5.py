#!/usr/bin/python3
import turtle
n=20
for i in range (0,10):
    for j in range (0,4):
        turtle.forward(n)
        turtle.left(90)
    turtle.penup()
    turtle.left(180)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()
    n=n+20


