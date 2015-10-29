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

def drawCurl(size, bend = 1, direction = -1):
    t.pencolor('black')
    for i in range(size):
        t.left(direction * math.sqrt(i))
        t.forward(bend)

def drawCurve():  #square root function
    for i in range(50):
        t.left(90)
        t.forward(math.sqrt(i))
        t.right(90)
        t.forward(i)

def drawLine(length, direction = 0, color='black', width = 1):
    t.pencolor(color)
    t.left(direction)
    t.forward(length)

def drawParabola(size, direction = -1):
    for i in range(size):
        t.left(direction * i)
        t.forward(math.pow(i, 2))

def pos(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()

#MAIN
pos(-350, -350)
t.begin_fill()
drawLine(100, 45)
drawLine(30, -60)
drawLine(89, -120)
drawLine(37, -45)
t.color('gray')
t.end_fill()

pos(-250, -288)
t.begin_fill()
drawLine(50, -150)
drawLine(70, -80, "")
drawLine(52, -90)
drawLine(112, -40)
t.color('green')
t.end_fill()

pos(-140, -325)
drawCurl(15)
drawParabola(11)
t.left(-80)
drawCurl(10, 20)
t.circle(50, 50)
t.left(215)
drawParabola(8, +1)
drawCurl(25, 1, +1)
t.right(90)
drawCurl(5, +1)

#get the last of this face done!


#display the work of art
done()
