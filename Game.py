import os # public imports
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys, pygame as pg, random as rng, json, sys
pg.display.set_caption('Untitled Project')
video = pg.display.set_mode((0, 0), pg.FULLSCREEN)

z = pg.K_z; x = pg.K_x; c = pg.K_c; v = pg.K_v; w = pg.K_w; s = pg.K_s; a = pg.K_a; d = pg.K_d; e = pg.K_e; q = pg.K_q; bk = pg.K_BACKSPACE; sp = pg.K_SPACE; tb = pg.K_TAB; esc = pg.K_ESCAPE; sh = pg.K_LSHIFT; p = pg.K_p # key variables, used for key detection
k = {z: 0, x: 0, c: 0, v: 0, w: 0, s: 0, a: 0, d: 0, e: 0, q: 0, bk: 0, sp: 0, tb: 0, esc: 0, sh: 0, p: 0} # dictionary using above key variables; a zero represents the key not being pressed and a one is it currently being pressed

mode = 'Menu' # modes control what section of the loop is active
state = 'Main' # states control which subsection of the loop is active

room = 0 # rooms are stored as integers; this is important for the following variables and dictionaries which are used in generation
room_drs = {1:[0, "2"], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[0, "1"]}
room_dat = {'Bg':[(50, 50, 50)], 'Fg':[(100, 100, 100)]} # this dictionary contains colors of the room in RGB
with open('Gamedata/room_shp.json', 'r') as f:
    room_shp = json.load(f)
room_colm = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
room_rows = ["1", "2", "3", "4", "5", "6", "7"]
miscvar1 = 0
miscvar2 = 0
miscvar3 = 0 # these three misc variables will help with triggers

boyimg = pg.image.load('Assets/c_boy.png')
manimg = pg.image.load('Assets/main.png') # importing and loading images

from Definitions import smth, obst, render, clrdet, door, text_objects, message_display, terrain_gen, door_gen # personal imports
pg.font.init()

