import pgzrun

TITLE = 'game'
WIDTH = 800
HEIGHT = 600

bird = Actor('bird0', (400, 300))
bullets = []
bird.set_shootable = True


def set_is_shootable():
    bird.set_shootable = True


def on_key_down(key):
    if bird.set_shootable:
        bullets.append(Actor('bird0', (bird.x, bird.y)))
        bird.set_shootable = False
        clock.schedule_unique(set_is_shootable, 1)


def draw():
    screen.clear()
    bird.draw()
    for bullet in bullets:
        bullet.draw()


def move_bullet():
    for bullet in bullets:
        bullet.x += 5
        if bullet.x >= 750:
            bullets.remove(bullet)


def update():
    move_bullet()


pgzrun.go()
