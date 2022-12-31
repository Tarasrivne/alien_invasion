import pygame

class Ship:
    """Клас для керування кораблем"""

    def __init__(self, ai_game):
        """Ініціалізує корабель і задає його початкову позицію"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Завантажує зображення корабля та отримує прямокутник
        self.image = pygame.image.load('ship.image/Star_ship2.bmp')
        self.rect = self.image.get_rect()
        '''Start each new ship at the bottom-center of the screen'''
        self.rect.midbottom = self.screen_rect.midbottom
        # saving the real coordinate
        self.x = float(self.rect.x)
        # Флаг переміщення
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """обновляє позицію корабля з урахуванням флага"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # оновлює атрибута rect на основі self.x
        self.rect.x = self.x


    def blitme(self):
        """малює корабель в актуальній позиції"""
        self.screen.blit(self.image, self.rect)