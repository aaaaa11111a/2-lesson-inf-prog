#!/usr/bin/python3
import turtle
turtle.shape("turtle")
n=int(input())
for i in range (0,n):
    turtle.right(360/n)
    turtle.forward(50)
    stamp()
    turtle.right(180)
    turtle.forward(50)
    
