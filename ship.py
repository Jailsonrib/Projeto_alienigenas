import pygame

class Ship:
    """Classe para cuidar da espaçonave"""
    def __init__(self, ai_game):
        """inicializa a espaçonave e define sua posição atual"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #Sobe a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images\ship.bmp') # 'rect' significa retângulo 
        
        self.rect = self.image.get_rect()
        
        # Começa cada espaçonave nova no centro inferior da tela
        self.rect.center = self.screen_rect.center
        #Armazena um float para a posição horizontal exata da espaçonave
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #Flag de movimento; começa com uma espaçonave que não está se movendo
        self.moving_rigth = False
        self.moving_left = False
        self.moving_top = False
        self.moving_botton = False
        
        
    def update(self):
        """Atualiza a posição da nave com base na flag de movimento"""
        if self.moving_rigth and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed 
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
            
        #Responsável por controlar a nave quanto bate na borda top  
        if self.moving_top and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        #Responsável por controlar a nave quanto bate na borda bottom
        if self.moving_botton and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed 
        #Atualiza o objeto rect de self.x
        self.rect.x = self.x
        #Atualiza o objeto rect de self.y
        self.rect.y = self.y
    def blitme(self):
        """Desenha a espaçonave em sua localização atual"""
        self.screen.blit(self.image, self.rect)
        
    