import pgzrun

# from pygame import mous

TITLE = 'game'
WIDTH = 800
HEIGHT = 600

pos_ = ()
box_size = [40, 20]


def on_mouse_move(pos):
    global pos_
    pos_ = pos


def draw():
    screen.fill((255, 100, 255))
    screen.draw.textbox(f'Mouse: {pos_}', Rect(10, 10, *box_size))


def update():
    screen.draw.textbox(f'Mouse: {pos_}', Rect(10, 10, *box_size))


pgzrun.go()
