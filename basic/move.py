import pgzrun
import random

TITLE = 'sample'
WIDTH = 800
HEIGHT = 600

x, y = 30, 30
bird = Actor('bird1', (x, y))


def bird_move():
    if keyboard.d:
        bird.x += 2
    elif keyboard.a:
        bird.x -= 2
    if keyboard.w:
        bird.y -= 2
    elif keyboard.s:
        bird.y += 2


def draw():
    bird.draw()


def update():
    screen.clear()
    bird_move()


pgzrun.go()
