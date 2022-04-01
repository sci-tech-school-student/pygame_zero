import pgzrun
import random
from pgzhelper import *

TITLE = 'clone'
# width:幅, wide:幅がある
WIDTH = 800
# height:高さ, high:高い
HEIGHT = 600
# bg : background 背景
bg = Actor('arceus_bg')
bg.is_sound_end = False

arceus = Actor('arceus', (100, 300))
arceus.is_shootable = True
arceus.vx = arceus.vy = 5
arceus.is_cleared = False
arceus.is_over = False

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

game_clear = Actor('game_clear', (WIDTH // 2, -100))
game_over = Actor('game_over', (WIDTH // 2, HEIGHT // 2))
game_over.opacity = 0


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
    game_clear.draw()
    game_over.draw()


def move_arceus():
    if keyboard.w:
        arceus.y -= arceus.vy
        if arceus.y <= 0:
            arceus.y += arceus.vy
    elif keyboard.s:
        arceus.y += arceus.vy
        if arceus.y >= HEIGHT:
            arceus.y -= arceus.vy
    if keyboard.d:
        arceus.x += arceus.vx
        arceus.flip_x = False
        if arceus.x >= WIDTH:
            arceus.x -= arceus.vx
    elif keyboard.a:
        arceus.x -= arceus.vx
        arceus.flip_x = True
        if arceus.x <= 0:
            arceus.x += arceus.vx

    if keyboard.r:
        arceus.reset_effects()
    elif keyboard.t:
        arceus.rgb = [255, 0, 0]
    elif keyboard.y:
        arceus.rgb = [0, 0, 250]
    elif keyboard.u:
        arceus.opacity = 50
    elif keyboard.i:
        arceus.opacity = 100
    elif keyboard.j:
        arceus.change_opacity_by(10)
    elif keyboard.k:
        arceus.change_opacity_by(-10)


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
            comet.x = arceus.x
            comet.flip_x = True
        else:
            comet.x = arceus.x
            comet.flip_x = False
        comets.append(comet)
        clock.schedule_unique(set_shootable, sounds.shoot.get_length())


def damage_enemy(comet):
    for enemy in enemies:
        if enemy.colliderect(comet):
            enemy.hp -= 5
            comets.remove(comet)
            if enemy.hp <= 0:
                enemies.remove(enemy)
                enemy.scale = 0
                enemy.hp = 0


def move_comet():
    for comet in comets:
        if comet.flip_x:
            comet.x -= 10
            if comet.x <= 50:
                comets.remove(comet)
        else:
            comet.x += 10
            if comet.x >= 700:
                comets.remove(comet)
        damage_enemy(comet)


def shoot_power_ball():
    if keyboard.b and len(power_balls) == 0:
        power_ball = Actor('power_ball', (arceus.x, arceus.y))
        power_ball.scale = 0.5
        power_balls.append(power_ball)


def move_power_ball():
    for power_ball in power_balls:
        power_ball.move_towards(palkia, 3)

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


def _damage_animation(enemy):
    for i in range(60):
        enemy.rgb = [200, 200, 200]
        enemy.reset_effects()


def _is_sound_end():
    bg.is_sound_end = True
    exit()


def check_game_clear():
    if len(enemies) == 0 and not bg.is_sound_end and not arceus.is_cleared:
        arceus.is_cleared = True
        sounds.clear.play()
        animate(game_clear, duration=1, pos=(WIDTH // 2, HEIGHT // 2))
        clock.schedule_unique(_is_sound_end, sounds.clear.get_length())


def check_game_over(enemy):
    if arceus.colliderect(enemy) and not bg.is_sound_end and not arceus.is_over:
        arceus.is_over = True
        sounds.bell_toll.play()
        clock.schedule_unique(_is_sound_end, sounds.bell_toll.get_length())
    if not bg.is_sound_end and arceus.is_over:
        game_over.change_opacity_by(3)


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
        check_game_over(enemy)

    check_game_clear()
