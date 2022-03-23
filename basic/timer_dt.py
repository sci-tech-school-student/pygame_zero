import pgzrun
import random
import math

TITLE = 'timer'
WIDTH = 500
HEIGHT = 500

time = 0
dt = 0

def text_():
    screen.draw.text(f'{math.floor(time)}', (0, 0))

def update(dt):
    global time
    timer += dt

def draw():
    screen.clear()
    screen.draw.text(f'{math.floor(time)}', (0, 0))

clock.schedule_interval(text_, 1)
