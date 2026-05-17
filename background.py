import pygame

class Background:
    def __init__(self, ai_game):
        """Initialize background"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        self.bg_image = pygame.image.load("assets/bg.png")
        self.y = -1824 / 2
    
    def update(self):
        self.y += 1
        if self.y > 0:
            self.y = -1824 / 2
    
    def draw(self):
        self.screen.fill([0, 0, 0])
        self.screen.blit(self.bg_image,(0,self.y))