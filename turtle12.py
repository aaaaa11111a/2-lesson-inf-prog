#!/usr/bin/python3
import turtle
def smcircle ():
    n=200
    for i in range (n):
        turtle.forward(0.1)
        turtle.right(180/n)
    turtle.update()
def lacircle():
    n=200
    for j in range (n):
        turtle.forward(1)
        turtle.right(180/n)
    turtle.update()
turtle.tracer(False)
turtle.shape('turtle')
N=5
turtle.left(90)
for i in range (N):
    lacircle()
    smcircle()
turtle.mainloop()



