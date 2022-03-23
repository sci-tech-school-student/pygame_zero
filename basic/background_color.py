import pgzrun

# from pygame import mous

TITLE = 'game'
WIDTH = 800
HEIGHT = 600

bird = Actor('bird0', (100, 300))
color = (255, 255, 255)

def on_mouse_move(pos):
    bird.x += 1


def draw():
    screen.fill(color)
    bird.draw()


pgzrun.go()
