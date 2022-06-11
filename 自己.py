import pygame
import sys
import os
import time
import random
from pygame.sprite import Sprite
fclock = pygame.time.Clock()
file = r'C:\Users\Lenovo\Desktop\魂斗罗\123.mp3'
#file = r'C:\Users\Lenovo\Desktop\魂斗罗\234.mp3'
file1 = r'C:\Users\Lenovo\Desktop\魂斗罗\boom.mp3'
fps = 40  # 跳缓冲
fps1 = 20
fps2 = 20
fps3 = 10
speed1 = 10#运动速度
speed2 = 80
speed3 = 10#防止向左跑出屏幕
speed4 = 5 #用来防止向左跳出屏幕
a = []  # 子弹集合
b = [] #敌人集合


diren_flag = 1
hight = 700
H = 270
pygame.mixer.init()
#初始化背景
screenx = 0
screeny = 0
pygame.display.set_caption("魂斗罗")
screen_image = pygame.display.set_mode((1200, 750))
screen_rect = screen_image.get_rect()
bg = pygame.image.load('images/map01.bmp')
screen_image.blit(bg, (screenx, screeny))      
class player:
    def __init__(self):
        self.temp = 0
        self.playerx = 0  # 横坐标
        self.playery = 0  # 纵坐标
        self.flag = 0  # 状态 1代表站立，2向右跑，3向左跑，4向右趴下，5向左趴下,6向右上，7向坐上,8死了
        self.buttles = []  # 子弹
        self.player_image = pygame.image.load('images/player.bmp') #记录刷新前的状态
        self.life = 3 #三次机会
    def show(self):  # 开场动画
        self.flag = 1
        self.player_image = pygame.image.load("images/jump2.bmp")
        for i in range(3):
            #screen_image.blit(bg, (screenx, screeny))
            self.playery += 30
            self.playerx += 15
            fclock.tick(fps)
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery, 97, 109))
            pygame.display.flip()
            fclock.tick(fps)

        self.player_image = pygame.image.load("images/jump3.bmp")
        for i in range(3):
            screen_image.blit(bg, (screenx, screeny))
            self.playery += 30
            self.playerx += 15
            fclock.tick(fps)
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery, 97, 109))
            pygame.display.flip()
            fclock.tick(fps)

        self.player_image = pygame.image.load("images/jump4.bmp")

        for i in range(3):
            screen_image.blit(bg, (screenx, screeny))
            self.playery += 30
            self.playerx += 15
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery, 97, 109))
            pygame.display.flip()
            fclock.tick(fps)
        self.player_image = pygame.image.load('images/player.bmp')
        screen_image.blit(bg, (screenx, screeny))
        screen_image.blit(self.player_image,
                          (self.playerx, self.playery, 97, 109))
        pygame.display.flip()
        fclock.tick(fps)

    def rrun(self):  # x向右跑，一个动作一张图片
        global screenx
        self.flag = 2  # 向右跑
        if self.playerx < 135:  # 小于135的时候人物移动
            self.player_image = pygame.image.load('images/player1.bmp')

            screen_image.blit(bg, (screenx, screeny))

            self.playerx += speed1
            screen_image.blit(self.player_image,(self.playerx, self.playery, 97, 109))
            pygame.display.update()
            fclock.tick(fps1)

            self.player_image = pygame.image.load('images/player2.bmp')
            self.playerx += speed1
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,(self.playerx, self.playery, 97, 109))
            pygame.display.update()
            fclock.tick(fps1)
            self.player_image = pygame.image.load('images/player3.bmp')
            screen_image.blit(bg, (screenx, screeny))
            self.playerx += speed1
            screen_image.blit(self.player_image,(self.playerx, self.playery, 97, 109))
            pygame.display.update()
            fclock.tick(fps1)
            self.player_image = pygame.image.load('images/player4.bmp')

            screen_image.blit(bg, (screenx, screeny))
            self.playerx += speed1
            screen_image.blit(self.player_image,(self.playerx, self.playery, 97, 109))
            pygame.display.update()
            fclock.tick(fps1)
            self.player_image = pygame.image.load('images/player5.bmp')
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,(self.playerx, self.playery, 97, 109))
            pygame.display.update()
            fclock.tick(fps1)
            self.player_image = pygame.image.load('images/player.bmp')
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,(self.playerx, self.playery, 97, 109))
            pygame.display.update()
            fclock.tick(fps1)
        else:  # 大于135的时候背景移动
            self.player_image = pygame.image.load('images/player1.bmp')
            screenx -= speed1
            screen_image.blit(bg, (screenx, screeny))

            #self.playerx += speed1
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery, 97, 109))
            pygame.display.update()
            fclock.tick(fps1)

            self.player_image = pygame.image.load('images/player2.bmp')

            screenx -= speed1
            #self.playerx += speed1
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,(self.playerx, self.playery, 97, 109))
            pygame.display.update()
            fclock.tick(fps1)
            self.player_image = pygame.image.load('images/player3.bmp')
            screenx -= speed1
            screen_image.blit(bg, (screenx, screeny))
        # self.playerx += speed1
            screen_image.blit(self.player_image,(self.playerx, self.playery, 97, 109))
            pygame.display.update()
            fclock.tick(fps1)
            self.player_image = pygame.image.load('images/player4.bmp')
            screenx -= speed1
            screen_image.blit(bg, (screenx, screeny))
            #self.playerx += speed1
            screen_image.blit(self.player_image,(self.playerx, self.playery, 97, 109))
            pygame.display.update()
            fclock.tick(fps1)
            self.player_image = pygame.image.load('images/player5.bmp')
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,(self.playerx, self.playery, 97, 109))
            pygame.display.update()
            fclock.tick(fps1)
            self.player_image = pygame.image.load('images/player.bmp')
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,(self.playerx, self.playery, 97, 109))
            pygame.display.update()
            fclock.tick(fps1)

    def lrun(self):  # 向左跑，一个动作一张图片
        global speed3
        self.flag = 3  # 向左跑
        if self.playerx <= 0:
            speed3 = 0
        else:
            speed3 = 10
        self.player_image = pygame.image.load('images/player11.bmp')
        screen_image.blit(bg, (screenx, screeny))
        self.playerx -= speed3
        screen_image.blit(self.player_image,
                          (self.playerx, self.playery, 97, 109))
        pygame.display.flip()
        fclock.tick(fps1)

        self.player_image = pygame.image.load('images/player12.bmp')
        screen_image.blit(bg, (screenx, screeny))
        self.playerx -= speed3
        screen_image.blit(self.player_image,
                          (self.playerx, self.playery, 97, 109))
        pygame.display.flip()
        fclock.tick(fps1)
        self.player_image = pygame.image.load('images/player13.bmp')
        screen_image.blit(bg, (screenx, screeny))
        self.playerx -= speed3
        screen_image.blit(self.player_image,
                          (self.playerx, self.playery, 97, 109))
        pygame.display.flip()
        fclock.tick(fps1)
        self.player_image = pygame.image.load('images/player14.bmp')
        screen_image.blit(bg, (screenx, screeny))
        self.playerx -= speed3
        screen_image.blit(self.player_image,
                          (self.playerx, self.playery, 97, 109))
        pygame.display.flip()
        fclock.tick(fps1)
        self.player_image = pygame.image.load('images/player15.bmp')
        screen_image.blit(bg, (screenx, screeny))
        screen_image.blit(self.player_image,
                          (self.playerx, self.playery, 97, 109))
        pygame.display.flip()
        fclock.tick(fps1)
        self.player_image = pygame.image.load('images/player10.bmp')
        screen_image.blit(bg, (screenx, screeny))
        screen_image.blit(self.player_image,
                          (self.playerx, self.playery, 97, 109))
        pygame.display.flip()
        fclock.tick(fps1)

    def down(self):
        if self.flag == 3:
            self.player_image = pygame.image.load('images/ldown.bmp')
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery+45, 97, 109))
            pygame.display.flip()
            fclock.tick(fps1)
            self.flag = 5
        elif self.flag == 1 or self.flag == 2:
            self.player_image = pygame.image.load('images/rdown.bmp')
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery+45, 97, 109))
            pygame.display.flip()
            fclock.tick(fps1)
            self.flag = 4

    def up(self):
        if self.flag == 2 or self.flag == 1:  # 站立时的向上
            self.player_image = pygame.image.load('images/rup.bmp')
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery-25, 97, 109))
            pygame.display.flip()
            fclock.tick(fps1)
            self.flag = 6
        if self.flag == 4:  # 趴下时的向上
            self.player_image = pygame.image.load('images/rup.bmp')
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery-25, 97, 109))
            pygame.display.flip()
            fclock.tick(fps1)
            self.flag = 6
        if self.flag == 3:  # 向左的时候向上
            self.player_image = pygame.image.load('images/lup.bmp')
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery-25, 97, 109))
            pygame.display.flip()
            fclock.tick(fps1)
            self.flag = 7
        if self.flag == 5:  # 向坐趴下时的向上
            self.player_image = pygame.image.load('images/lup.bmp')
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery-25, 97, 109))
            pygame.display.flip()
            fclock.tick(fps1)
            self.flag = 7

    def jump(self):
        global speed4, hight, screenx, H
        if self.playerx <= 100:
            speed4 = 0
        else:
            speed4 = 5
        if self.flag == 1:
            self.player_image = pygame.image.load("images/jump1.bmp")
            for i in range(10):
                self.playery -= 10
                fclock.tick(fps)
                screen_image.blit(bg, (screenx, screeny))
                screen_image.blit(self.player_image,
                                  (self.playerx, self.playery, 97, 109))
                pygame.display.flip()
            self.player_image = pygame.image.load("images/jump2.bmp")
            fclock.tick(fps)
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery, 97, 109))
            pygame.display.flip()
            self.player_image = pygame.image.load("images/jump3.bmp")
            fclock.tick(fps)
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery, 97, 109))
            pygame.display.flip()
            self.player_image = pygame.image.load("images/jump4.bmp")
            fclock.tick(fps)
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery, 97, 109))
            self.player_image = pygame.image.load("images/jump1.bmp")
            for i in range(10):
                self.playery += 10
                fclock.tick(fps)
                screen_image.blit(bg, (screenx, screeny))
                screen_image.blit(self.player_image,
                                  (self.playerx, self.playery, 97, 109))
                pygame.display.flip()
            self.player_image = pygame.image.load('images/player.bmp')
            fclock.tick(fps)
            screen_image.blit(bg, (screenx, screeny))
            if self.playery - 150 <= H:
                self.stand()
            else:
                screen_image.blit(self.player_image,
                                  (self.playerx, self.playery, 97, 109))
            pygame.display.flip()
        if self.flag == 2:
            self.player_image = pygame.image.load("images/jump1.bmp")
            for i in range(10):
                self.playery -= 10
                screenx -= 5
                fclock.tick(fps)
                screen_image.blit(bg, (screenx, screeny))
                screen_image.blit(self.player_image,
                                  (self.playerx, self.playery, 97, 109))
                pygame.display.flip()
            self.player_image = pygame.image.load("images/jump2.bmp")
            fclock.tick(fps)
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery, 97, 109))
            pygame.display.flip()
            self.player_image = pygame.image.load("images/jump3.bmp")
            fclock.tick(fps)
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery, 97, 109))
            pygame.display.flip()
            self.player_image = pygame.image.load("images/jump4.bmp")
            fclock.tick(fps)
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery, 97, 109))
            self.player_image = pygame.image.load("images/jump1.bmp")
            for i in range(10):
                self.playery += 10
                screenx -= 5
                fclock.tick(fps)
                screen_image.blit(bg, (screenx, screeny))
                screen_image.blit(self.player_image,
                                  (self.playerx, self.playery, 97, 109))
                pygame.display.flip()
            self.player_image = pygame.image.load('images/player.bmp')
            fclock.tick(fps)
            screen_image.blit(bg, (screenx, screeny))
            if self.playery - 150 <= H:
                self.stand()
            else:
                screen_image.blit(self.player_image,
                                  (self.playerx, self.playery, 97, 109))
            pygame.display.flip()
        if self.flag == 3:  # 向左跑
            self.player_image = pygame.image.load("images/ljump1.bmp")
            for i in range(10):
                self.playery -= 10
                self.playerx -= speed4
                fclock.tick(fps)
                screen_image.blit(bg, (screenx, screeny))
                screen_image.blit(self.player_image,
                                  (self.playerx, self.playery, 97, 109))
                pygame.display.flip()
            self.player_image = pygame.image.load("images/ljump2.bmp")
            fclock.tick(fps)
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery, 97, 109))
            pygame.display.flip()
            self.player_image = pygame.image.load("images/ljump3.bmp")
            fclock.tick(fps)
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery, 97, 109))
            pygame.display.flip()
            self.player_image = pygame.image.load("images/ljump4.bmp")
            fclock.tick(fps)
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,
                              (self.playerx, self.playery, 97, 109))
            self.player_image = pygame.image.load("images/ljump1.bmp")
            for i in range(10):
                self.playery += 10
                self.playerx -= speed4
                fclock.tick(fps)
                screen_image.blit(bg, (screenx, screeny))
                screen_image.blit(self.player_image,
                                  (self.playerx, self.playery, 97, 109))
                pygame.display.flip()
            self.player_image = pygame.image.load('images/player.bmp')
            fclock.tick(fps)
            screen_image.blit(bg, (screenx, screeny))
            if self.playery - 150 <= H:
                self.stand()
            else:
                screen_image.blit(self.player_image,
                                  (self.playerx, self.playery, 97, 109))
            pygame.display.flip()
        if self.flag == 4:  # 向右趴
            self.luo(hight)
            self.flag = 2
        if self.flag == 5:
            self.luo(hight)
            self.flag = 3

    def luo(self, high):
        if self.flag == 4 or self.flag == 2:  # 向右的落
            self.player_image = pygame.image.load('images/player2.bmp')
            while self.playery < high:
                self.playery += 10
                screen_image.blit(bg, (screenx, screeny))
                screen_image.blit(self.player_image,
                                  (self.playerx, self.playery, 97, 109))
                fclock.tick(fps)
                pygame.display.flip()
        if self.flag == 5 or self.flag == 3:
            self.player_image = pygame.image.load('images/player12.bmp')
            while self.playery < high:
                self.playery += 10
                screen_image.blit(bg, (screenx, screeny))
                screen_image.blit(self.player_image,
                                  (self.playerx, self.playery, 97, 109))
                fclock.tick(fps)
                pygame.display.flip()

    def stand(self):  # 从下往上跳
        self.flag = 2
        self.player_image = pygame.image.load('images/player.bmp')
        screen_image.blit(bg, (screenx, screeny))
        self.playery = H
        screen_image.blit(self.player_image,
                          (self.playerx, self.playery, 97, 109))
        pygame.display.flip()
        fclock.tick(fps1)
    def death(self): #人物死亡
        self.player_image = pygame.image.load('images/death1.bmp')
        for i in range(5):
            self.playerx -= 2
            self.playery -= 2
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,(self.playerx, self.playery, 97, 109))
            pygame.display.flip()
            fclock.tick(30)
        self.player_image = pygame.image.load('images/death2.bmp')
        for i in range(5):
            self.playerx -= 2
            self.playery += 2
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player_image,(self.playerx, self.playery+70, 97, 109))
            pygame.display.flip()
            fclock.tick(30)

