import os
import sys
import time
import pygame
import sqlite3
con = sqlite3.connect('game_data.sqlite')
cur = con.cursor()
cells = [['water'],
         ['air'],
         ['earth'],
         ['fire']]

def load_image(name, colorkey=None):
    fullname = os.path.join('sprites', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        fullname = os.path.join('sprites', 'none.png')
    image = pygame.image.load(fullname)
    return image


class Elements(pygame.sprite.Sprite):
    item_001 = load_image("water.png")
    item_002 = load_image("air.png")
    item_003 = load_image("earth.png")
    item_004 = load_image("fire.png")

    def __init__(self, group, el):
        super().__init__(group)

        if el == 1:
            self.image = Elements.item_001
            self.x = 16
            self.y = 16
        if el == 2:
            self.image = Elements.item_002
            self.x = 16
            self.y = 48
        if el == 3:
            self.image = Elements.item_003
            self.x = 16
            self.y = 80
        if el == 4:
            self.image = Elements.item_004
            self.x = 16
            self.y = 112
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
fuse_first = ''
fuse_second = ''
element_1 = load_image('none.png')
element_2 = load_image('none.png')
element_3 = load_image('none.png')
all_sprites = pygame.sprite.Group()
adunatio = load_image("adunatio_ui.png")
calefactus = load_image("calefactus_ui.png")
tryi = load_image("try.png")
division = load_image("division_ui.png")
for i in range(4):
    Elements(all_sprites, i + 1)
size = width, height = 1280, 960
screen = pygame.display.set_mode(size)
running, flag = True, False
board = Board(30, 20)
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            x, y = x // 64, y // 64
            try:
                print(x, y)
                print(cells)
                print(cells[y][x])
                if fuse_first == '':
                    fuse_first = str(cells[y][x])
                    element_1 = load_image(cells[y][x] + '.png')
                else:
                    fuse_second = str(cells[y][x])
                    element_2 = load_image(cells[y][x] + '.png')
                    craft_result = cur.execute("""SELECT out_elem FROM crafts WHERE first_elem = '{}' AND secn_elem = '{}'""".format(str(fuse_first),
                                                str(fuse_second))).fetchall()
                    craft_result = str(craft_result).replace("'", '').replace("[", '').replace("]", '').replace(")", '').replace("(", '').replace(",", '')
                    time.sleep(1.5)
                    print('alright', craft_result, fuse_first, fuse_second)
                    element_1 = load_image('none.png')
                    element_2 = load_image('none.png')
                    fuse_first = ''
                    fuse_second = ''
                    element_3 = load_image(str(craft_result) + '.png')
                print(1111, fuse_first, fuse_second)
                flag = True
            except IndexError as e:
                print(35436534, 'none', e)
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    board.render(screen)
    all_sprites.draw(screen)
    screen.blit(element_1, (640, 64))
    screen.blit(element_2, (704, 64))
    screen.blit(element_3, (673, 128))
    screen.blit(adunatio, (624, 16))
    screen.blit(calefactus, (416, 576))
    screen.blit(division, (624, 240))
  #  screen.blit(tryi, (416, 576))
    pygame.display.flip()
con.close()