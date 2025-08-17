import sys
import pygame
from settings import Settings
from ship import Ship
from sprite import Sprite
class AlienInvasion:
    '''Classe geral para gerenciar ativos e comportamentos do jogo'''
    def __init__(self):
        '''Inicializa o jogo e cria recursos do jogo'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Meu primeiro jogo usando o pygame')
        self.ship = Ship(self)
        '''self.sprite = Sprite(self)''' #objeto da classe sprite 
        #Define a cor do background
        # self.bg_color = (230, 230, 230)
    def run_game(self):
        '''inicia o loop principal do jogo'''
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self.clock.tick(120)
    def _check_events(self):
            #Observa eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    #Captura eventos das teclas de seta
                elif event.type == pygame.KEYDOWN:
                    #Chama o metodo auxiliar que controla teclas pressionadas
                    self._check_keydown(event)
                elif event.type == pygame.KEYUP:
                    #Chama o metodo auxiliar que controla teclas soltas
                    self._check_keyup(event)
                     
    def _check_keydown(self, event):
            '''Responde a teclas pressionadas'''   
            if event.key == pygame.K_RIGHT:
                self.ship.moving_rigth = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            #Responde a teclas (cima/baixo) pressionadas  
            elif event.key == pygame.K_UP:
                self.ship.moving_top = True
            elif event.key == pygame.K_DOWN:
                self.ship.moving_botton = True
            #Encerra o jogo se o usuário precionar a tecla 'q'
            elif event.key ==pygame.K_ESCAPE:
                sys.exit()              
    def _check_keyup(self, event):
            '''Responde a teclas soltas'''          
            if event.key == pygame.K_RIGHT:
                self.ship.moving_rigth = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False
            #Responde a teclas (cima/baixo) soltas    
            elif event.key == pygame.K_UP:
                self.ship.moving_top = False
            elif event.key == pygame.K_DOWN:
                self.ship.moving_botton = False
                   
    def _update_screen(self):      
            #Atualiza as imagens na tela e muda para a nova tela
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            '''self.sprite.Intial_game()'''
            #Deixa a tela desenhada mais recente visível
            pygame.display.flip()
           
if __name__=="__main__":
    #Cria uma instância do jogo e executa o jogo
    ai = AlienInvasion()
    ai.run_game()