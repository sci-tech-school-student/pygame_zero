import pgzrun

TITLE = 'game'
WIDTH = 800
HEIGHT = 600

bird = Actor('bird0', (400, 300))
birds = ['bird0', 'bird1', 'bird2']
bird.last_idx = 0


def draw():
    screen.clear()
    bird.draw()


def update():
    bird.x += 2


def animation_():
    bird.image = birds[bird.last_idx]
    if bird.last_idx < len(birds) - 1:
        bird.last_idx += 1
    else:
        bird.last_idx = 0


clock.schedule_interval(animation_, 0.1)
pgzrun.go()
