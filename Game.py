import os # public imports
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys, pygame as pg, random as rng
pg.display.set_caption('Untitled Project')
v = pg.display.set_mode((0, 0), pg.FULLSCREEN)

w = pg.K_w; s = pg.K_s; a = pg.K_a; d = pg.K_d; e = pg.K_e; q = pg.K_q; bk = pg.K_BACKSPACE; sp = pg.K_SPACE; tb = pg.K_TAB; esc = pg.K_ESCAPE; sh = pg.K_LSHIFT; p = pg.K_p # key variables, used for key detection
k = {w: 0, s: 0, a: 0, d: 0, e: 0, q: 0, bk: 0, sp: 0, tb: 0, esc: 0, sh: 0, p: 0} # dictionary using above key variables; a zero represents the key not being pressed and a one is it currently being pressed

gamemode = 'Game' # gamemodes control what section of the loop is actively

room = 0 # rooms are stored as integers; this is important for the following variables and dictionaries which are used in generation
room_dat = {'Bg':[(50, 50, 50)], 'Fg':[(100, 100, 100)], 'P1_x':[120], 'P1_y':[120]} # this dictionary contains colors of the room in RGB as well as starting position of the player character
room_shp = {'A1':[1], 'B1':[1], 'C1':[1], 'D1':[0], 'E1':[0], 'F1':[0], 'G1':[0], 'H1':[0], 'I1':[0], 'J1':[0], 'K1':[0], 'L1':[0], 'M1':[0], 'N1':[0],
            'A2':[1], 'B2':[1], 'C2':[1], 'D2':[0], 'E2':[0], 'F2':[0], 'G2':[0], 'H2':[0], 'I2':[0], 'J2':[0], 'K2':[0], 'L2':[0], 'M2':[0], 'N2':[0],
            'A3':[1], 'B3':[1], 'C3':[1], 'D3':[1], 'E3':[1], 'F3':[0], 'G3':[0], 'H3':[0], 'I3':[0], 'J3':[0], 'K3':[0], 'L3':[0], 'M3':[0], 'N3':[0],
            'A4':[1], 'B4':[1], 'C4':[1], 'D4':[1], 'E4':[1], 'F4':[1], 'G4':[0], 'H4':[0], 'I4':[0], 'J4':[0], 'K4':[0], 'L4':[0], 'M4':[0], 'N4':[0],
            'A5':[0], 'B5':[0], 'C5':[0], 'D5':[1], 'E5':[1], 'F5':[1], 'G5':[1], 'H5':[1], 'I5':[1], 'J5':[1], 'K5':[1], 'L5':[1], 'M5':[1], 'N5':[1],
            'A6':[0], 'B6':[0], 'C6':[0], 'D6':[0], 'E6':[1], 'F6':[1], 'G6':[1], 'H6':[1], 'I6':[1], 'J6':[1], 'K6':[1], 'L6':[1], 'M6':[1], 'N6':[1],
            'A7':[0], 'B7':[0], 'C7':[0], 'D7':[0], 'E7':[1], 'F7':[1], 'G7':[1], 'H7':[1], 'I7':[1], 'J7':[1], 'K7':[1], 'L7':[1], 'M7':[1], 'N7':[1]} # this dictionary is laid out proportionately to how the rooms are actually generated
room_setup = 1 # an if statement will be passed at the beginning of the room - this mainly serves to reset the position of the player character
roomvar1 = 0
roomvar2 = 0
roomvar3 = 0 # these three misc variables will help with triggers that i would set off while in rooms

boyimg = pg.image.load('Assets/t_boy.png')
manimg = pg.image.load('Assets/main.png') # importing and loading images

from Definitions import smth, obst, render, clrdet # personal imports

running = 1
while running:
    mouse_x, mouse_y = pg.mouse.get_pos()
    mouse1, mouse3, mouse2 = pg.mouse.get_pressed() # mouse input is always nice to have
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
                    k[this] = 0 # these for loops handle all key inputs

    if gamemode == 'Menu':
        pass

    if gamemode == 'Game':
        room_x = 0; room_y = 120
        for this in room_shp:
            room_x += 120
            if room_x == 1800:
                room_x = 120; room_y += 120
            if room_shp.get(this)[room]:
                pg.draw.rect(v, (room_dat.get('Fg')[room]), (room_x, room_y, 120, 120)) # this is how the rooms are generated - in 120 by 120 squares
        if room == 0:
            if room_setup:
                P1_x = room_dat.get('P1_x')[room]
                P1_y = room_dat.get('P1_y')[room]
                room_setup = 0
            boyspeed = 4
            boy = smth(P1_x, P1_y, 44, 91) # may upgrade the player from smth to a more specific class - not necessary as of now (6/14)
            if k[p]:
                print(str(P1_x) + ', ' + str(P1_y))
            if k[a] and not clrdet('l', P1_x, P1_y + 61, 44, 30, room_dat.get('Bg')[room]):
                P1_x -= boyspeed * k[a]
            if k[d] and not clrdet('r', P1_x, P1_y + 61, 44, 30, room_dat.get('Bg')[room]):
                P1_x += boyspeed * k[d]
            if k[w] and not clrdet('u', P1_x, P1_y + 61, 44, 30, room_dat.get('Bg')[room]):
                P1_y -= boyspeed * k[w]
            if k[s] and not clrdet('d', P1_x, P1_y + 61, 44, 30, room_dat.get('Bg')[room]):
                P1_y += boyspeed * k[s]
            render(boyimg, P1_x, P1_y)

    if gamemode == 'Paused':
        pass

    pg.time.wait(10)
    pg.display.flip()
    if gamemode == 'Game':
        v.fill(room_dat.get('Bg')[room]) # background is filled in accordance to the color associated with the room
    else:
        v.fill((125, 125, 125))
