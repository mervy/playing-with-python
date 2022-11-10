# https://seongjuhong.com/2019-06-25am-how-to-draw-random-flower-with-python-turtle/

from random import randrange
from turtle import Turtle, Screen

MAX_ANGLE = 30
MAX_DISTANCE = 250

def jaggedLine (turtle, pieceLength):
    randomColor(turtle)

    while turtle.distance(0,0) < MAX_DISTANCE:
        angle = randrange(-MAX_ANGLE, MAX_ANGLE +1)
        turtle.right(angle)
        turtle.forward(pieceLength)

def jumToCenter(turtle):
    turtle.penup()
    turtle.home()
    turtle.pendown()

def randomColor(turtle):
    r = randrange(255)
    g = randrange(255)
    b = randrange(255)

    turtle.pencolor(r, g, b)

def main():
    s = Screen()
    s.colormode(255)
    t = Turtle()
    t.speed('fastest') # because I have no patience

    for angle in range (0, 360, 2):
        jumToCenter(t)
        t.setheading(angle)
        jaggedLine(t, 30)

    t.hideturtle()

    s.mainloop()

if __name__ == "__main__":
    main()