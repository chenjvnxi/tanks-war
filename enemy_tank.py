import pygame as pg
class Enemy:
    def __init__(self,status,x,y) ->None:
        self.status=status
        self.image=pg.image.load()
        self.rect=self.image.get_rect()
        self.rect.x,self.rect.y=x,y

    def blitme(self):
        pg.blit(self.image,self.rect)

    def move(self) ->None:
        self.y+=self.status.ENEMY_SPEED#Eazy move:move down