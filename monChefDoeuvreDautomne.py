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

def drawShape(shapeType, size, fillColor, colorOfPen, positionx = None, positiony = None):
    t.penup()
    if positionx != None and positiony != None:
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
    t.circle(size)

def drawTriangle():
    for i in range(3):
        t.forward(size)
        t.right(120)

def drawOctagon():
    for i in range(8):
        t.left(45)
        t.forward(size)

def drawRectangle():
    for i in range(2):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.left(90)
        t.forward(size)

def drawDecagon():
    for i in range(10):
        t.left(36)
        t.forward(size)

def drawCurl():
    for i in range(100):
        t.left(math.sqrt(i))
        t.forward(5)


def drawLine(length = 50, direction = 0, colour = 'black'):
    t.pencolor(colour)
    t.left(direction)
    t.forward(length)

def pos(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()

#MAIN
t.begin_fill()
pos(-300, -300)
drawLine(100, 45)
drawLine(25, -60)
drawLine(25, 60)
drawLine(115, -180)
drawLine(30, -45)
t.color('gray')
t.end_fill()

"""
for i in range(50):
    t.left(90)
    t.forward(math.sqrt(i))
    t.right(90)
    t.forward(i)
"""

#display the work of art
done()
