import pgzrun

TITLE = 'game'
WIDTH = 800
HEIGHT = 600


bird = Actor('bird0', (100, 300))
box = Rect((500, 300), (50, 50))


def draw():
    screen.clear()
    bird.draw()
    screen.draw.filled_rect(box, 'orange')


def update():
    bird.x += 5
    if bird.colliderect(box):
        sounds.bell_toll.play()
        clock.schedule_interval(exit, sounds.bell_toll.get_length())

pgzrun.go()
