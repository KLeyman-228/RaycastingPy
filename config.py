import pygame
import math


#Project Settings

FPS = 60

SCREEN_WIDGTH = 1200
SCREEN_HEIGHT = 800
HALF_SCREEN_WIDGTH = SCREEN_WIDGTH // 2
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

PI = math.pi
FOV = PI / 3
RAYS = 120
DEPTH = 800
ANGLE = PI / 3
D_ANGLE = FOV / RAYS



DIST = RAYS // (2 * math.tan(FOV / 2))
SCALE_RECT = SCREEN_WIDGTH // RAYS

TILE = 100
PROJECTION_K = DIST * TILE

MCOLS = 10
MROWS = 10



#Level Create

tmap = [
    'WWWWWWWWWWWW',
    'W..WW..WWW.W',
    'W..W.......W',
    'W........W.W',
    'W.W........W',
    'W.W.......WW',
    'W....W...WWW',
    'WWWWWWW..WWW'
]

map = set()
for j, row in enumerate(tmap):
    for i, char in enumerate(row):
        if char == 'W':
            map.add((i * TILE, j * TILE))
