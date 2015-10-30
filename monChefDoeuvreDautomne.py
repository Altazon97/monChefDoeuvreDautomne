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
import math
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

def drawRectangle(x, y):
    t.forward(x)
    t.right(90)
    t.forward(y)
    t.right(90)
    t.forward(x)
    t.right(90)
    t.forward(y)

def drawCurl(size, bend = 1, direction = -1):
    t.pencolor('black')
    for i in range(size):
        t.left(direction * sqrt(i))
        t.forward(bend)

"""
def drawCurve():  #square root function
    for i in range(50):
        t.left(90)
        t.forward(math.sqrt(i))
        t.right(90)
        t.forward(i)
"""

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

def drawSquare(size):
    for i in range(2):
        t.forward(size)
        t.right(90)
        t.forward(size)
        t.right(90)

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

def drawLine(length, direction = 0, color='black'):
    t.pencolor(color)
    t.left(direction)
    t.forward(length)

def drawParabola(size, direction = -1):
    for i in range(size):
        t.left(direction * i)
        t.forward(math.pow(i, 2))

#MAIN
t.bgcolor("#b27e1e")

#begin drawing the left girl - coded by Eric

t.speed(50)
t.shape("turtle")

#Prepare an area for colour fill at the end
pos(-25, 50)
t.pencolor("") #outline the fill colour area
t.begin_fill()
drawSquare(200)
t.fillcolor("#ceefee")
t.end_fill()

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
t.fillcolor('#698066')
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

#end of the left girl

#begin drawing the right girl - coded by Andy

t.tracer(n = None, delay = None)

#MAIN
tracer(delay = None)
t.pensize(5)

# Draw the right hair
t.penup()
t.home()
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

#draw the credits
t.penup()
t.home()
pos(20, -275)
drawRectangle(300, 75)
t.register_shape("credits.gif")


"""
# Hide the turtle
ht()
"""

# Display the work of art
done()
