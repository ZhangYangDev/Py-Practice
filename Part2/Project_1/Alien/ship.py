import pygame
# import sys
# import os
# os.chdir(os.path.dirname(sys.arvg[0]))

'''
    管理飞船的类
'''
class Ship:
    
    def __init__(self,screen):

        '''
        初始化飞船并设置其初始位置
        '''    
        self.screen = screen
        '''
        加载飞船图像并获取其外接矩形
        '''
        self.image = pygame.image.load(r'D:\Git-Workspace\Py-Practice\Part2\Project_1\Alien\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        '''
        对于每艘新飞船 都将其放在屏幕底部的中央位置
        '''
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    '''
    在指定的位置绘制飞船
    '''
    def blitme(self):
        self.screen.blit(self.image,self.rect)

