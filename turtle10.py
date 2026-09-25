#!/usr/bin/python3
import turtle
def circle(direction= 'left'):
    n=200
    for i in range (n):
        turtle.forward(1)
        if direction=='left':
            turtle.left(360/n)
        elif direction=='right':
            turtle.right(360/n)
        else:
            print('Error')
            return
    turtle.update()
def eight():
    circle('left')
    circle('right')
turtle.tracer(False)
turtle.shape('turtle')
N=3
for i in range(N):
    eight()
    turtle.left(180/N)
turtle.mainloop()



