import pgzrun
import pygame
from pgzero.rect import Rect

from TreeBroko import TreeBroko

QUANTITY_MAIN_ROUNDS = 3
DEPTH_IMMERSION = 6
UNIT = 200
HORIZONTAL_OFFSET = UNIT / 2
ROUNDS_WIDTH = UNIT * QUANTITY_MAIN_ROUNDS

SIDE_ZOOM_SQUARE = UNIT / 2
SIDE_ZOOM_AREA = UNIT
x_center_zoom = ROUNDS_WIDTH / 2
zoom = 2

move = False
moveInLeft = False
zooming = False
isIncrease = False

MAIN_ROUNDS_COLOR = (255, 255, 255)
ZOOM_ROUNDS_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

WIDTH = ROUNDS_WIDTH + UNIT
HEIGHT = UNIT

tree_broko = TreeBroko(QUANTITY_MAIN_ROUNDS - 1, DEPTH_IMMERSION)


def update():
    global move, moveInLeft, x_center_zoom, zoom

    if move:
        if moveInLeft:
            x_center_zoom -= 10 / zoom
            if x_center_zoom < SIDE_ZOOM_SQUARE / zoom:
                x_center_zoom = SIDE_ZOOM_SQUARE / zoom
        else:
            x_center_zoom += 10 / zoom
            if x_center_zoom > ROUNDS_WIDTH - SIDE_ZOOM_SQUARE / zoom:
                x_center_zoom = ROUNDS_WIDTH - SIDE_ZOOM_SQUARE / zoom

    if zooming:
        if isIncrease:
            zoom += zoom / 8
        else:
            zoom -= zoom / 8
            if zoom < 1:
                zoom = 1


def draw():
    screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((0, 0, 0))

    #  Zoom area
    screen.draw.rect(Rect((UNIT * QUANTITY_MAIN_ROUNDS, 0), (SIDE_ZOOM_AREA, SIDE_ZOOM_AREA)), ZOOM_ROUNDS_COLOR)

    # Zoom rounds
    for fraction in tree_broko.generate_tree():
        radius = (1 / (fraction.get_denominator() ** 2)) * UNIT / 2 * zoom
        zoom_offset = HORIZONTAL_OFFSET + fraction.get_value() * UNIT - x_center_zoom
        screen.draw.circle(
            (zoom_offset * zoom + ROUNDS_WIDTH + SIDE_ZOOM_AREA / 2,
             HEIGHT - radius),
            radius, ZOOM_ROUNDS_COLOR)

    # Main background
    screen.draw.filled_rect(Rect((0, 0), (UNIT * QUANTITY_MAIN_ROUNDS, HEIGHT)), BACKGROUND_COLOR)

    # Zoom square
    screen.draw.rect(
        Rect((x_center_zoom - SIDE_ZOOM_SQUARE / zoom, HEIGHT - SIDE_ZOOM_SQUARE / zoom * 2),
             (SIDE_ZOOM_SQUARE / zoom * 2, SIDE_ZOOM_SQUARE / zoom * 2)),
        ZOOM_ROUNDS_COLOR)

    # Main rounds
    for fraction in tree_broko.generate_tree():
        radius = (1 / (fraction.get_denominator() ** 2)) * UNIT / 2
        screen.draw.circle((fraction.get_value() * UNIT + HORIZONTAL_OFFSET, HEIGHT - radius),
                           radius, MAIN_ROUNDS_COLOR)


def on_key_down(key):
    global move, moveInLeft, zooming, isIncrease
    if key == keys.LEFT or key == keys.RIGHT:
        move = True
        moveInLeft = (key == keys.LEFT)
    if key == keys.UP or key == keys.DOWN:
        zooming = True
        isIncrease = key == keys.UP


def on_key_up(key):
    global move, zooming
    if key == keys.LEFT or key == keys.RIGHT:
        move = False
    if key == keys.UP or key == keys.DOWN:
        zooming = False


pgzrun.go()
