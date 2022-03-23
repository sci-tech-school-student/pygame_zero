import pgzrun

TITLE = 'game'
WIDTH = 400
HEIGHT = 600

bg = Actor('background')

def draw():
    screen.clear()
    bg.draw()

def update():
    pass

pgzrun.go()
