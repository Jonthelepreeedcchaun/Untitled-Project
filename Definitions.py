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
    from Game import v
    if x < -130 or x > 2050 or y < -130 or y > 1210:
        pass
    else:
        v.blit(img, (x, y))

def clrdet(direction, x, y, x_siz, y_siz, clr):
    from Game import v
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

def door(P1_x, P1_y, x, y, x_siz, y_siz, Fg):
    import pygame as pg
    from Game import v
    pg.draw.rect(v, (Fg), (x, y, x_siz, y_siz))
    if P1_x >= x and P1_x <= x + x_siz and P1_y >= y and P1_y <= y + y_siz:
        return True
