import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")

        # 设置游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，精灵和精灵组的创建
        self.__create_sprite()
        # 设置定时器事件，创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprite(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(is_alt=True)
        # bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)



    def start_game(self):
        print("游戏开始")

        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新 绘制精灵组
            self.__update_sprite()
            # 更新显示
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出厂")
                # 创建敌机精灵
                enemy = Enemy()

                # 将敌机精灵添加到精灵组
                self.enemy_group.add(enemy)
            # 监听英雄发射子弹时间 500ms
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动")
        # 使用键盘提供的方法获取键盘按键
        keys_passed = pygame.key.get_pressed()
        # 判断元祖中对应的按键索引值
        if keys_passed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_passed[pygame.K_LEFT]:
            self.hero.speed = -2
        elif keys_passed[pygame.K_UP]:
            self.hero.speed2 = -2
        elif keys_passed[pygame.K_DOWN]:
            self.hero.speed2 = 2
        else:
            self.hero.speed = 0
            self.hero.speed2 = 0


    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 判断列表是否为空
        if len(enemies) > 0:

            # 英雄牺牲
            self.hero.kill()

            # PlaneGame.__game_again(self)

            # 结束游戏
            PlaneGame.__game_over()

    # def __game_again(self):
    #     # 创建again弹窗
    #     print("提示")
    #     self.again_txt = again()
    #     self.again_group = pygame.sprite.Group(self.again_txt)
    #     # 弹出提示框
    #
    #     self.again_group.update()
    #     self.again_group.draw(self.screen)
        # 检测点击事件
        # 结束或 重新开始游戏

    def __update_sprite(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)







    @staticmethod
    def __game_over():
        print("游戏结束")
        # pygame.image.load("./images/again.png")

        pygame.quit()
        exit()

if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()

    #启动游戏
    game.start_game()
