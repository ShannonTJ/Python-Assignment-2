#Shannon TJ 10101385
#This program reads mathematical expressions from the user and displays them on a graph

from SimpleGraphics import *
from math import *

#Store numeric constants in variables

POS_GRIDUNIT = 30
NEG_GRIDUNIT = -30
HALF_WIDTH = 400
HALF_HEIGHT = 300
UPPER_BOUND = 15
LOWER_BOUND = 1

background("white")

#Draw the x and y axes

line(0,HALF_HEIGHT, 2*HALF_WIDTH,HALF_HEIGHT)
line(HALF_WIDTH,2*HALF_HEIGHT, HALF_WIDTH,0)

#Draw the tickmarks on the axes

x = 0
for i in range(LOWER_BOUND,UPPER_BOUND):
  x = x + 1
  screenX = POS_GRIDUNIT*x + HALF_WIDTH
  line(screenX,HALF_HEIGHT - 5, screenX,HALF_HEIGHT + 5)
  screenX2 = NEG_GRIDUNIT*x + HALF_WIDTH
  line(screenX2,HALF_HEIGHT - 5, screenX2,HALF_HEIGHT + 5)

y = 0
for i in range(LOWER_BOUND,UPPER_BOUND):
  y = y + 1
  screenY = POS_GRIDUNIT*y + HALF_HEIGHT
  line(HALF_WIDTH - 5,screenY, HALF_WIDTH + 5,screenY)
  screenY2 = NEG_GRIDUNIT*y + HALF_HEIGHT
  line(HALF_WIDTH - 5,screenY2, HALF_WIDTH + 5,screenY2)

#Label the tickmarks

x = 0
label1 = 0 
label2 = 0
for i in range(LOWER_BOUND,UPPER_BOUND):
  x = x + 1
  label1 = label1 + 1
  screenX = POS_GRIDUNIT*x + HALF_WIDTH
  setFont("Times", "12")
  text(screenX, HALF_HEIGHT + 15, label1)
  label2 = label2 - 1
  screenX2 = NEG_GRIDUNIT*x + HALF_WIDTH
  text(screenX2, HALF_HEIGHT + 15, label2)

y = 0
label3 = 0
label4 = 0
for i in range(LOWER_BOUND,UPPER_BOUND):
  y = y + 1
  label3 = label3 + 1
  screenY = NEG_GRIDUNIT*y + HALF_HEIGHT
  setFont("Times", "12")
  text(HALF_WIDTH + 17,screenY, label3)
  label4 = label4 - 1
  screenY2 = POS_GRIDUNIT*y + HALF_HEIGHT
  text(HALF_WIDTH + 17,screenY2, label4)

#Prompt the user to enter a mathematical expression
#Count the number of expressions the user inputs

expr = (input("Enter a mathematical expression (blank line to exit): "))
color_counter = 1

while expr != "":
  x = -UPPER_BOUND

#Draw the expression

  while x < UPPER_BOUND:
    y = eval(expr)
    screenX = POS_GRIDUNIT*x + HALF_WIDTH
    screenY = NEG_GRIDUNIT*y + HALF_HEIGHT
    x = x + 0.1
    y = eval(expr)
    screenX2 = POS_GRIDUNIT*x + HALF_WIDTH
    screenY2 = NEG_GRIDUNIT*y + HALF_HEIGHT

#Change the line color based on how many expressions the user inputs

    if color_counter % 3 == 1:
      setOutline(255, 0, 0)
      line(screenX,screenY, screenX2,screenY2)

    elif color_counter % 3 == 2:
      setOutline(0, 255, 0)
      line(screenX,screenY, screenX2,screenY2)

    else:
      setOutline(0, 0, 255)
      line(screenX,screenY, screenX2,screenY2)

  expr = (input("Enter a mathematical expression (blank line to exit): "))
  color_counter = color_counter + 1

#Close the window if the user enters a blank line

close()
