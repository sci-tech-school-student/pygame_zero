import pgzrun
import random

TITLE = 'angle'
WIDTH = 800
HEIGHT = 600

x, y = 30, 30
bird = Actor('bird1', (x, y))
bird_dead = Actor('birddead', (200, 150))


def draw():
    bird.draw()
    bird_dead.draw()


def update():
    screen.clear()
    bird.y += 2
    bird.angle = bird.angle_to(bird_dead)


pgzrun.go()
