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
        self.platforms = pg.sprite. Group()
        # Player 1
        self.player = Player(self)
        self.all_sprites.add(self.player)
        # Player 2
        self.player_2 = Player(self)
        self.player_2.image.fill(WHITE)
        self.player_2.up = pg.K_w
        self.player_2.left = pg.K_a
        self.player_2.right = pg.K_d
        self.all_sprites.add(self.player_2)
        # Platforms
        for plat in PLAT_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
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
        #Collision code
        self.all_sprites.update()
        hits_1 = pg.sprite.spritecollide(self.player, self.platforms, False)
        hits_2 = pg.sprite.spritecollide(self.player_2, self.platforms, False)
        if hits_1:
            self.player.pos.y = hits_1[0].rect.top + 1
            self.player.vel.y = 0
        if hits_2:
            self.player_2.pos.y = hits_2[0].rect.top + 1
            self.player_2.vel.y = 0
        if self.player.rect.bottom > HEIGHT:
            self.playing = False

        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        #Update game
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == self.player.up:
                    self.player.jump()

            if event.type == pg.KEYDOWN:
                if event.key == self.player.up:
                    self.player.jump()
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