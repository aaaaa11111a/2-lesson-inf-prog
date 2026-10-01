#!/usr/bin/python3
import turtle
n=int(input())
def star():
    for i in range (n):
        turtle.forward(150)
        turtle.left(180-180/n)
turtle.update()
star()
turtle.mainloop()

