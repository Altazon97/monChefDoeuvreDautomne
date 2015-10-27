"""
monChefDoeuvreDautomne.py,

Eric Sund
Oct 23 2015

This program creates a drawing using the Python Turtle Graphics module.
"""

"""
> 20 shapes
> 6 colors
5 for loops
4 functions that have parameters
1 fruitful function
3 void functions

"""



import turtle as t
from turtle import *
from math import *
import math

def drawShape(fillColor, positionx, positiony, colorOfPen, shapeType):
    t.penup()
    t.setpos(positionx, positiony)
    t.pendown()
    t.begin_fill()
    t.pencolor(colorOfPen)
    if shapeType == 'circle':
        drawCircle()
    elif shapeType == 'triangle':
        drawTriangle()
    elif shapeType == 'octagon':
        drawOctagon()
    elif shapeType == 'rectangle':
        drawRectangle()
    elif shapeType == 'decagon':
        drawDecagon()
    t.color(fillColor)
    t.end_fill()

def drawCircle():
    t.circle(50)

def drawTriangle():
    for i in range(3):
        t.forward(100)
        t.right(120)

def drawOctagon():
    for i in range(8):
        t.left(45)
        t.forward(50)

def drawRectangle():
    for i in range(2):
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(100)

def drawDecagon():
    for i in range(10):
        t.left(36)
        t.forward(200)


"""
t.shape("turtle")
for i in range(100):
    t.left(math.sqrt(i))
    t.forward(5)

t.shape("turtle")
for i in range(100):
    t.left(90)
    t.forward(math.sqrt(i))
    t.right(90)
    t.forward(i)
"""


drawShape('blue', 100, -250, 'orange', 'decagon')
drawShape('pink', 25, -12.5, 'black', 'octagon')
drawShape('yellow', 0, 0, "black", 'circle')
drawShape('red', -50, 150, 'green', 'triangle')
drawShape('orange', 100, 100, 'pink', 'rectangle')


#display the work of art
done()
