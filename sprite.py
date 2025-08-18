import pygame

class Sprite:
    def __init__(self,game_sprite):
        self.screen = game_sprite.screen
        self.screen_rect = game_sprite.screen.get_rect()
        
        
        self.image = pygame.image.load('images\sprite-0042.png') 
        
        self.rect = self.image.get_rect()
        self.rect.center= self.screen_rect.center
    def Intial_game(self):
        self.screen.blit(self.image, self.rect)