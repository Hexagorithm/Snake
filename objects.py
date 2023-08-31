import pygame as pg
import settings as st

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
        self.surface.blit(self.image, (self.x_real, self.y_real))

    def move(self):
        if self.curr_dir == 'right':
            self.x_real += st.snake_speed
        elif self.curr_dir == 'left':
            self.x_real -= st.snake_speed
        elif self.curr_dir == 'up':
            self.y_real -= st.snake_speed
        elif self.curr_dir == 'down':
            self.y_real += st.snake_speed

    def dir_update(self):
        if self.new_dir == 'right' and self.curr_dir not in [None, 'left']:
            self.curr_dir = self.new_dir
            self.new_dir = None
        elif self.new_dir == 'left' and self.curr_dir not in [None, 'right']:
            self.curr_dir = self.new_dir
            self.new_dir = None
        elif self.new_dir == 'up' and self.curr_dir not in [None, 'down']:
            self.curr_dir = self.new_dir
            self.new_dir = None
        elif self.new_dir == 'down' and self.curr_dir not in [None, 'up']:
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

    def update(self):
        self.dir_update()
        self.move()