class hundouluo:
    global screenx,diren_flag
    def __init__(self):#初始化游戏
        self.player = player()
        self.player.show()
        j = 0
        for i in range(5):
            i = [self.player.playerx+1200+j*350, 270]
            b.append(i)
            j += 1

    def start_game(self):
        global speed3,diren_flag
        track = pygame.mixer.music.load(file)
        #pygame.mixer.music.play()
        while True:
            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.play()
            if self.player.life > 0 and self.player.flag == 8:
                self.player.show()
                self.player.flag = 1
            if self.player.life == 0:
                exit()
            self.__event_handler()
            self.bgmap()
            #self.diren()
            for i in a:
                buttle_image = pygame.image.load("images/bullet1.bmp")
                screen_image.blit(bg, (screenx, screeny))
                screen_image.blit(self.player.player_image,(self.player.playerx,self.player.playery,99,107))
                screen_image.blit(buttle_image,(i[0],i[1],15,15))
                #screen_image.blit(bg, (screenx, screeny))
                pygame.display.update()
                fclock.tick(fps)
            for i in a:
                if i[2] == 2 or i[2] == 4 or i[2] == 1:  # 向右
                    i[0] += speed2
                if i[2] == 3 or i[2] == 5:  # 向左
                    i[0] -= speed2
                if i[2] == 6 or i[2] == 7:  # 向上
                    i[1] -= speed2
                if i[0] > 1200 or i[0] < 0:
                    a.remove(i)
                if i[1] < 0 or i[1] > 750:
                    a.remove(i)
            
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys_pressed = pygame.key.get_pressed()
            
            #判断元组中对应的按键索引值 1
        if keys_pressed[pygame.K_d] and self.player.temp == 0:#向右跑
            self.player.rrun()
        if keys_pressed[pygame.K_a] and self.player.temp == 0:#向左跑
            self.player.lrun()
        if keys_pressed[pygame.K_s] and self.player.temp == 0:#趴下
            self.player.down()
        if keys_pressed[pygame.K_w] and self.player.temp == 0:#趴下
            self.player.up()
        if keys_pressed[pygame.K_k] and self.player.temp == 0:#跳跃
            self.player.jump()
        if keys_pressed[pygame.K_j]:  # 子弹
            if self.player.flag == 1 or self.player.flag == 2:
                a.append([self.player.playerx+100,self.player.playery+25, self.player.flag])
            if self.player.flag == 3 :
                a.append([self.player.playerx-100,self.player.playery+25, self.player.flag])
            if self.player == 5:
                a.append([self.player.playerx,self.player.playery-75, self.player.flag])
            if self.player.flag == 6:
                a.append([self.player.playerx+25, self.player.playery-20, self.player.flag])
    def bgmap(self): #地图路线
        global hight,H
        global screenx
        if self.player.playerx < 50 and self.player.playery == 270 and screenx == 0:
            self.player.luo(680)
        if -690 < screenx < -390 and self.player.playery == 270:#第一块
            hight = 380
        if -690 < screenx < -390 and self.player.playery == 380:
            hight = 680
        if  -800< screenx < -690 and self.player.playery == 380:
            self.player.luo(480)
            hight = 680
        if -740 < screenx < -690 and self.player.playery == 480:
            H = 380
        if -800 < screenx < -690 and self.player.playery == 270:
            hight = 480
            H = 380
        if -800 < screenx < -690 and self.player.playery == 480:
            hight = 680
        if -800 < screenx < -750 and self.player.playery == 680:
            H = 600
        if -900 < screenx < -800 and self.player.playery == 480:
            self.player.luo(600)
        if -1000 < screenx < -800 and self.player.playery == 270:
            hight = 600
        if  -1100 < screenx < -1000 and self.player.playery == 600:
            self.player.luo(680)
        if -1120 < screenx < -1000 and self.player.playery == 270:
            hight = 480
        if -1260 < screenx < -1130 and self.player.playery == 480:
            self.player.luo(680)
        if -1520 < screenx < -1260 and self.player.playery == 270:
            hight = 380
        if -1520 < screenx < -1260 and self.player.playery == 380:
            hight = 680
        if -1650 < screenx < -1520 and self.player.playery == 380:
            self.player.luo(680)
        if -1910 < screenx < -1520 and self.player.playery == 270:
            hight = 680
        if -2040 < screenx < -1910 and self.player.playery == 270:
            hight = 600
        if -2250 < screenx < -2100 and self.player.playery == 600:
            self.player.luo(680)
        if -2430 < screenx < -2040 and self.player.playery == 270:
            hight = 480
        if -2170 < screenx < -2040 and self.player.playery == 480:
            hight = 680
        if -2820 < screenx < -2350 and self.player.playery == 270:
            self.player.luo(680)
        if -4860 < screenx < -4500 and self.player.playery == 680:
            self.player.playery = 600
        if -5600 < screenx < -4860 and self.player.playery == 600:
            self.player.luo(680)
        if -6240 < screenx < -5600 and self.player.playery == 680:
            self.player.playery = 600
        if screenx < -6240 and self.player.playery == 600:
            self.player.luo(680)
            if self.player.playery >= 680:
                self.player.death()
                self.player.life -= 1
                self.player.flag = 8
                self.player.playerx -= 90
                self.player.playery = 0 
        if -6600 < screenx < -6500 and self.player.playery >= 480:
            self.player.death()
            self.player.life -= 1
            self.player.flag = 8
            self.player.playerx -= 90
            self.player.playery = 0 
        if -7020 < screenx < -6900 and self.player.playery >= 480:
            self.player.death()
            self.player.life -= 1
            self.player.flag = 8
            self.player.playerx -= 90
            self.player.playery = 0
        if -7150 < screenx < -7040 and self.player.playery >= 430:
            self.player.death()
            self.player.life -= 1
            self.player.flag = 8
            self.player.playerx -= 90
            self.player.playery = -130
        if -7240 < screenx < -7150 and self.player.playery == 140:
            hight = 380
        if screenx < -7240 and self.player.playery == 140:
            self.player.luo(380)
        if -7600 < screenx < -7480 and self.player.playery >= 380:
            self.player.death()
            self.player.life -= 1
            self.player.flag = 8
            self.player.playerx -= 90
            self.player.playery = 0
        if -7760 < screenx < -7600 and self.player.playery ==270:
            self.player.luo(600)
    def update(self):
        pass
    def diren(self):
        global diren_flag
        #track1 = pygame.mixer.music.load(file1)
        for i in b:
            screen_image.blit(bg, (screenx, screeny))
            screen_image.blit(self.player.player_image, (self.player.playerx, self.player.playery, 99, 107))
            if diren_flag == 1:
                diren_image = pygame.image.load("images/bag1.bmp")
                screen_image.blit(diren_image, (i[0], i[1], 69, 95))
                pygame.display.flip()
                fclock.tick(50)
                diren_flag += 1

            if diren_flag == 2:
                diren_image = pygame.image.load("images/bag2.bmp")
                screen_image.blit(diren_image, (i[0], i[1], 69, 95))
                pygame.display.flip()
                fclock.tick(50)
                diren_flag += 1
            if diren_flag == 3:
                diren_image = pygame.image.load("images/bag3.bmp")
                screen_image.blit(diren_image, (i[0], i[1], 69, 95))
                pygame.display.flip()
                fclock.tick(50)
                diren_flag += 1
            if diren_flag == 4:
                diren_image = pygame.image.load("images/bag4.bmp")
                screen_image.blit(diren_image, (i[0], i[1], 69, 95))
                pygame.display.flip()
                fclock.tick(50)
                diren_flag = 1
        for i in b:
            i[0] -= 80
            if abs(i[0] - self.player.playerx) <= 20 and abs(i[1] - self.player.playery) <=20:
                self.player.death()
                self.player.life -= 1
                self.player.flag = 8
                self.player.playerx -= 90
                self.player.playery = 0 
                b.remove(i)
                pygame.display.flip()
            for j in a:
                if i[0] - j[0] <= 20:
                    #pygame.mixer.music.play()
                    boom = pygame.image.load("images/boom1.bmp")
                    screen_image.blit(boom,(i[0],i[1],97,74))
                    fclock.tick(10)
                    pygame.display.flip()
                    boom = pygame.image.load("images/boom2.bmp")
                    screen_image.blit(boom,(i[0],i[1],97,74))
                    fclock.tick(10)
                    pygame.display.flip()
                    b.remove(i)
                    a.remove(j)
if __name__ == '__main__':
    game = hundouluo()
    game.start_game()
        
