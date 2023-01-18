class Settings():
    """class to store all game settings"""
    def __init__(self):
        # screen settings
        self.screen_width = 1024
        self.screen_height = 640
        self.bg_color = (100, 140, 240)#
        # ship settings
        self.ship_speed = 1.5
        # projectile parameters
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 13
        self.bullet_color = (60, 60, 60)

