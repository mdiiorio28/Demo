# This file was created by Mikey DiIorio
# Thanks to Chris Bradfield for the "Kids Can Code" Series

import pygame as pg
import random
from settings import *
from sprites import *
from time import *

class Game:
    def __init__(self): 
        #-Game window
        #Init pygame and create...
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Enigma")
        self.clock = pg.time.Clock()
        self.running = True
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()
        #Create new player
        pass
    def run(self):
        self.playing = True
        #Game loop
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pass
    def update(self):
        self.all_sprites.update()

        #Update game
        pass
    def events(self):
        #Lisening for events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        #Double Buffer
        pg.display.flip()
        #Draw character (and others)
        pass
    def show_start_screen(self):
        #Show the start screen
        pass
    def show_go_screen(self):
        #Show the go screen
        pass

g = Game()
g.show_start_screen()
while g.running: 
    g.new()
    g.show_go_screen()

pg.quit()