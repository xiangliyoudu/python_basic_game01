import pygame

class Dog():

    def __init__(self, screen):
        self.screen = screen

        _image = pygame.image.load('../images/dog.jpg')
        # 缩放图片
        self.image = pygame.transform.scale(_image, (80, 60))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #  将dog放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        ''' 在指定位置绘制dog'''
        self.screen.blit(self.image, self.rect)