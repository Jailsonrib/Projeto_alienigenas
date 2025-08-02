import sys
import pygame
class AlienInvasion:
    '''Classe geral para gerenciar ativos e comportamentos do jogo'''
    def __init__(self):
        '''Inicializa o jogo e cria recursos do jogo'''
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Meu primeiro jogo usando o pygame')
        
    def run_game(self):
        '''inicia o loop principal do jogo'''
        while True:
            #Observa eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    #Deixa a tela desenhada mais recente visível
            pygame.display.flip()
            self.clock.tick(60)
if __name__=="__main__":
    #Cria uma instância do jogo e executa o jogo
    ai = AlienInvasion()
    ai.run_game()