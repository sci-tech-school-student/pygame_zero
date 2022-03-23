import pgzrun
import random

TITLE = 'game'
WIDTH = 800
HEIGHT = 600


def draw():
    screen.clear()
    screen.draw.circle((250, 250), 50, 'white')
    screen.draw.filled_circle((250, 100), 50, 'red')
    screen.draw.line((150, 20), (150, 450), 'gray')
    screen.draw.line((150, 20), (350, 20), 'gray')
    screen.draw.filled_rect(Rect((500, 100), (50, 50)), 'orange')


pgzrun.go()
