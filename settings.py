
class Settings:
    def __init__(self):
        """Inicializa as configurações do jogo"""
        #Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 10
        
        #Configurações do projétil
        self.bullet_speed = 15.5
        self.bullet_width = 300
        self.bullet_height = 13
        self.bullet_color = (0,0,0)
        self.bullets_allowed = 6
        
        
        
    #Configurações do alienigena
        self.alien_speed = 2
        self.fleet_drop_speed = 10
        #Direção da frota: 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1