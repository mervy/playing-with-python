from turtle import *

def drawFlake(length, depth):
    "draws a flake"
    if depth > 0:
        for _ in range(6):
            forward(length)
            drawFlake(length // 3, depth - 1)
            backward(length)
            left(60)

drawFlake(200,4)