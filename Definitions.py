class smth:
    def __init__(self, x, y, x_siz, y_siz):
        self.x = x
        self.y = y
        self.x_siz = x_siz
        self.y_siz = y_siz

class obst(smth):
    def __init__(self, x, y, x_siz, y_siz, r_per, t_per, l_per, b_per):
        self.r_per = r_per
        self.t_per = t_per
        self.l_per = l_per
        self.b_per = b_per

def render(img, x, y):
    from Game import video as v
    if x < -130 or x > 2050 or y < -130 or y > 1210:
        pass
    else:
        v.blit(img, (x, y))

def clrdet(direction, x, y, x_siz, y_siz, clr):
    from Game import video as v
    cntr_x = int(x + x_siz / 2)
    cntr_y = int(y + y_siz / 2)
    if direction == 'r':
        if v.get_at((cntr_x + int(0.6 * x_siz), cntr_y))[:3] == clr:
            return True
        else:
            return False
    if direction == 'l':
        if v.get_at((cntr_x - int(0.6 * x_siz), cntr_y))[:3] == clr:
            return True
        else:
            return False
    if direction == 'u':
        if v.get_at((cntr_x, cntr_y - int(0.6 * y_siz)))[:3] == clr:
            return True
        else:
            return False
    if direction == 'd':
        if v.get_at((cntr_x, cntr_y + int(0.6 * y_siz)))[:3] == clr:
            return True
        else:
            return False

def door(P1_x, P1_y, defaults, x = 'lmao', y = 'imagine having', x_siz = 'default', y_siz = 'values'):
    import pygame as pg
    from Game import video as v, room_dat, room
    if room >= len(room_dat["Fg"]):
        foreground_color = (100, 100, 100)
    else:
        foreground_color = room_dat.get('Fg')[room]
    if defaults == 1:
        x = 1800
        y = 600
        x_siz = 120
        y_siz = 360
    if defaults == 2:
        x = 1800
        y = 120
        x_siz = 120
        y_siz = 360
    if defaults == 3:
        x = 1320
        y = 0
        x_siz = 480
        y_siz = 120
    if defaults == 4:
        x = 720
        y = 0
        x_siz = 480
        y_siz = 120
    if defaults == 5:
        x = 120
        y = 0
        x_siz = 480
        y_siz = 120
    if defaults == 6:
        x = 0
        y = 120
        x_siz = 120
        y_siz = 360
    if defaults == 7:
        x = 0
        y = 600
        x_siz = 120
        y_siz = 360
    if defaults == 8:
        x = 120
        y = 960
        x_siz = 480
        y_siz = 120
    if defaults == 9:
        x = 720
        y = 960
        x_siz = 480
        y_siz = 120
    if defaults == 10:
        x = 1320
        y = 960
        x_siz = 480
        y_siz = 120
    pg.draw.rect(v, (foreground_color), (x, y, x_siz, y_siz))
    if P1_x >= x and P1_x <= x + x_siz and P1_y >= y and P1_y <= y + y_siz:
        return True

def text_objects(text, font, colour): ##creates text objects
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def message_display(text, position, size = 15, colour = ((255, 255, 255))):  ##defines messages to be typed and displayed and whatnot
    import pygame as pg
    from Game import video as v
    smallText = pg.font.Font('Assets/Helvetica.ttf',size)
    TextSurf, TextRect = text_objects(text, smallText, colour)
    TextRect.topleft = position
    v.blit(TextSurf, TextRect)

def door_gen(P1_x, P1_y):
    from Game import room_drs, room
    for this in room_drs:
        if room in room_drs.get(this):
            room_index = room_drs.get(this).index(room)
            if door(P1_x, P1_y, this):
                room = int(room_drs.get(this)[room_index + 1])
                return room

def terrain_gen(room_shp, room):
    import pygame as pg
    from Game import video as v, room_dat, room_drs
    room_x = 0; room_y = 120
    if room >= len(room_dat["Fg"]):
        foreground_color = (100, 100, 100)
    else:
        foreground_color = room_dat.get('Fg')[room]
    for this in room_shp:
        room_x += 120
        if room_x == 1800:
            room_x = 120; room_y += 120
        if room_shp.get(this)[room]:
            pg.draw.rect(v, (foreground_color), (room_x, room_y, 120, 120)) # this is how the rooms are generated - in 120 by 120 squares
