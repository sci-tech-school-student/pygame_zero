import pgzrun

# from pygame import mous

TITLE = 'game'
WIDTH = 800
HEIGHT = 600

bird = Actor('bird0', (100, 300))
pos_ =()

def on_mouse_move(pos):
    global pos_
    bird.x += 1
    pos_ = pos


def draw():
    screen.fill((255, 100, 255))
    bird.draw()
    screen.draw.text(f'Bird-X: {bird.x}, Mouse: {pos_}', (10, 10))


def update():
    screen.draw.text(f'Bird-X: {bird.x}, Mouse: {pos_}', (10, 10))


pgzrun.go()
