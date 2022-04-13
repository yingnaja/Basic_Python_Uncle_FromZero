import sys
print(sys.version)

import turtle
tao = turtle.Pen()
tao.shape('turtle')
   
def RectangleRight(z):
    for i in range(4):
        tao.forward(z)
        tao.right(90)

def RectangleLeft(z):
    for i in range(4):
        tao.forward(z)
        tao.left(90)

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

RectangleRight(100)
Go(100,50)
RectangleRight(50)
Go(150,100)
RectangleRight(50)
Go(200,200)
RectangleRight(100)
Go(0,-100)

RectangleLeft(300)




