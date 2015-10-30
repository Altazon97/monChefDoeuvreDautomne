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
import time

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
t.bgcolor("#b27e1e")

#shoulder in the corner
t.pensize(5)
pos(-350, -350)
t.begin_fill()
drawLine(100, 45)
drawLine(30, -60)
drawLine(89, -120)
drawLine(37, -45)
t.color('gray')
t.end_fill()

#more hands
pos(-250, -288)
t.begin_fill()
drawLine(50, -150)
drawLine(70, -80, "")
drawLine(52, -90)
drawLine(112, -40)
t.fillcolor('#315e27')
t.end_fill()

#draw the stuff on the bottom
t.right(175)
pos(-205, -350)
t.begin_fill()
drawLine(70, -5)
drawLine(110, 20)
drawLine(45, 90)
drawLine(125, 92)
drawLine(50, 18)
t.fillcolor('#40E0D0')
t.end_fill()

t.left(320)
pos(-20, 47)
t.pencolor('black')
t.begin_fill()
t.right(39.5)
t.circle(250, 70)
drawCurl(20, 5, +1)
drawCurl(15, 20, +1)
t.fillcolor('#c289d3')
t.end_fill()

#draw the face outline and fill it
pos(-140, -325)
t.left(236)
t.begin_fill()
drawCurl(15)
drawParabola(11)
t.left(-80)
drawCurl(10, 20)
t.circle(50, 50)
t.left(215)
drawParabola(8, +1)
drawCurl(25, 1, +1)
t.right(90)
drawCurl(5, 1)
drawCurl(24, 11.7)
t.fillcolor('#40E0D0')
t.end_fill()

pos(-262, 35)
drawCurl(20, 3, +1)
drawCurl(15, 12, +1)
drawCurl(5, 23, +1)
drawLine(9)

pos(-22, 47)
drawLine(250, -40)
drawLine(50, -80)
pos(-220, -30)
t.left(120)
drawCurl(40, 4, +1)

#begin oulining the same area again, to fill for lighter green!
t.pencolor("")
t.left(208)
pos(-140, -325)
t.left(236)
drawCurl(15)
drawParabola(11)
t.left(-80)
drawCurl(10, 20)
t.circle(50, 50)
t.left(215)
#fill from this spot right here
t.begin_fill()
drawParabola(8, +1)
drawCurl(25, 1, +1)
t.right(90)
drawCurl(5, 1)
drawCurl(24, 11.7)
t.fillcolor("#ceefee")
t.end_fill()

#re-outline the nose
pos(-22, 47)
drawLine(250, 60)
drawLine(50, -80)

#right eye
pos(-60, -120)
t.left(-260)
t.circle(25, 160)

#fill under the nose
pos(-150, -183)
t.begin_fill()
drawLine(135, 205, "")
drawLine(130, 155, "")
drawLine(55, 100, "")
t.fillcolor("#ceefee")
t.end_fill()


#draw the mouth
t.pencolor('black')
pos(-165,-230)
t.right(185)
t.pensize(7)
drawParabola(6, +1)
pos(-155,-245)
t.right(7)
t.pensize(3)
drawParabola(5, +1)

#finish up the bottom now
t.pensize(5)
pos(-170, -350)
t.begin_fill()
drawLine(160, -5)
drawLine(45, 120)
drawLine(110, 80)
t.fillcolor('#ceefee')
t.end_fill()

#hair strand
t.pensize(7)
pos(-362, -70)
t.right(120)
drawCurl(16, 8)

#draw the fingers
t.pensize(5)
pos(-275, -350)
drawLine(15, 90)
pos(-225, -350)
drawCurl(13, 2, +1)
pos(-210, -350)
t.left(-50)
t.begin_fill()
drawCurl(7, 7, +1)
t.right(155)
drawLine(52)
t.right(115)
drawLine(27)
t.fillcolor("#ce3737")
t.end_fill()
pos(-170, -320)
t.right(83)
drawLine(24)
t.circle(8, 180)
drawLine(24, 5)

#finish up that last hair outline

pos(-277, -275)
drawLine(75, 100)


#display the work of art
done()
