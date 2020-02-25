import pygame
from plane_sprites import *

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480,700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
pygame.display.update()


# 绘制英雄
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(200,500))
# 可以在所以绘制工作完成后，一次执行update方法，绘制所以图像
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 飞机初始位置
hero_rect = pygame.Rect(150, 100, 102, 126)


# 创建敌机精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)
# 创建敌机精灵组
enemy_groug = pygame.sprite.Group(enemy, enemy1)


# 游戏循环

while True:
    # 可以控制游戏循环内部代码每秒循环次数
    clock.tick(60)

    # 监听事件
    for event in pygame.event.get():

        # 判断事件类型  退出事件
        if event.type == pygame.QUIT:
            print("游戏退出。。。")
            # quit 卸载所以模块
            pygame.quit()
            # 终止程序
            exit()

    # 修改飞机位置
    hero_rect.y -= 1
    # 判断飞机的位置
    # if hero_rect.y + hero_rect.height <= 0:
    #     hero_rect.y = 700
    if hero_rect.bottom <= 0:
        hero_rect.y = 700
    # 调用blit 方法绘制图像
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)

    # 精灵组调用两个方法
    # update - 让组中所有精灵更新位置
    enemy_groug.update()

    # draw - 在screen上绘制所有精灵
    enemy_groug.draw(screen)

    pygame.display.update()


pygame.quit()
