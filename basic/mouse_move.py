import pgzrun

# from pygame import mous

TITLE = 'game'
WIDTH = 800
HEIGHT = 600

bird = Actor('bird0', (100, 300))


def on_mouse_move(pos):
    bird.x += 1


def draw():
    screen.clear()
    bird.draw()


pgzrun.go()
