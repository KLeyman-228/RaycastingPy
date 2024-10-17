import pygame as pg
from config import *
import sys, os



#Init 

pg.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDGTH, SCREEN_HEIGHT))
pg.display.set_caption('Level Editor')
play = True


player_loc = (HALF_SCREEN_WIDGTH, HALF_SCREEN_HEIGHT)




#Raycast func
def MyRayCasti(location):
    dAngle = ANGLE - FOV / 2
    xo, yo = location
    for ray in range(RAYS):
        cos_a = math.cos(dAngle)
        sin_a = math.sin(dAngle)
        for ddepth in range(DEPTH):
            x = xo + ddepth * cos_a
            y = yo + ddepth * sin_a
            if (x // TILE * TILE, y // TILE * TILE) in map:
                h = (RAYS // (2 * math.tan(FOV / 2)) * TILE) / ddepth
                c = 255 / (1 + ddepth * ddepth * 0.00001)
                color = (c, c, c)
                pg.draw.rect(screen, color, (ray * (SCREEN_WIDGTH // RAYS), (HALF_SCREEN_HEIGHT - h), SCALE_RECT, h * 2))
                break
        dAngle += D_ANGLE


dx, dy = (HALF_SCREEN_WIDGTH, HALF_SCREEN_HEIGHT)



#Main
while play:
    screen.fill('black')
    
    MyRayCasti(player_loc)
    pg.draw.circle(screen, 'red', player_loc, 10)

    sina = math.sin(ANGLE)
    cosa = math.cos(ANGLE)

    player_loc = (dx, dy)

#Movement
    key = pg.key.get_pressed()
    if key[pg.K_LEFT]:
        ANGLE -= 0.02
    if key[pg.K_RIGHT]:
        ANGLE += 0.02
    if key[pg.K_w]:
        dx += 5 * cosa
        dy += 5 * sina
    if key[pg.K_s]:
        dx += -5 * cosa
        dy += -5 * sina

#QUIT EVENT
    for event in pg.event.get():
        if event.type == pg.QUIT:
            play = False


#PG UPDATE
    pg.display.update()
    clock.tick(FPS)

sys.exit()

