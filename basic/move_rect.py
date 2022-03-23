import pgzrun
import random

TITLE = 'game'
WIDTH = 800
HEIGHT = 600

box = Rect((500, 100), (50, 50))
box_2 = Rect((150, 20), (1, 450))
radius = 50


def draw():
    screen.clear()
    screen.draw.filled_rect(box_2, 'gray')
    screen.draw.filled_rect(box, 'orange')
    screen.draw.filled_circle((250, 100), radius, 'red')


def update():
    global radius
    box.x += 2
    box_2.y += 2
    radius += 1
    screen.draw.filled_circle((250, 100), radius, 'red')

pgzrun.go()
