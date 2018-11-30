# Sprite classes for game

import pygame as pg
from pygame.sprite import Sprite
import random
from settings import *
from time import *
from os import path

vec = pg.math.Vector2
img = path.join(path.dirname(__file__), '_images')

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        # Shape of player character
        self.game = game
        self.image = pg.Surface((40,40))
        self.image.fill(THANOS)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 3, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.left = pg.K_LEFT
        self.right = pg.K_RIGHT
        self.up = pg.K_UP

    def update(self):
        self.acc = vec(0, 0.5)
        keys = pg.key.get_pressed()
        if keys[self.left]:
            self.acc.x = -0.5
        if keys[self.right]:
            self.acc.x = 0.5

        self.acc.x += self.vel.x * p_fric
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -15
    
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(REDDISH)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

