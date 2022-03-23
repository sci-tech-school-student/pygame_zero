import pgzrun

TITLE = 'game'
WIDTH = 800
HEIGHT = 600

bird = Actor('bird0', (400, 300))


def draw():
    screen.clear()
    bird.draw()


def update():
    bird.x += 2
    if bird.x >= 700:
        animate(bird, duration=1, pos=(100, 100))


pgzrun.go()
