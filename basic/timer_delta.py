import pgzrun
import random
import math

TITLE = 'timer'
WIDTH = 500
HEIGHT = 500

time = 20

def text_():
    screen.draw.text(f'{math.floor(time)}', (0, 0))

def update(delta):
    global time
    time -= delta
    print(time, delta)

def draw():
    screen.clear()
    screen.draw.text(f'{math.floor(time)}', (0, 0))

clock.schedule_interval(text_, 1)
