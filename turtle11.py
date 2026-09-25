#!/usr/bin/python3
import turtle
def circle(direction='left', a=1):
    n=200
    for i in range (n):
        turtle.forward(a)
        if direction=='left':
            turtle.left(360/n)
        elif direction=='right':
            turtle.right(360/n)
        else:
            print('Error')
            return
    turtle.update()
def eight(a):
    circle('left', a)
    circle('right', a)
turtle.tracer(False)
turtle.shape('turtle')
turtle.left(90)
N=10
for i in range(N):
    eight(1+i/10)
turtle.mainloop()
