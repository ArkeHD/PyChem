import os
import sys
import time
import pygame
import sqlite3
con = sqlite3.connect('game_data.sqlite')
cur = con.cursor()
cells = [['water', 'metall'],
         ['air', 'iron'],
         ['earth', 'steel'],
         ['fire'],
         ['mud'],
         ['energy'],
         ['lava'],
         ['lake'],
         ['rain'],
         ['lightning'],
         ['life'],
         ['plant'],
         ['tree'],
         ['coal'],
         ['obsidian']]

element_index = {'water': 0, 'air': 1, 'earth': 2, 'fire': 3, 'mud': 4,
                 'energy': 5, 'lava': 6, 'lake': 7, 'rain': 8,
                 'lightning': 9, 'life': 10, 'plant': 11, 'tree': 12,
                 'coal': 13, 'obsidian': 14, 'metall': 15, 'iron': 16,
                 'steel': 17}
save = '111100000000000000'

def load_image(name, colorkey=None):
    fullname = os.path.join('sprites', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        fullname = os.path.join('sprites', 'none.png')
    image = pygame.image.load(fullname)
    return image


class Elements(pygame.sprite.Sprite):
    menu_1 = load_image('adunatio_ui.png')
    menu_2 = load_image('calefactus_ui.png')
    menu_3 = load_image('division_ui.png')
    item_001 = load_image("water.png")
    item_002 = load_image("air.png")
    item_003 = load_image("earth.png")
    item_004 = load_image("fire.png")
    item_005 = load_image("mud.png")
    item_006 = load_image("energy.png")
    item_007 = load_image("lava.png")
    item_008 = load_image("lake.png")
    item_009 = load_image("rain.png")
    item_010 = load_image("lightning.png")
    item_011 = load_image("life.png")
    item_012 = load_image("plant.png")
    item_013 = load_image("tree.png")
    item_014 = load_image("coal.png")
    item_015 = load_image("obsidian.png")
    item_016 = load_image("metall.png")
    item_017 = load_image("iron.png")
    item_018 = load_image("steel.png")
    adun = load_image('plus.png')
    cale = load_image('fire_craft.png')
    divi = load_image('minus.png')

    def __init__(self, group, el):
        super().__init__(group)

        if el == 1:
            self.image = Elements.menu_1
            self.x = 864
            self.y = 224
        if el == 2:
            self.image = Elements.menu_2
            self.x = 736
            self.y = 752
        if el == 3:
            self.image = Elements.menu_3
            self.x = 1024
            self.y = 544
        if el == 4:
            self.image = Elements.item_001
            self.x = 32
            self.y = 32
        if el == 5:
            self.image = Elements.item_002
            self.x = 32
            self.y = 96
        if el == 6:
            self.image = Elements.item_003
            self.x = 32
            self.y = 160
        if el == 7:
            self.image = Elements.item_004
            self.x = 32
            self.y = 224
        if el == 8:
            self.image = Elements.item_005
            self.x = 32
            self.y = 288
        if el == 9:
            self.image = Elements.item_006
            self.x = 32
            self.y = 352
        if el == 10:
            self.image = Elements.item_007
            self.x = 32
            self.y = 416
        if el == 11:
            self.image = Elements.item_008
            self.x = 32
            self.y = 480
        if el == 12:
            self.image = Elements.item_009
            self.x = 32
            self.y = 544
        if el == 13:
            self.image = Elements.item_010
            self.x = 32
            self.y = 608
        if el == 14:
            self.image = Elements.item_011
            self.x = 32
            self.y = 672
        if el == 15:
            self.image = Elements.item_012
            self.x = 32
            self.y = 736
        if el == 16:
            self.image = Elements.item_013
            self.x = 32
            self.y = 800
        if el == 17:
            self.image = Elements.item_014
            self.x = 32
            self.y = 864
        if el == 18:
            self.image = Elements.item_015
            self.x = 32
            self.y = 928
        if el == 19:
            self.image = Elements.item_016
            self.x = 96
            self.y = 32
        if el == 20:
            self.image = Elements.item_017
            self.x = 96
            self.y = 96
        if el == 21:
            self.image = Elements.item_018
            self.x = 96
            self.y = 160
        if el == 22:
            self.image = Elements.adun
            self.x = 352
            self.y = 32
        if el == 23:
            self.image = Elements.cale
            self.x = 352
            self.y = 96
        if el == 24:
            self.image = Elements.divi
            self.x = 352
            self.y = 160
        self.rect = self.image.get_rect(center=(self.x, self.y))


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 64
        self.rect_color = pygame.Color('white')

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                rect_points = (i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, self.rect_color, rect_points, 1)


# sprite loading and other preparing
# adunatio animations
adunatio_anim0 = load_image('adunatio_anim0.png')
adunatio_anim1 = load_image('adunatio_anim1.png')
adunatio_anim2 = load_image('adunatio_anim2.png')
adunatio_anim3 = load_image('adunatio_anim3.png')
# adunatio process
adunatio_in0 = load_image('none.png')
adunatio_in1 = load_image('none.png')
adunatio_out = load_image('none.png')
# calefactus animations
calefactus_anim0 = load_image('calefactus_anim0.png')
calefactus_anim1 = load_image('calefactus_anim1.png')
calefactus_anim2 = load_image('calefactus_anim2.png')
# calefactus process
calefactus_in = load_image('none.png')
calefactus_heat = load_image('none.png')
calefactus_out = load_image('none.png')
# division animations
division_anim0 = load_image('divisio_anim0.png')
division_anim1 = load_image('division_anim1.png')
division_anim2 = load_image('division_anim2.png')
division_anim3 = load_image('division_anim3.png')
# division process
division_in = load_image('none.png')
division_0ut = load_image('none.png')
division_ou1 = load_image('none.png')
#
wrong = load_image('wrong_button.png')
right = load_image('right_button.png')
closed = load_image('closed.png')
#
craft_mode = 0
craft_mode0 = load_image('right_button.png')
craft_mode1 = load_image('wrong_button.png')
craft_mode2 = load_image('wrong_button.png')
#
a_in0 = ''
a_in1 = ''
a_out = ''
#
c_in = ''
c_heat = ''
c_out = ''
#
d_in = ''
d_0ut = ''
d_ou1 = ''
#
tec = 0
crafting = False
#
file = 'savfk-past-tense.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)
#
all_sprites = pygame.sprite.Group()
for i in range(24):
    Elements(all_sprites, i + 1)
size = width, height = 1280, 960
screen = pygame.display.set_mode(size)
running= True
board = Board(30, 20)
is_crafting = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            x, y = x // 64, y // 64
            try:
                if x == 5 and y == 0 or x == 4 and y == 0:
                    craft_mode0 = load_image('right_button.png')
                    craft_mode1 = load_image('wrong_button.png')
                    craft_mode2 = load_image('wrong_button.png')
                    craft_mode = 0
                    a_in0 = ''
                    a_in1 = ''
                    a_out = ''
                    adunatio_in0 = load_image('none.png')
                    c_in = ''
                    c_heat = ''
                    c_out = ''
                    calefactus_in = load_image('none.png')
                elif x == 5 and y == 1 or x == 4 and y == 1:
                    craft_mode0 = load_image('wrong_button.png')
                    craft_mode1 = load_image('right_button.png')
                    craft_mode2 = load_image('wrong_button.png')
                    craft_mode = 1
                    a_in0 = ''
                    a_in1 = ''
                    a_out = ''
                    adunatio_in0 = load_image('none.png')
                    c_in = ''
                    c_heat = ''
                    c_out = ''
                    calefactus_in = load_image('none.png')
                elif x == 5 and y == 2 or x == 4 and y == 2:
                    craft_mode0 = load_image('wrong_button.png')
                    craft_mode1 = load_image('wrong_button.png')
                    craft_mode2 = load_image('right_button.png')
                    craft_mode = 2
                    a_in0 = ''
                    a_in1 = ''
                    a_out = ''
                    adunatio_in0 = load_image('none.png')
                    c_in = ''
                    c_heat = ''
                    c_out = ''
                    calefactus_in = load_image('none.png')
                else:
                    if not crafting:
                        if int(save[element_index[cells[y][x]]]) == 1:
                            print(cells[y][x])
                            if craft_mode == 0:
                                if a_in0 == '':
                                    a_in0 = cells[y][x]
                                    adunatio_in0 = load_image(cells[y][x] + '.png')
                                    pygame.display.flip()
                                else:
                                    a_in1 = cells[y][x]
                                    adunatio_in1 = load_image(cells[y][x] + '.png')
                                    pygame.display.flip()
                                    a_out = cur.execute(
                                        """SELECT adunatio_out FROM adunatio WHERE adunatio_in0 = '{}' AND adunatio_in1 = '{}'""".format(
                                            str(a_in0),
                                            str(a_in1))).fetchall()
                                    a_out = (str(a_out).replace("'", '').replace("[", '')
                                                    .replace("]",'').replace(")", '').replace("(", '')
                                                    .replace(",", ''))
                                    crafting = True
                            elif craft_mode == 1:
                                if c_in == '':
                                    c_in = cells[y][x]
                                    calefactus_in = load_image(cells[y][x] + '.png')
                                    pygame.display.flip()
                                else:
                                    c_heat = cells[y][x]
                                    calefactus_heat = load_image(cells[y][x] + '.png')
                                    pygame.display.flip()
                                    c_out = cur.execute(
                                        """SELECT calefactus_out FROM calefactus WHERE calefactus_in = '{}' AND calefactus_heat = '{}'""".format(
                                            str(c_in),
                                            str(c_heat))).fetchall()
                                    c_out = (str(c_out).replace("'", '').replace("[", '')
                                                    .replace("]",'').replace(")", '').replace("(", '')
                                                    .replace(",", ''))
                                    crafting = True
                            elif craft_mode == 2:
                                if d_in == '':
                                    d_in = cells[y][x]
                                    division_in = load_image(cells[y][x] + '.png')
                                    pygame.display.flip()
                                    d_0ut = cur.execute(
                                        """SELECT division_out0 FROM division WHERE division_in = '{}'""".format(
                                            str(c_in),
                                            str(c_heat))).fetchall()
                                    d_0ut = (str(c_out).replace("'", '').replace("[", '')
                                                    .replace("]",'').replace(")", '').replace("(", '')
                                                    .replace(",", ''))
                                    d_ou1 = cur.execute(
                                        """SELECT division_out1 FROM division WHERE division_in = '{}'""".format(
                                            str(c_in),
                                            str(c_heat))).fetchall()
                                    d_ou1 = (str(c_out).replace("'", '').replace("[", '')
                                             .replace("]", '').replace(")", '').replace("(", '')
                                             .replace(",", ''))
                                    crafting = True
                        else:
                            screen.blit(closed, (x * 64, y * 64))
                            pygame.display.flip()
                            time.sleep(0.25)
            except IndexError as e:
                tec += 1
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 198, 155))
    board.render(screen)
    all_sprites.draw(screen)
    screen.blit(craft_mode0, (256, 0))
    screen.blit(craft_mode1, (256, 64))
    screen.blit(craft_mode2, (256, 128))
    screen.blit(adunatio_in0, (768, 128))
    screen.blit(adunatio_in1, (768, 256))
    screen.blit(adunatio_out, (896, 192))
    screen.blit(calefactus_in, (640, 672))
    screen.blit(calefactus_heat, (640, 768))
    screen.blit(calefactus_out, (768, 672))
    screen.blit(division_in, (960, 512))
    screen.blit(division_0ut, (1056, 448))
    screen.blit(division_ou1, (1056, 576))
    pygame.display.flip()
    if crafting and a_in1 != '':
        screen.blit(adunatio_anim0, (768, 128))
        pygame.display.flip()
        time.sleep(0.75)
        screen.blit(adunatio_anim1, (768, 128))
        pygame.display.flip()
        time.sleep(0.75)
        screen.blit(adunatio_anim2, (768, 128))
        pygame.display.flip()
        time.sleep(0.75)
        screen.blit(adunatio_anim3, (768, 128))
        pygame.display.flip()
        time.sleep(0.75)
        adunatio_out = load_image(a_out + '.png')
        pygame.display.flip()
        time.sleep(0.5)
        a_in0 = ''
        a_in1 = ''
        a_out = ''
        adunatio_in0 = load_image('none.png')
        adunatio_in1 = load_image('none.png')
        pygame.display.flip()
        crafting = False
    elif crafting and c_in != '':
        screen.blit(calefactus_anim0, (640, 672))
        pygame.display.flip()
        time.sleep(0.75)
        screen.blit(calefactus_anim1, (640, 672))
        pygame.display.flip()
        time.sleep(0.75)
        screen.blit(calefactus_anim2, (640, 672))
        pygame.display.flip()
        time.sleep(0.75)
        calefactus_out = load_image(c_out + '.png')
        pygame.display.flip()
        time.sleep(0.5)
        c_in = ''
        c_heat = ''
        c_out = ''
        calefactus_in = load_image('none.png')
        calefactus_heat = load_image('none.png')
        pygame.display.flip()
        crafting = False
    elif crafting and d_in != '':
        screen.blit(division_anim0, (992, 448))
        pygame.display.flip()
        time.sleep(0.75)
        screen.blit(division_anim1, (992, 448))
        pygame.display.flip()
        time.sleep(0.75)
        screen.blit(division_anim2, (992, 448))
        pygame.display.flip()
        time.sleep(0.75)
        screen.blit(division_anim3, (992, 448))
        pygame.display.flip()
        time.sleep(0.75)
        division_0ut= load_image(d_0ut + '.png')
        pygame.display.flip()
        time.sleep(0.5)
        d_in = ''
        d_0ut = ''
        d_ou1 = ''
        division_in = load_image('none.png')
        pygame.display.flip()
        crafting = False
con.close()
print(tec)
