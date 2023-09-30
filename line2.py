from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
daco_character = load_image('Daco.png')
hand_character = load_image('hand_arrow')

# def stop():
#     turtle.bye()
hx1 = random.randint(0, 1280)
hy1 = random.randint(0, 1024)
hx2, hy2 = 0, 0
hand_point = [hx1, hy1, hx2, hy2]
catch = False
running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0  # 0,1 좌우
frame2 = 0  # 2,3 상하
dirx = 0
diry = 0


def draw_hand_arrow(x1, y1, x2, y2):
    while True:
        if catch:
            hand_character.draw(x1, y1)
        else:
            x2 = random.randint(0, 1280)
            y2 = random.randint(0, 1024)
            x1 = hx2
            y1 = hy2


def draw_daco_point(x1,y1):
    while True:
        if catch:
            clear_canvas()
            tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
            daco_character.clip_draw(frame * 121, 122, 121, 122, x1, y1, 120, 120)
            update_canvas()
            frame = (frame + 1) % 9
            delay(0.03)
        else


while running:

    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if x < 0:
        x = 0
    elif x > TUK_WIDTH:
        x = TUK_WIDTH

    if y < 0:
        y = 0
    elif y > TUK_HEIGHT:
        y = TUK_HEIGHT

    hand_character.draw(hx1, hy1)

    if catch:



    update_canvas()

    frame = (frame + 1) % 9
    frame2 = (frame2 + 1) % 7
    x += dirx * 8
    y += diry * 8
    delay(0.03)
