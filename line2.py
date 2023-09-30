from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
daco_character = load_image('Daco.png')
hand_character = load_image('hand_arrow.png')


def tuk_canvas():
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)


def draw_hand(p):
    hand_character.draw_now(p[0], p[1])

def rightleft(p1,p2):
    global left,right

    if p2[0] > p1[0]:
        right = True
        left = False
    else:
        left = True
        right = False


def draw_line(p1, p2):
    rightleft(p1, p2)

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    for i in range(0, 101, 5):
        t = i / 100  # (0~1)까지
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2

        draw_daco((x, y))
        draw_hand(p2)


def draw_daco(p):
    clear_canvas()
    tuk_canvas()
    global frame

    if right:
        daco_character.clip_draw(frame * 121, 122, 121, 122, p[0], p[1], 120, 120)
    elif left:
        daco_character.clip_draw(frame * 121, 0, 121, 122, p[0], p[1], 120, 120)

    frame += 1
    frame = (frame + 1) % 9
    delay(0.03)
    update_canvas()

# def change_pont(p1,p2):
#     tmp = p1
#     p2 = tmp

right = False
left = False
frame = 0
points = [(random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)) for i in range(10)]


while True:
    clear_canvas()
    tuk_canvas()
    update_canvas()



    for i in range(0, len(points) - 1):
        draw_line(points[i], points[i + 1])



