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
import math as m
import turtle as t
from turtle import *
from math import *


def drawShape(shapeType, size, fillColor, colorOfPen, positionx = None, positiony = None, angle = 120, direction = 'forward'):
    t.penup()
    if positionx != None and positiony != None:
        t.setpos(positionx, positiony)
    t.pendown()
    t.pencolor(colorOfPen)
    t.fillcolor(fillColor)
    t.begin_fill()
    if shapeType == 'circle':
        drawCircle(size)
    elif shapeType == 'triangle':
        drawTriangle(size, angle)
    elif shapeType == 'octagon':
        drawOctagon(size)
    elif shapeType == 'rectangle':
        drawRectangle(size)
    elif shapeType == 'square':
        drawSquare(size)
    elif shapeType == 'decagon':
        drawDecagon(size)
    elif shapeType == 'parallelogram':
        drawParallelogram(size, angle)
    elif shapeType == 'parallelogram1': # for determining position
        drawParallelogram1(size, angle)
    elif shapeType == 'curl':
        drawCurl(size, direction)
    t.end_fill()

def drawCircle(size):
    t.circle(size)

def drawTriangle(size, angle):
    for i in range(3):
        t.forward(size)
        t.left(angle)

def drawParallelogram(size, angle):
    for i in range (2):
        t.forward(size)
        t.left(angle)
        t.forward(size)
        t.left(180 - angle)

def drawParallelogram1(size, angle):  #for determining position
    for i in range (1):
        t.forward(size)
        t.left(angle)
        t.forward(size)
        t.left(180 - angle)
        t.forward(size)

def drawOctagon(size):
    for i in range(8):
        t.left(45)
        t.forward(size)

def drawRectangle(size):
    for i in range(2):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.left(90)
        t.forward(size)

def drawSquare(size):
    for i in range(2):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.left(90)

def drawDecagon(size):
    for i in range(10):
        t.left(36)
        t.forward(size)

def drawCurl(size, direction = 'forward'):
    for i in range(size):
        t.left(-1 * m.sqrt(i))
        if direction == 'forward':
            t.forward(5)
        elif direction == 'backward':
            t.backward(5)

def drawLine(length = 50, direction = 0):
    t.pencolor('black')
    t.left(direction)
    t.forward(length)

def drawParabola(size):
    for i in range(size):
        t.left(-1 * i)
        t.forward(m.pow(i, 2))

def pos(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()

def move(size):
    t.penup()
    t.forward(size)
    t.pendown()


#MAIN
tracer(delay = None)
t.shape("turtle")
t.pensize(5)

# Draw Head and neck 
t.left(-30)
drawShape('parallelogram', 200, "green4", 'black', positionx = 0, positiony = 10, angle = 85)
move(200)
drawShape('parallelogram', 200, "green4", 'black', angle = -130)
move(200)

# Draw right shoulder
t.fillcolor('yellow')
t.begin_fill()
drawCurl(18)
t.goto(158.47,-258.40)
t.end_fill()


# Draw left side
t.fillcolor('yellow')
t.begin_fill()
t.goto(28,-258.40)
t.goto(-14.73,-158.40)
t.goto(158.47,-258.40)
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
