import pygame
import math
import os

import Sprite
import Ninja

# Código desenvolvido por Lucas Campos Achcar para a aula de monitoria em Computação Cientifica em Python

'''
    Free Sprite and SpriteSheet     ->  https://opengameart.org/content/lots-of-free-2d-tiles-and-sprites-by-hyptosis
    Camp Fire						->	https://opengameart.org/content/camp-fire-animation-for-rpgs-finished
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
        # cria a classe superior (construtor superior)
        super().__init__()


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
        self.packetImagePacMan = self.loadImagePacket("./assets/sprite/pacman", "frame", 5, (1.0, 1.0))
        
        # cria os grupos das sprites
        self.groupBird = pygame.sprite.Group()
        self.groupPacMan = pygame.sprite.Group()
        self.genericGroupSprite = pygame.sprite.Group()

        # inicializa uma sprite e coloca no seu devido grupo
        self.groupBird.add(Sprite.GSprite(self.packetImageBird, (1 / self.fps)))
        self.groupBird.add(Sprite.GSprite(self.packetImageBird, (1 / self.fps) * 3, (200, 200)))

        self.pacMan = Sprite.GSprite(self.packetImagePacMan, (1 / self.fps) * 3, (500, 500))
        self.pacMan.setPosition((0, 0))

        self.groupPacMan.add(self.pacMan)

        # carrega nossas spritesheets
        self.campFire = self.loadSpriteSheetPacket('./assets/spritesheet', 'CampFire.png', (64, 64))
        self.ninjaSheet = self.loadSpriteSheetPacket('./assets/spritesheet', 'ninja.png', (50, 77),  (1, 1))

        self.genericGroupSprite.add(Sprite.GSprite(self.campFire, (1 / self.fps) * 0.5, (600, 500)))

        self.playerNinja = Ninja.Ninja(self.ninjaSheet, Ninja.ActionNinja.IDLE_FRONT, (1 / self.fps) * 0.8, (700, 500))

        self.genericGroupSprite.add(self.playerNinja)

    def loadSpriteSheetPacket(self, imagePath, spriteSheetName, dimensionSheet:(int, int), scaleSprite = (1, 1)):
        '''
            Função loadSpriteSheetPacket, cria uma lista de sprites a partir de uma spritesheet
                imagePath       ->  local onde deve ser lido as imagens
                dimensionSprite ->  dimensão da sprite (largura e altura)
                scaleSprite     ->  escala das imagens no eixo x e no eixo y
                Ex: loadSpriteSheetPacket('./assets/spritesheet/CampFire.png', (64, 64), (1, 1))
        '''
        sprites = []

        tempSpriteSheet = pygame.image.load(os.path.join(imagePath, spriteSheetName)).convert_alpha()

        
        for y in range(0, int((tempSpriteSheet.get_height() / dimensionSheet[1]))):
            for x in range(0, int((tempSpriteSheet.get_width() / dimensionSheet[0]))):
                tempImage = pygame.Surface(dimensionSheet)
                tempImage = tempSpriteSheet.subsurface((math.floor(x * dimensionSheet[0]), math.floor(y * dimensionSheet[1]), dimensionSheet[0], dimensionSheet[1]))
                
                sprites.append(tempImage)

                print(f'SpriteSheet - [{spriteSheetName}] - Clip SubSurface [{x * dimensionSheet[0], y * dimensionSheet[1], dimensionSheet[0], dimensionSheet[1]}]')

        return sprites


    def loadImagePacket(self, imagePath, prefixImageName, numSprite, scaleSprite = (1, 1)):
        '''
            Função loadImagePacket, cria uma lista de sprites com imagens com nomes prefix
                imagePath       ->  local onde deve ser lido as imagens
                prefixImageName ->  prefixo da imagem
                numSprite       ->  número de sprites
                scaleSprite     ->  escala da imagem no eixo x e no eixo y
                Ex: loadImagePacket('./assets/sprite/bird', 'frame', 8, (1, 1))
        '''
            
        sprites = []

        # carrega as sprites para o buffer
        for n_sprite in range(0, numSprite):
            tempImageName = prefixImageName + '_' + str(n_sprite) + '.png'
            folderImage = os.path.join(imagePath, tempImageName)
            print(f'Loading Imagem: [{folderImage}]')
            tempImageSurface = pygame.image.load(folderImage).convert_alpha()
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

            self.screen.fill((127, 127, 127))

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

        keys = pygame.key.get_pressed()

        # press M para fazer o personagem dançar
        if(keys[pygame.K_m] and not(self.playerNinja.getHasAnimation())):
            self.playerNinja.setAction(Ninja.ActionNinja.DANCE)

        # JUMP
        if(keys[pygame.K_SPACE]):
            if(self.playerNinja.getLastAction() == Ninja.ActionNinja.WALK_RIGHT or self.playerNinja.getLastAction() == Ninja.ActionNinja.JUMP_RIGHT):
                self.playerNinja.setAction(Ninja.ActionNinja.JUMP_RIGHT)
            elif(self.playerNinja.getLastAction() == Ninja.ActionNinja.WALK_LEFT or self.playerNinja.getLastAction() == Ninja.ActionNinja.JUMP_LEFT):
                self.playerNinja.setAction(Ninja.ActionNinja.JUMP_LEFT)

        # WALK
        if(keys[pygame.K_d]):
            if(self.playerNinja.getCurrentAction() != Ninja.ActionNinja.WALK_RIGHT):
                self.playerNinja.setAction(Ninja.ActionNinja.WALK_RIGHT)
        elif(keys[pygame.K_a]):
            if(self.playerNinja.getCurrentAction() != Ninja.ActionNinja.WALK_LEFT):
                self.playerNinja.setAction(Ninja.ActionNinja.WALK_LEFT)
        # se a tecla não for mais pressionada, para de caminhar
        elif(self.playerNinja.getHasAnimation() and (self.playerNinja.getCurrentAction() == Ninja.ActionNinja.WALK_RIGHT or self.playerNinja.getCurrentAction() == Ninja.ActionNinja.WALK_LEFT)):
            self.playerNinja.setAction(Ninja.ActionNinja.IDLE_FRONT)

        # se não existe nenhuma ação e nenhuma animação, se a ação é diferente do IDLE_FRONT, volta para IDLE_FRONT
        if(not(self.playerNinja.getHasAnimation()) and self.playerNinja.getCurrentAction() != Ninja.ActionNinja.IDLE_FRONT):
            self.playerNinja.setAction(Ninja.ActionNinja.IDLE_FRONT)


        self.groupBird.update(self.deltaTime)
        self.groupPacMan.update(self.deltaTime)
        self.genericGroupSprite.update(self.deltaTime)

    # função de renderização
    def gameRender(self):
        '''
            Função responsável por desenhar na tela do jogo
        '''

        self.groupBird.draw(self.screen)
        self.groupPacMan.draw(self.screen)
        self.genericGroupSprite.draw(self.screen)

game = Game((800, 600), title='Game - Sprite')
game.gameMain()
