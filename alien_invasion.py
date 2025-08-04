import sys
import pygame
from settings import Settings
class AlienInvasion:
    '''Classe geral para gerenciar ativos e comportamentos do jogo'''
    def __init__(self):
        '''Inicializa o jogo e cria recursos do jogo'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Meu primeiro jogo usando o pygame')
        #Define a cor do background
        self.bg_color = (230, 230, 230)
    def run_game(self):
        '''inicia o loop principal do jogo'''
        while True:
            #Observa eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    #Deixa a tela desenhada mais recente visível
            pygame.display.flip()
            #Redesenha a tela durante cada passagem pelo loop
            self.screen.fill(self.settings.bg_color)
            self.clock.tick(60)
if __name__=="__main__":
    #Cria uma instância do jogo e executa o jogo
    ai = AlienInvasion()
    ai.run_game()