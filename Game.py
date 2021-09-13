import pygame
import os

import Sprite

# Código desenvolvido por Lucas Campos Achcar para a aula de monitoria em Computação Cientifica em Python

'''
    Free Sprite and SpriteSheet     ->  https://opengameart.org/content/lots-of-free-2d-tiles-and-sprites-by-hyptosis
    Bird (Sprite)                   ->  https://opengameart.org/content/fat-bird-sprite-sheets-for-gamedev
    Bat (SpriteSheet)               ->  https://opengameart.org/content/bat-sprite
    Goblin (SpriteeSheet)           ->  https://opengameart.org/content/lpc-goblin
'''

class Game():
    '''
        Classe responsável por gerenciar o jogo
    '''
    def __init__(self, screenSize : (int, int), fps=60, title='Game', icon=None):
        '''
            Construtor da Classe Game, possui como parâmetro
                screenSize  ->  tupla contendo de dois valores inteiros (int, int) 
                                que corresponde a largura e altura, ex (800, 600)
                fps         ->  contendo da taxa de atualização da tela
                title       ->  contendo o titulo do jogo
                icon        ->  contendo uma surface (imagem) com o icone a ser exibido na tela
        '''
        # inicializa as variáveis da classe
        self.gameRunning = True
        self.screenSize = screenSize

        self.title = title
        self.icon = icon
        self.fps = fps

        # inicializa o game
        self.initGame()
        
        # carrega o pacote de imagem (conjunto que define a sprite)
        self.packetImageBird = self.loadImagePacket("./assets/sprite/bird", "frame", 8, (0.3, 0.3))
        self.packetImageBall = self.loadImagePacket("./assets/sprite/ball", "frame", 12, (1.0, 1.0))
        
        # cria os grupos das sprites
        self.groupBird = pygame.sprite.Group()
        self.groupBall = pygame.sprite.Group()

        # inicializa uma sprite e coloca no seu devido grupo
        self.groupBird.add(Sprite.GSprite(self.packetImageBird, (1 / self.fps)))
        self.groupBird.add(Sprite.GSprite(self.packetImageBird, (1 / self.fps) * 3, (200, 200)))

        self.groupBall.add(Sprite.)

    def loadImagePacket(self, imagePath, prefixImageName, numSprite, scaleSprite = (1, 1)):
        '''
            Função loadImagePack, cria uma lista de sprites com imagens com nomes prefix
                imagePath       ->  local onde deve ser lido as imagens
                prefixImageName ->  prefixo da imagem
                numSprite       ->  número de sprites
                scaleSprite     ->  escala da imagem no eixo x e no eixo y
                Ex: loadSprite('./assets/sprite/bird', 'frame', 8, (1, 1))
        '''
            
        sprites = []

        # carrega as sprites para o buffer
        for n_sprite in range(0, numSprite):
            tempImageName = prefixImageName + '_' + str(n_sprite) + '.png'
            folderImage = os.path.join(imagePath, tempImageName)
            print(f'Loading Imagem: [{folderImage}]')
            tempImageSurface = pygame.image.load(folderImage).convert()
            sprites.append(pygame.transform.scale(tempImageSurface, (int(tempImageSurface.get_width() * scaleSprite[0]), int(tempImageSurface.get_height() * scaleSprite[1]))))
        
        return sprites

    def initGame(self):
        '''
            Função responsável por inicializar e configurar a tela do jogo,
            essa função não possui parâmetros
        '''
        self.screen = pygame.display.set_mode(self.screenSize)
        pygame.display.set_caption(self.title)

        if(self.icon != None):
            pygame.display.set_icon(self.icon)

        self.gameClock = pygame.time.Clock()

    # função principal do jogo
    def gameMain(self):
        '''
            Loop principal do jogo, essa função não possui parâmetros
        '''
        while self.gameRunning:
            self.deltaTime = self.gameClock.tick(self.fps)

            for event in pygame.event.get():
                self.gameEvent(event)

            self.gameUpdate()
            self.gameRender()

            pygame.display.update()

        pygame.quit()
        
    # função de eventos
    def gameEvent(self, event):
        '''
            Função responsável por gerenciar os eventos do display
            event -> contém a estrutura do evento (veja a documentação do pygame para mais detalhes)
        '''
        if(event.type == pygame.QUIT):
            self.gameRunning = False
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_ESCAPE):
                self.gameRunning = False

    # função de atualização
    def gameUpdate(self):
        '''
            Função responsável por atualizar a lógica do jogo
        '''
        self.groupBird.update(self.deltaTime)

    # função de renderização
    def gameRender(self):
        '''
            Função responsável por desenhar na tela do jogo
        '''

        self.groupBird.draw(self.screen)

game = Game((800, 600), title='Game - Sprite')
game.gameMain()
