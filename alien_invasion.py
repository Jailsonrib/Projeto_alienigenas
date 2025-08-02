import sys
import pygame
class AlienInvasion:
    '''Classe geral para gerenciar ativos e comportamentos do jogo'''
    def __init__(self):
        '''Inicializa o jogo e cria recursos do jogo'''
        pygame.init()
        self.screen = pygame.display.set_mode(1200, 800)
        pygame.display.set_caption('Alien Invasion')
        
    def run_game(self):
        '''inicia o loop principal do jogo'''
        while True:
            #Observa eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
        