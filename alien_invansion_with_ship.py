import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvansion:
    """class for managing resources and game behavior"""
    def __init__(self):
        """initializes the game and creates game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        
        pygame.display.set_caption("Alien Invansion")
        self.ship = Ship(self)
        
    def run_game(self):
        """Starting the basic game cycle"""
        while True:
            # tracking of keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # at each pass of the cycle, the screen is redrawn
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # display of the last registered screen
            pygame.display.flip()
if __name__ == '__main__':
    # Creating an exemplar and running the game
    ai = AlienInvansion
    ai.run_game()
