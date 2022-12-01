import sys

import pygame

class AlienInvansion:
    """class for managing resources and game behavior"""
    def __init__(self):
        """initializes the game and creates game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invansion")

    def run_game(self):
        """Starting the basic game cycle"""
        while True:
            # tracking of keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # display of the last registered screen
            pygame.display.flip()
if __name__ == '__main__':
    # Creating an instance and running the game
    ai = AlienInvansion
    ai.run_game()