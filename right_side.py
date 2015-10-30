"""
monChefDoeuvreDautomne.py,

Eric Sund
Andy Zeng
Oct 29 2015

This program uses the Python Turtle Graphics Module in an attempt to draw a truncated version of Picasso's "Deux Enfants Lisant" painting.
The drawing will only feature the shoulders up, as shown in this image: 
http://www.lsa.umich.edu/UMICH/lsa/Home/LSA%20Today/2013/images/Picasso-1.jpg
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

t.tracer(n = None, delay = None)

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

def drawCurl(size, bend = 1, direction = -1):
    t.pencolor('black')
    for i in range(size):
        t.left(direction * sqrt(i))
        t.forward(bend)

def drawCurve():  #square root function
    for i in range(50):
        t.left(90)
        t.forward(math.sqrt(i))
        t.right(90)
        t.forward(i)

def drawLine(length = 50, direction = 0):
    t.pencolor('black')
    t.left(direction)
    t.forward(length)

def drawParabola(size):
    for i in range(size):
        t.left(-1 * i)
        t.forward(m.pow(i, 2))

def eyes(x,y,radius,size=2):
    pos(x,y)
    t.fillcolor('black')
    t.begin_fill()
    x = x - radius  # our chosen position is the top right edge
    for i in range(60):  #over 60 slices
        t.goto(x+radius*cos(i*pi/60), y - radius*sin(i*pi/60))
    for i in range(60):  #over 60 slices
        t.goto(x-radius*cos(i*pi/60), y - radius/size*sin(i*pi/60))
    t.end_fill()

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
t.bgcolor('#BB8228')

# Draw the right hair
pos(115,145)            # Starting point
t.left(5)               ### ASSUMES THAT WE START ENTIRELY FACING RIGHT
t.begin_fill()
drawCurl(33, 15, -1)
t.goto(346.41,-190.00)  # End by shoulder
t.goto(215,-37)         # Close the shape
t.fillcolor('#723D39')
t.end_fill()
t.left(70)
pos(287.92,73.83)       # Start at right edge of face
drawCurl(16, 10, -1)    # Groove in her hair
t.goto(346.41,-190.00)  # End by shoulder

# Draw the left hair
pos(115,145)            # Starting point          
t.right(150)            
t.begin_fill()
drawCurl(20, 5, +1)     # Initial curve for hair 
drawCurl(22, 3, +1)     # Tight turn 
drawCurl(21, 7, +1)     # Smooth out the curve
t.goto(0,10)            # End at left edge of face
t.fillcolor('#723D39')
t.end_fill()

# Draw Head and neck
pos(0,10)
t.fillcolor('#698066')
t.begin_fill()
t.goto(173.21,-90.00)   # Using goto(x,y) for head because parallelogram is entirely assymetrical 
t.goto(287.92,73.83)
t.goto(80,160)
t.goto(0,10)
t.end_fill()
pos(173.21,-90.00)      # Return to the chin in order to draw neck
t.left(24)
drawShape('parallelogram', 200, '#698066', 'black', angle = -130)   # Neck; may as well use the function
move(200)

# Draw right shoulder
t.fillcolor('#E1D849')
t.begin_fill()
drawCurl(18,5)          # End at same horizontal plane as parallelogram
t.goto(158.47,-258.40)  # Close shape at bottom of parallelogram
t.end_fill()

# Draw left shoulder
t.fillcolor('#E1D849')
t.begin_fill()
t.goto(40,-258.40)      # End at girl on the left
t.goto(-14.73,-158.40)  # End at left edge of parallelogram 
t.end_fill()

# Draw the eyes
eyes(85,40,30,1.2)
eyes(260,80,30,1.2)

# Draw the Nose
pos(115,145)
t.goto(100,-15)
t.goto(140,0)

# Draw the Mouth
pos(135, -40)
t.goto(175, -30)

# Hide the turtle
ht()

# Display the work of art
done()
