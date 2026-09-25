#!/usr/bin/python3
import turtle
import math
turtle.shape('turtle')
a=2
for i in range (1000):
    phi=i*0.05
    r=a*phi
    x=r*math.cos(phi)
    y=r*math.sin(phi)
    turtle.goto(x,y)
    turtle.mainloop()

