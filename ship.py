import pygame

class Ship():
        """Клас для керування кораблем"""
    def __init__(self, ai_game):
        """Ініціалізує корабель і задає його початкову позицію"""
        self.screen = ai_game.scren
        self.screen_rect = ai_game.scren.get_rect()

        #Завантажує зображення корабля та отримує прямокутник
        self.imege = pygame.image.load()
        self.rect = self.imege.get_rect()
        #Кожен нижній корабель зявляється у нижньому краї екрану
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """малює корабель в актуальній позиції"""
        self.screen.blit(self.image, self.rect)
