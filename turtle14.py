#!/usr/bin/python3
import turtle
n=int(input())
turtle.left(180)
def star():
    for i in range (n):
        turtle.forward(80)
        turtle.left(360/n*2)
turtle.update()
star()
turtle.mainloop()

