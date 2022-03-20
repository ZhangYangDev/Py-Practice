## 项目: 外星人 入侵

from re import A, S
import sys
from webbrowser import get
from settings import Settings
from ship import Ship
import pygame

'''
管理游戏资源和行为的类
'''
class AlienInvasion: 
    '''
    管理游戏资源并创建游戏资源
    '''
    def __init__(self):

        pygame.init()
        
    
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_wight,self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion - 外星人入侵")
        
        self.ship = Ship(self)    

    
    '''
    开始游戏的主体循环
    '''
    def run_game(self):
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # 让最近绘制的屏幕可见
            pygame.display.flip()


'''
游戏的启动入口
'''
if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()        

