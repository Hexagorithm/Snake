import pygame as pg
import settings as st
from abc import ABC, abstractmethod
from objects import TileMap, TileBorder, SnakeHead

class Screen(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def events(self):
        pass
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def change_mode(self):
        pass

class Game:

    def __init__(self,screen_size):
        self.screen_size = screen_size

        self.running = True
        self.mode = 'playing'
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(size=self.screen_size)
        icon = pg.image.load(st.snake_head_path)
        caption = 'Snake'
        pg.display.set_caption(caption)
        pg.display.set_icon(icon)

    def get_mode(self):
        if self.mode == 'playing':
            return Playing(self.screen)
        elif self.mode == 'screen1':
            return ScreenLoss(self.screen)
        elif self.mode == 'screen2':
            return Screen2(self.screen)

    def end(self):
        pg.quit()

    def run(self):
        while self.running:
            curr_mode = self.get_mode()
            while curr_mode.running:
                curr_mode.events()
                curr_mode.display()
                pg.display.update()
                self.clock.tick(st.fps)
                new_mode = curr_mode.change_mode()
                if new_mode == None:
                    # mode was not changed
                    pass

                elif new_mode == 'quit':
                    # mode was changed to quit game
                    self.running = False
                    break

                elif new_mode == 'screen1':
                    # mode was changed to SomethingElse
                    self.mode = 'screen1'
                    break
                elif new_mode == 'screen2':
                    # mode was changed to SomethingElse
                    self.mode = 'screen2'
                    break
                elif new_mode == 'playing':
                    self.mode = 'playing'
                    break
        self.end()


class Playing(Screen):

    def __init__(self, screen):
        self.screen = screen

        self.running = True
        self.changed_mode = None
        self.create_map()
        self.create_snake()

    def create_map(self):
        self.tiles_border = pg.sprite.Group()
        self.tiles_map = pg.sprite.Group()
        for y in range(st.real_tile_amount[1]):
            for x in range(st.real_tile_amount[0]):
                if y == 0 or x == 0 or y == st.real_tile_amount[1] - 1 or x == st.real_tile_amount[0] - 1:
                    tile = TileBorder(x,y,self.screen)
                    self.tiles_border.add(tile)
                else:
                    tile = TileMap(x,y,self.screen)
                    self.tiles_map.add(tile)

    def create_snake(self):
        self.snake_head = SnakeHead(st.spawn_cord,self.screen)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.changed_mode = 'quit'
            if event.type == pg.KEYDOWN:
                if event.unicode in ['w', 's', 'a', 'd']:
                    self.snake_head.dir_change(event.unicode)

    def check_if_loss(self):
        for tile in self.tiles_border:
            if self.snake_head.rect.colliderect(tile.rect):
                self.running = False
                self.changed_mode = 'screen1'

    def display(self):
        self.screen.fill('green')
        for tile in self.tiles_border:
            tile.draw()
        for tile in self.tiles_map:
            tile.draw()
        self.snake_head.update()
        self.snake_head.draw()
        self.check_if_loss()

    def change_mode(self):
        return self.changed_mode




class ScreenLoss(Screen):

    def __init__(self,screen):
        self.screen = screen

        self.running = True
        self.changed_mode = None

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.changed_mode = 'quit'
            if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if keys[pg.K_1]:
                    self.changed_mode = 'screen1'
                elif keys[pg.K_2]:
                    self.changed_mode = 'screen2'
                elif keys[pg.K_3]:
                    self.changed_mode = 'playing'


    def display(self):
        self.screen.fill('red')

    def change_mode(self):
        return self.changed_mode

class Screen2(Screen):

    def __init__(self,screen):
        self.screen = screen

        self.running = True
        self.changed_mode = None

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.changed_mode = 'quit'
            if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if keys[pg.K_1]:
                    self.changed_mode = 'screen1'
                elif keys[pg.K_2]:
                    self.changed_mode = 'screen2'
                elif keys[pg.K_3]:
                    self.changed_mode = 'playing'


    def display(self):
        self.screen.fill('blue')

    def change_mode(self):
        return self.changed_mode
