import pygame as pg


class Bullet:
    def __init__(self,tk_game):
        self.screen=tk_game.screen
        self.settings=tk_game.settings

        self.rect=pg.Rect(0,0,self.settings.BUL_WIDTH,
            self.settings.BUL_HEIGHT)
        self.rect.midbottom=tk_game.my_tank.rect.midtop

    def move(self):
        self.rect.y-=self.settings.BUL_SPEED

    def draw(self):
        pg.draw.rect(self.screen,
            self.settings.BUL_COL,self.rect)