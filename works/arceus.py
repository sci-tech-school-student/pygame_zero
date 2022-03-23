import random
from pgzhelper import *
import pygame

TITLE = 'clone'
# width:幅, wide:幅がある
WIDTH = 800
# height:高さ, high:高い
HEIGHT = 600
# bg : background 背景
bg = Actor('arceus_bg')

arceus = Actor('arceus', (100, 300))
arceus.is_shootable = True
arceus_image = pygame.image.load('images/arceus.png')
arceus_image.convert_alpha()
colored_arceus = arceus_image.copy()

comets = []
power_balls = []

palkia = Actor('palkia', (200, 200))
palkia.goal_x = 500
palkia.goal_y = 500
palkia.hp = 100

dialga = Actor('dialga', (200, 400))
dialga.goal_x = 300
dialga.goal_y = 300
dialga.hp = 100
enemies = [palkia, dialga]

textbox_pos = Rect(600, 0, 150, 80)


def draw():
    bg.draw()
    screen.draw.textbox(f'Palkia HP:{palkia.hp} Dialga HP:{dialga.hp}', textbox_pos)
    arceus.draw()
    palkia.draw()
    dialga.draw()
    for comet in comets:
        comet.draw()
    for power_ball in power_balls:
        power_ball.draw()


def move_arceus():
    if keyboard.w:
        arceus.y -= 10
        if arceus.y <= 0:
            arceus.y += 10
    elif keyboard.s:
        arceus.y += 10
        if arceus.y >= HEIGHT:
            arceus.y -= 10
    if keyboard.d:
        arceus.x += 10
        arceus.flip_x = False
        if arceus.x >= WIDTH:
            arceus.x -= 10
    elif keyboard.a:
        arceus.x -= 10
        arceus.flip_x = True
        if arceus.x <= 0:
            arceus.x += 10


def set_shootable():
    arceus.is_shootable = True


def shoot_comet():
    if keyboard.space and arceus.is_shootable:
        sounds.shoot.play()
        arceus.is_shootable = False
        comet = Actor('comet')
        comet.scale = 0.5  # change size
        comet.y = arceus.y
        if arceus.flip_x:
            comet.x = arceus.x - 100
            comet.flip_x = True
        else:
            comet.x = arceus.x + 100
            comet.flip_x = False
        comets.append(comet)
        clock.schedule_unique(set_shootable, sounds.shoot.get_length())


def move_comet():
    for comet in comets:
        if arceus.flip_x:
            comet.flip_x = True
            comet.x -= 10
            if comet.x <= 50:
                comets.remove(comet)
        else:
            comet.flip_x = False
            comet.x += 10
            if comet.x >= 700:
                comets.remove(comet)


def shoot_power_ball():
    if keyboard.b and len(power_balls) == 0:
        power_ball = Actor('power_ball', (arceus.x, arceus.y))
        power_ball.scale = 0.5
        power_balls.append(power_ball)


def move_power_ball():
    for power_ball in power_balls:
        power_ball.move_towards(palkia, 3)

        if keyboard.r:
            power_ball.reset_effects()
        elif keyboard.t:
            power_ball.set_color_effect(255, 0, 0)
        elif keyboard.y:
            power_ball.change_ghost_effect(-10)

        if power_ball.colliderect(palkia):
            power_balls.remove(power_ball)
            palkia.hp -= 25


def set_direction(sprite, new_x, old_x):
    if new_x - old_x > 0:
        sprite.flip_x = False
    else:
        sprite.flip_x = True


def move_enemy(enemy):
    if enemy.x >= enemy.goal_x * 0.9 and \
            enemy.y >= enemy.goal_y * 0.9:
        enemy.goal_x = random.randrange(0, 800)  # 600 -> 540
        enemy.goal_y = random.randrange(0, 600)  # 400
        set_direction(enemy, enemy.goal_x, enemy.x)
    animate(enemy, duration=1, pos=(enemy.goal_x, enemy.goal_y))


def damage_enemy(enemy):
    for comet in comets:
        if enemy.colliderect(comet):
            enemy.hp -= 5
            comets.remove(comet)
            if enemy.hp <= 0:
                enemies.remove(enemy)
                enemy.scale = 0


def game_over(enemy):
    pass


def update():
    bg.draw()
    screen.draw.textbox(f'Palkia HP:{palkia.hp}  Dialga HP:{dialga.hp}', textbox_pos)
    move_arceus()
    move_comet()
    move_power_ball()
    shoot_comet()
    shoot_power_ball()

    for enemy in enemies:
        move_enemy(enemy)
        damage_enemy(enemy)
