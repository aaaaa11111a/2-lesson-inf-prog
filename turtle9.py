#!/usr/bin/python3
import turtle
import math
r=40
def figura(n,r):
    turtle.penup()
    turtle.goto(r,0)
    turtle.pendown()
    turtle.left(90+180/n)
    a=2 * r * math.sin(math.pi / n)
    for i in range (n):
        turtle.forward(a)
        turtle.left(360/n)
    turtle.right(90+180/n)
    turtle.penup()
    turtle.goto(r,0)
    turtle.pendown()
for i in range (10):
    n=3+i
    r=r+20
    figura(n,r)







