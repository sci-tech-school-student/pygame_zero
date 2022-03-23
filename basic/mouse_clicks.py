import pgzrun

# from pygame import mous

TITLE = 'game'
WIDTH = 800
HEIGHT = 600

bird = Actor('bird0', (100, 300))


def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        bird.x += 5


def draw():
    screen.clear()
    bird.draw()


pgzrun.go()
