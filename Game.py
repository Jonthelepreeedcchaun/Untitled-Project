import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys, pygame as pg, random as rng
pg.display.set_caption('Untitled Project')
v = pg.display.set_mode((0, 0), pg.FULLSCREEN)
from Definitions import smth, obst, render

w = pg.K_w; s = pg.K_s; a = pg.K_a; d = pg.K_d; e = pg.K_e; q = pg.K_q; bk = pg.K_BACKSPACE; sp = pg.K_SPACE; tb = pg.K_TAB; esc = pg.K_ESCAPE; sh = pg.K_LSHIFT
k = {w: 0, s: 0, a: 0, d: 0, e: 0, q: 0, bk: 0, sp: 0, tb: 0, esc: 0, sh: 0}

gamemode = 'Game'

room = 1
room_x = 0; room_y = 0
room_dat = {}
room_shp = {'A1':[0, 1], 'B1':[1, 1], 'C1':[0, 1], 'D1':[1, 0], 'E1':[0, 0], 'F1':[1, 0], 'G1':[0, 0], 'H1':[1, 0], 'I1':[0, 0], 'J1':[1, 0], 'K1':[0, 0], 'L1':[1, 0], 'M1':[0, 0], 'N1':[1, 0],
            'A2':[1, 1], 'B2':[0, 1], 'C2':[1, 1], 'D2':[0, 0], 'E2':[1, 0], 'F2':[0, 0], 'G2':[1, 0], 'H2':[0, 0], 'I2':[1, 0], 'J2':[0, 0], 'K2':[1, 0], 'L2':[0, 0], 'M2':[1, 0], 'N2':[0, 0],
            'A3':[0, 1], 'B3':[1, 1], 'C3':[0, 1], 'D3':[1, 1], 'E3':[0, 1], 'F3':[1, 0], 'G3':[0, 0], 'H3':[1, 0], 'I3':[0, 0], 'J3':[1, 0], 'K3':[0, 0], 'L3':[1, 0], 'M3':[0, 0], 'N3':[1, 0],
            'A4':[1, 1], 'B4':[0, 1], 'C4':[1, 1], 'D4':[0, 1], 'E4':[1, 1], 'F4':[0, 1], 'G4':[1, 0], 'H4':[0, 0], 'I4':[1, 0], 'J4':[0, 0], 'K4':[1, 0], 'L4':[0, 0], 'M4':[1, 0], 'N4':[0, 0],
            'A5':[0, 0], 'B5':[1, 0], 'C5':[0, 0], 'D5':[1, 1], 'E5':[0, 1], 'F5':[1, 1], 'G5':[0, 1], 'H5':[1, 1], 'I5':[0, 1], 'J5':[1, 1], 'K5':[0, 1], 'L5':[1, 1], 'M5':[0, 1], 'N5':[1, 1],
            'A6':[1, 0], 'B6':[0, 0], 'C6':[1, 0], 'D6':[0, 0], 'E6':[1, 1], 'F6':[0, 1], 'G6':[1, 1], 'H6':[0, 1], 'I6':[1, 1], 'J6':[0, 1], 'K6':[1, 1], 'L6':[0, 1], 'M6':[1, 1], 'N6':[0, 1],
            'A7':[0, 0], 'B7':[1, 0], 'C7':[0, 0], 'D7':[1, 0], 'E7':[0, 1], 'F7':[1, 1], 'G7':[0, 1], 'H7':[1, 1], 'I7':[0, 1], 'J7':[1, 1], 'K7':[0, 1], 'L7':[1, 1], 'M7':[0, 1], 'N7':[1, 1]}

Bg = [50, 50, 50]; Fg = [100, 100, 100]; P1_x = 120; P1_y = 120

boyimg = pg.image.load('Assets/t_boy.png')
manimg = pg.image.load('Assets/main.png')

running = 1
while running:
    mouse_x, mouse_y = pg.mouse.get_pos()
    mouse1, mouse3, mouse2 = pg.mouse.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:  ##makes the prohgram Mortal
            running = 0
        if event.type == pg.KEYDOWN:
            for this in k:
                if this == event.key:
                    k[this] = 1
        if event.type == pg.KEYUP:
            for this in k:
                if this == event.key:
                    k[this] = 0

    if gamemode == 'Menu':
        pass

    if gamemode == 'Game':
        room_x = 0; room_y = 120
        for this in room_shp:
            room_x += 120
            if room_x == 1800:
                room_x = 120; room_y += 120
            if room_shp.get(this)[room]:
                pg.draw.rect(v, ((Fg[0], Fg[1], Fg[2])), (room_x, room_y, 120, 120))
        if room == 1:
            boy = smth(P1_x, P1_y, 44, 91)
            render(boyimg, boy.x, boy.y)
            boyspeed = 4
            collision = 1
            P1_x += (((k[d] - k[a]) * boyspeed) / (k[w] * 0.65 + 1) / (k[s] * 0.65 + 1)) * collision
            P1_y += (((k[s] - k[w]) * boyspeed) / (k[a] * 0.65 + 1) / (k[d] * 0.65 + 1)) * collision

    if gamemode == 'Paused':
        pass

    pg.time.wait(10)
    pg.display.flip()
    v.fill((Bg[0], Bg[1], Bg[2]))
