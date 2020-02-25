


import pygame

pygame.init()

#创建游戏窗口
screen = pygame.display.set_mode((480,700))

#绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
pygame.display.update()


# 绘制英雄
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(200,500))
# 可以在所以绘制工作完成后，一次执行update方法，绘制所以图像
pygame.display.update()

while True:
    pass


pygame.quit()