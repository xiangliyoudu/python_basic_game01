import pygame

from pygame.sprite import Group
# 导入设置类
import basicsettings as bs
# import ship
import ship as sp
# import gf
import game_functions as gf

#import dog as dg


def run_game():
    # 初始化pygame所有模块
    pygame.init()
    # 构建窗口，大小为 800 * 600
    #screen = pygame.display.set_mode((800, 600))
    # 设置窗口名称未alien_invasion
    #pygame.display.set_caption('alien_invasion')
    # 背景设置为一种浅灰色。
    #bc_color = (230, 230, 230)

    # 实例化Settings类
    ai_settings = bs.Settings()

    # 构建窗口，大小为 800 * 600
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    # 设置窗口名称未alien_invasion
    pygame.display.set_caption('alien_invasion')

    #  创建一艘飞船
    ship = sp.Ship(ai_settings, screen)
    # dog = dg.Dog(screen)
    bullets = Group()


    # 开始游戏循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # 执行循环时都调用飞船的方法 update
        ship.update()
        # 执行循环时都调用bullet的方法 update_bullets
        gf.update_bullets(bullets)
        # 更新屏幕状态
        # gf.update_screen(ai_settings, screen, ship, dog)
        gf.update_screen(ai_settings, screen, ship, bullets)





if __name__ == '__main__':
    run_game()

