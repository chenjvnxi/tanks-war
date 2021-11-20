from collections import defaultdict
import json
import sys
from typing import DefaultDict

import pygame as pg

import caching
from bullet import Bullet
from enemy_tank import Enemy
from my_tank import MyTank
from settings import Settings


class TanksWar:
    def __init__(self) ->None:
        pg.init()
        self.settings=Settings()
        self.screen=pg.display.set_mode(
            (0,0),pg.FULLSCREEN)
        pg.display.set_caption(
            "Tanks war")
        self.clock=pg.time.Clock()
        self.my_tank=MyTank(self)
        self.bullets=[]
        self.enemys=[]
        pg.mixer.Sound(open("tanks_war/mixer/start.mp3",mode="rb")).play()

        self.game_cycle()

    def game_cycle(self) ->None:
        while True:
            self.check_event()
            self.my_tank.move()
            self.bullets_move()
            self.up_screen()

    def check_event(self) ->None:
        for event in pg.event.get():
            if event.type==pg.KEYDOWN:
                self.check_kdown_event(event)
            elif event.type==pg.KEYUP:
                self.check_kup_event(event)

    def check_kdown_event(self,event) ->None:
        if event.key==pg.K_ESCAPE:
            sys.exit()
        elif event.key==pg.K_q:
            sys.exit()
        elif event.key==pg.K_UP or event.key==pg.K_w:
            self.my_tank.move_u=True
        elif event.key==pg.K_DOWN or event.key==pg.K_s:
            self.my_tank.move_d=True
        elif event.key==pg.K_LEFT or event.key==pg.K_a:
            self.my_tank.move_l=True
        elif event.key==pg.K_RIGHT or event.key==pg.K_d:
            self.my_tank.move_r=True
        elif event.key==pg.K_SPACE or event.key==pg.K_0:
            self.fire()

    def check_kup_event(self,event) ->None:
        if event.key==pg.K_UP or event.key==pg.K_w:
            self.my_tank.move_u=False
        elif event.key==pg.K_DOWN or event.key==pg.K_s:
            self.my_tank.move_d=False
        elif event.key==pg.K_LEFT or event.key==pg.K_a:
            self.my_tank.move_l=False
        elif event.key==pg.K_RIGHT or event.key==pg.K_d:
            self.my_tank.move_r=False

    def fire(self) ->None:
        if len(self.bullets)<self.settings.BUL_MAX:
            new_bul=Bullet(self)
            self.bullets.append(new_bul)

    def bullets_move(self) ->None:
        for bullet in self.bullets:
            bullet.move()
            if bullet.rect.bottom<0:
                self.bullets.remove(bullet)

#The function is incomplete
    def enemy_move(self) ->None:
        for enemy in self.enemys:
            enemy.move()

    def up_screen(self) ->None:
        self.screen.fill(
            self.settings.SCREEN_COLOR)
        self.my_tank.blitme()
        for bullet in self.bullets:
            bullet.draw()
        pg.display.flip()
        self.clock.tick(self.settings.SCREEN_FPS)


if __name__=="__main__":
    tw=TanksWar()