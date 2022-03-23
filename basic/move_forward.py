import pgzrun
from pgzhelper import *

TITLE = 'sample'
WIDTH = 800
HEIGHT = 600

x, y = 30, 30
bird = Actor('bird1', (x, y))
# bird.flip_x = True

enemy = Actor('birddead', (400, 300))


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
    enemy.draw()


def update():
    screen.clear()
    bird_move()
    bird.angle = bird.angle_to(enemy)
    bird.move_forward(1)



pgzrun.go()
