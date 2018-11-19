import pygame
import sys

from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        # 事件类型
        _keytype = event.type
        # 鼠标关闭窗口，游戏退出
        if _keytype == pygame.QUIT:
            sys.exit()
        # 按键按下事件
        elif _keytype == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # 按键抬起事件
        elif _keytype == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # 按键事件对应的键的int值
    _key = event.key
    # 右移动
    if _key == pygame.K_RIGHT:
        ship.moving_right = True
    # 左移动
    elif _key == pygame.K_LEFT:
        ship.moving_left = True

    elif _key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    _key = event.key
    # 右移动停止
    if _key == pygame.K_RIGHT:
        ship.moving_right = False
    # 左移动停止
    elif _key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings, screen, ship, bullets):
    # 用背景色填充屏幕
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    #dog.blitme()
    # 显示窗口
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()

    #  删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    #  创建新子弹并将其加入到编组 bullets 中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)