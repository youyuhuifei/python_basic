import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self,image_name,speed=1, speed2=0):
        # 调用父类初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.speed2 = speed2

    def update(self):
        # 垂直方向移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 调用父类方法，实现精灵创建
        super().__init__("./images/background.png")
        # 判断是否是交替图像，若是，需设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类方法实现垂直移动
        super().update()

        # 判断图像是否移出屏幕，图像设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        # 调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png")

        # 指定敌机的初始随机速度
        self.speed = random.randint(1,3)

        # 指定敌机的初始随机位置
        # self.rect.y = -self.rect.height
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)


    def update(self):

        # 调用父类方法，保持垂直方向飞行
        super().update()
        # 判断是否飞出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            #print("飞出屏幕，需要从精灵组中删除")
            #kill方法可以将精灵从所有精灵组中移出
            self.kill()


    def __del__(self):
        # print("敌机挂了 %s" % self.rect)
        pass

class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        # 调用父类方法，设置image/speed
        super().__init__("./images/me1.png", 0)
        #设置英雄初始位置

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()


    def update(self):
        # super().update()

        # 英雄水平方向移动
        self.rect.x += self.speed
        # 英雄垂直方向移动
        self.rect.y += self.speed2

        if self.rect.x <= 0:
            self.rect.x = 0

        elif self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

        elif self.rect.bottom >= SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

        elif self.rect.y <= 0:
            self.rect.y = 0

    def fire(self):
        # print("发射子弹")

        for i in (0, 1, 2):

            # 创建子弹精灵
            bullet = Bullet()

            # 设置子弹初始位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            # 将子弹精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        super().__init__("./images/bullet1.png", -2)


    def update(self):
        # 调用父类方法，让子弹垂直飞行
        super().update()

        if self.rect.bottom < 0:
            self.kill()


    def __del__(self):
        pass


        #print("子弹被销毁")

# class again(GameSprite):
#
#     def __init__(self):
#         # 调用父类方法弹出again提示框
#         super().__init__("./images/again.png", 0)
#         # 设置初始位置
#         self.rect.center = SCREEN_RECT.center
#         # 设置初始速度