running = 1
while running:
    if k[esc]:
        running = 0
        pygame.display.quit()
        sys.exit()
    mouse_x, mouse_y = pg.mouse.get_pos()
    mouse1, mouse3, mouse2 = pg.mouse.get_pressed() # mouse input is always nice to have
    for event in pg.event.get():
        if event.type == pg.QUIT:  ##makes the prohgram Mortal
            running = 0
            pygame.display.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            for this in k:
                if this == event.key:
                    k[this] = 1
        if event.type == pg.KEYUP:
            for this in k:
                if this == event.key:
                    k[this] = 0 # these for loops handle all key inputs

    if mode == 'Menu':
        Bg_gen = 0
        message_display("Untitled Project", (120, 120), 50, ((0, 0, 0)))
        message_display("Press 'Space' to start", (120, 220), 30, ((0, 0, 0)))
        message_display("Press 'P' to enter dev mode", (120, 300), 30, ((0, 0, 0)))
        message_display("Press 'ESC' to quit", (120, 900), 30, ((0, 0, 0)))
        if k[sp]:
            mode = "Game"
            room = 0
            P1_x = 260; P1_y = 260
        if k[p]:
            mode = "devmode"
            room = 0
            devmode_menu = 0

    if mode == 'Game':
        Bg_gen = 1
        if room == 0:
            boyspeed = 3
            boy = smth(P1_x, P1_y, 44, 91) # may upgrade the player from smth to a more specific class - not necessary as of now (6/14)
            boy_cntr_x = int(P1_x + 44 / 2)
            boy_cntr_y = int((P1_y + 61) + 30 / 2)

            plrimg = boyimg # not sure if these four lines are *necessary*, but they certainly make it easier for humans to understand, and imo keep it all very neat
            plrspeed = boyspeed
            plr_cntr_x = boy_cntr_x
            plr_cntr_y = boy_cntr_y

        player_position_var = 120; player_colm = " "
        for this in room_colm:
            if plr_cntr_x >= player_position_var and plr_cntr_x < (player_position_var + 120):
                player_colm = this
            player_position_var += 120
        player_position_var = 120; player_rows = " "
        for this in room_rows:
            if plr_cntr_y >= player_position_var and plr_cntr_y < (player_position_var + 120):
                player_rows = this
            player_position_var += 120
        player_position_var = player_colm + player_rows

        terrain_gen(room_shp, room)
        if player_rows == " " or player_colm == " ":
            room = door_gen(plr_cntr_x, plr_cntr_y)
        else:
            door_gen(plr_cntr_x, plr_cntr_y)
        if k[a] and not clrdet('l', P1_x, P1_y + 61, 44, 30, room_dat.get('Bg')[room]):
            P1_x -= plrspeed * k[a]
        if k[d] and not clrdet('r', P1_x, P1_y + 61, 44, 30, room_dat.get('Bg')[room]):
            P1_x += plrspeed * k[d]
        if k[w] and not clrdet('u', P1_x, P1_y + 61, 44, 30, room_dat.get('Bg')[room]):
            P1_y -= plrspeed * k[w]
        if k[s] and not clrdet('d', P1_x, P1_y + 61, 44, 30, room_dat.get('Bg')[room]):
            P1_y += plrspeed * k[s]
        render(plrimg, P1_x, P1_y)

    if mode == 'devmode':
        Bg_gen = 1
        if k[q]:
            mode = "Menu"
        terrain_gen(room_shp, room)
        devmode_mouse_var = 120; devmode_colm = " "
        for this in room_colm:
            if mouse_x >= devmode_mouse_var and mouse_x < (devmode_mouse_var + 120):
                devmode_colm = this
            devmode_mouse_var += 120
        devmode_mouse_var = 120; devmode_rows = " "
        for this in room_rows:
            if mouse_y >= devmode_mouse_var and mouse_y < (devmode_mouse_var + 120):
                devmode_rows = this
            devmode_mouse_var += 120
        devmode_mouse_var = devmode_colm + devmode_rows

        if devmode_menu:
            message_display("Press 'Space' to close the Devmenu", (20, 20))
            message_display("room = " + str(room), (20, 120))
            message_display("Press Z to increase the room number and X to reduce it", (20, 140))
            message_display("Press S to save your changes", (20, 340))
            message_display("Press Q to leave devmode", (20, 520))
            if k[sp]:
                miscvar1 = 1
            if not k[sp] and miscvar1:
                miscvar1 = 0
                devmode_menu = 0
        else:
            message_display("Press 'Space' to access the Devmenu", (20, 20))
            if k[sp]:
                miscvar1 = 1
            if not k[sp] and miscvar1:
                miscvar1 = 0
                devmode_menu = 1

        if k[s]:
            with open('Gamedata/room_shp.json', 'w', encoding = 'utf-8') as f: # terrain_gen saves
                json.dump(room_shp, f, ensure_ascii = False, indent = 4)
        if k[z]:
            miscvar2 = 1
        if not k[z] and miscvar2:
            miscvar2 = 0
            room += 1
        if k[x]:
            miscvar3 = 1
        if not k[x] and miscvar3:
            miscvar3 = 0
            if room > 0:
                room -= 1

        devmode_mode = "terrain"

        if devmode_mode == "terrain":
            if not devmode_colm == " " and not devmode_rows == " ": # this if statement checks if the mouse is on the room shape grid
                if mouse1:
                    room_shp[devmode_mouse_var][room] = 1
                if mouse2:
                    room_shp[devmode_mouse_var][room] = 0
            else:
                if devmode_colm == " " and not devmode_rows == " ":
                    if mouse_x > 420.69: # i could have used any int or float between zero and 1080, so naturally i went with the funny haha choice
                        pass #rightside
                    if mouse_x < 420.69:
                        pass #leftside
                if devmode_rows == " " and not devmode_colm == " ":
                    if mouse_y > 420.69:
                        pass #downside
                    if mouse_y < 420.69:
                        pass #upside

    pg.time.wait(10)
    pg.display.flip()
    if Bg_gen:
        if room >= len(room_dat["Bg"]):
            background_color = (50, 50, 50)
        else:
            background_color = room_dat.get('Bg')[room]
        video.fill(background_color) # background is filled in accordance to the color associated with the room
    else:
        video.fill((125, 125, 125))
