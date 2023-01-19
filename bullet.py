import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для керування снарядами випущених кораблем"""

    def __init__(self, ai_game):
        """Створює обєкт снарядів в нинішній позиції корабля"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet.color

        #Створення снаряда в позиції (0,0) та призначення правильної позиції
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # позиція снаряду зберігається в float форматі
        self.y = float(self.rect.y)

    def update(self):
        """Переміщує снаряд вверх по екрану"""
        self.y -= self.settings.bullet.speed
        # Оновлення позиції прямокутника
        self.rect.y = self.y

    def draw_bullet(self):
        """Вивід снаряду на екран"""
        pygame.draw.rect(self.screen, self.color, self.rect)
