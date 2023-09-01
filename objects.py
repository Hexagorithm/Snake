import pygame as pg
import settings as st
from math import ceil, floor

class TileBorder(pg.sprite.Sprite):

    def __init__(self,x,y,surface):
        super().__init__()
        self.x = x
        self.y = y
        self.surface = surface
        self.create()

    def create(self):
        self.image = pg.image.load(st.tile_border_path)
        self.image = pg.transform.scale(self.image, st.tile_size)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x * st.tile_size[0], self.y * st.tile_size[1])

    def draw(self):
        self.surface.blit(self.image, self.rect)

class TileMap(pg.sprite.Sprite):

    def __init__(self,x,y,surface):
        super().__init__()
        self.x = x
        self.y = y
        self.surface = surface
        self.create()

    def create(self):
        self.image = pg.image.load(self.get_image())
        self.image = pg.transform.scale(self.image, st.tile_size)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x * st.tile_size[0], self.y * st.tile_size[1])

    def get_pos(self):
        return self.x, self.y

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def get_image(self):
        return st.tile_map_dict[(self.x + self.y) % 2]

class SnakeHead(pg.sprite.Sprite):

    def __init__(self, spawn_cords,surface):
        super().__init__()
        self.x,self.y = spawn_cords
        self.surface = surface

        self.curr_dir = 'right'
        self.new_dir = None
        self.x_real = self.x * st.tile_size[0]
        self.y_real = self.y * st.tile_size[1]
        self.create()

    def create(self):
        self.image = pg.image.load(st.snake_head_path)
        self.image = pg.transform.scale(self.image, st.tile_size)

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def move(self):
        if self.curr_dir == 'right':
            self.x += st.snake_speed / st.tile_size[0]
        elif self.curr_dir == 'left':
            self.x -= st.snake_speed / st.tile_size[0]
        elif self.curr_dir == 'up':
            self.y -= st.snake_speed / st.tile_size[1]
        elif self.curr_dir == 'down':
            self.y += st.snake_speed / st.tile_size[1]
        self.x_real = self.x * st.tile_size[0]
        self.y_real = self.y * st.tile_size[1]
        self.create_rect()

    def turn(self):
        dir_list = ['up', 'left', 'down', 'right']
        before = dir_list.index(self.curr_dir)
        after = dir_list.index(self.new_dir)
        times2turn = after - before
        self.image = pg.transform.rotate(self.image, 90 * times2turn)

    def dir_update(self):
        if self.new_dir == 'right' and self.curr_dir not in [None, 'left']:
            self.turn()
            self.allign()
            self.curr_dir = self.new_dir
            self.new_dir = None
        elif self.new_dir == 'left' and self.curr_dir not in [None, 'right']:
            self.turn()
            self.allign()
            self.curr_dir = self.new_dir
            self.new_dir = None
        elif self.new_dir == 'up' and self.curr_dir not in [None, 'down']:
            self.turn()
            self.allign()
            self.curr_dir = self.new_dir
            self.new_dir = None
        elif self.new_dir == 'down' and self.curr_dir not in [None, 'up']:
            self.turn()
            self.allign()
            self.curr_dir = self.new_dir
            self.new_dir = None
        else:
            self.new_dir = None

    def dir_change(self,key):
        if key == 'w':
            self.new_dir = 'up'
        elif key == 's':
            self.new_dir = 'down'
        elif key == 'a':
            self.new_dir = 'left'
        elif key == 'd':
            self.new_dir = 'right'

    def create_rect(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x_real, self.y_real)

    def allign(self):
        if self.new_dir in ['right','left'] and self.curr_dir  == 'up':    # allign vertically
            self.y = floor(self.y)
        elif self.new_dir in ['right', 'left'] and self.curr_dir == 'down':  # allign vertically
            self.y = ceil(self.y)
        elif self.new_dir in ['up','down'] and self.curr_dir  == 'right':    # allign vertically
            self.x = ceil(self.x)
        elif self.new_dir in ['up','down'] and self.curr_dir  == 'left':    # allign vertically
            self.x = floor(self.x)

    def update(self):
        self.dir_update()
        self.move()

class Upgrade(pg.sprite.Sprite):

    def __init__(self, cords, screen):
        super().__init__()
        self.x, self.y = cords
        self.screen = screen

        self.real_x = self.x * st.tile_size[0]
        self.real_y = self.y * st.tile_size[1]
        self.create()

    def create(self):
        self.image = pg.image.load(st.upgrade_path)
        self.image = pg.transform.scale(self.image, st.tile_size)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.real_x, self.real_y)

    def draw(self):
        self.screen.blit(self.image, self.rect)

class SnakeTail(pg.sprite.Sprite):

    def __init__(self,cords , identity, surface):
        self.x, self.y = cords
        self.identity = identity
        self.surface = surface

        self.x_real = self.x * st.tile_size
        self.y_real = self.y * st.tile_size

    def create(self):
        self.image = pg.image.load(st.snake_tail_path)
        self.image = pg.transform.scale(self.image, st.tile_size)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x_real, self.y_real)

    def get_identity(self):
        return self.identity

    def draw(self):
        self.surface.blit(self.image, self.rect)

class Shit(pg.sprite.Sprite):

    def __init__(self, cords, identity,surface):
        self.x, self.y = cords
        self.identity = identity
        self.surface = surface

        self.x_real = self.x * st.tile_size
        self.y_real = self.y * st.tile_size

    def create(self):
        self.image = pg.image.load(st.shit_path)
        self.image = pg.transform.scale(self.image, (10,10))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_real, self.y_real)

    def draw(self):
        self.surface.blit(self.image,self.rect)



