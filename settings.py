
class Settings:
    def __init__(self):
        """Inicializa as configurações do jogo"""
        #Configurações da tela
        self.screen_width = 900
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.ship_speed = 10
        
        #Configurações do projétil
        self.bullet_speed = 15.5
        self.bullet_width = 3
        self.bullet_height = 13
        self.bullet_color = (0,0,0)
        self.bullets_allowed = 3