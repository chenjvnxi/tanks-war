import pygame as pg
class MyTank:
    def __init__(self,tk_game):
        self.settings=tk_game.settings
        self.screen=tk_game.screen
        self.scr_rect=tk_game.screen.get_rect()
        self.image=pg.image.load("tanks_war\images\lv1.bmp")
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.scr_rect.midbottom
        self.move_u=False
        self.move_d=False
        self.move_r=False
        self.move_l=False

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def move(self):
        if self.move_u and self.rect.top>0:
            self.rect.y-=self.settings.MY_TANK_SPEED
        if self.move_d and self.rect.bottom<self.scr_rect.bottom:
            self.rect.y+=self.settings.MY_TANK_SPEED
        if self.move_r and self.rect.right<self.scr_rect.right:
            self.rect.x+=self.settings.MY_TANK_SPEED
        if self.move_l and self.rect.left>0:
            self.rect.x-=self.settings.MY_TANK_SPEED