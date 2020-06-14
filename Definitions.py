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
