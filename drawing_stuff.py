#! python3
# drawing_stuff.py - Drawing squares using turtle. Nothing special really.

import turtle
import random

DIMENSIONS = 4
OFFSET = 5
turtle.speed('fastest')
color_change = 360 // OFFSET // 4
colors = ('black', 'white', 'red', 'blue', 'green', 'yellow')
color_index = 0

for angle_turn in range(360 // OFFSET):
        
        for i in range(DIMENSIONS):
                turtle.forward(100)
                turtle.left(90)
        turtle.right(OFFSET)

        turtle.color(colors[color_index])
        color_index += 1
        if color_index == len(colors):
                color_index = 0

turtle.exitonclick()
