import pgzrun

TITLE = 'game'
WIDTH = 800
HEIGHT = 600

bird = Actor('bird0', (400, 50))
birds = ['bird0', 'bird1', 'bird2']
bird.last_idx = 0
bird.vx, bird.vy = 1, 1


def draw():
    screen.clear()
    bird.draw()


def physics():
    bird.vy += 1


def update():
    physics()
    bird.y += bird.vy
    print(f'Y:{bird.y}  vy:{bird.vy}')


def animation_():
    bird.image = birds[bird.last_idx]
    if bird.last_idx < len(birds) - 1:
        bird.last_idx += 1
    else:
        bird.last_idx = 0


clock.schedule_interval(animation_, 0.1)
pgzrun.go()
