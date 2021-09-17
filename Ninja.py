import pygame
import math
from enum import Enum

class ActionNinja(Enum):
    IDLE_FRONT              =   0
    IDLE_RIGHT              =   1
    IDLE_LEFT              =   2

    JUMP_RIGHT              =   3
    JUMP_LEFT               =   4

    DANCE                   =   5

    CLIMB                   =   6

class Ninja(pygame.sprite.Sprite):
    '''
        Class de Controle do Ninja
    '''
    def __init__(self, spriteList, actionNinja : ActionNinja, spriteVelocity, spritePosition = (0, 0)):
        '''
            Construtor da Classe GSprite, possui como parâmetro
                actionNinja     -> define a ação do Ninja definida com o Enum ActionNinja
                spriteList      ->  lista contendo todas as surfaces (imagens) da sua sprite
                                que corresponde a largura e altura, ex (800, 600)
                spriteVelocity  ->  velocidade em que a sprite irá ser executada
                spritePosition  ->  posição em que a sprite irá ser desenhada, por padrão é (0, 0)
        '''
         # Chama o construtor __init__ da classe superior
        pygame.sprite.Sprite.__init__(self)

        # initializa as váriaveis posição e action da sprite
        self.spritePosition = spritePosition
        self.actionNinja = actionNinja

        # range das animações na lista de sprite [inicio da animação, fim da animação, repeat]

        # IDLE
        self.IDLE_FRONT     = (0, 0, False)
        self.IDLE_LEFT      = ((8 * 1), (8 * 1), False)
        self.IDLE_RIGHT     = ((8 * 2), (8 * 2), False)

        # JUMP
        self.JUMP_LEFT = ((8 * 4), (8 * 4) + 3, True)
        self.JUMP_RIGHT = ((8 * 4) + 4, (8 * 4) + 7, True)

        # quantidade de imagens (sprites)
        self.numSprite = len(spriteList)

        # lista de sprites
        self.sprites = spriteList

        self.currentAction = actionNinja
        self.has_action = False

        self.setAction(self.currentAction)

        self.rect = self.image.get_rect()
        self.rect.move_ip(self.spritePosition)

        # velocidade da imagem
        self.spriteVelocity = spriteVelocity

    def setAction(self, actionNinja):
        self.lastAction = self.currentAction
        self.currentAction = actionNinja

        print(f'lastAction [{self.lastAction}] - currentAction [{self.currentAction}]')

        # IDLE
        if(actionNinja == ActionNinja.IDLE_FRONT):
            self.currentSequenceImage = self.IDLE_FRONT
        elif(actionNinja == ActionNinja.IDLE_RIGHT):
            self.currentSequenceImage = self.IDLE_RIGHT
        elif(actionNinja == ActionNinja.IDLE_LEFT):
            self.currentSequenceImage = self.IDLE_LEFT
           
        # JUMP
        if(actionNinja == ActionNinja.JUMP_RIGHT):
            self.currentSequenceImage = self.JUMP_RIGHT
        elif(actionNinja == ActionNinja.JUMP_LEFT):
            self.currentSequenceImage = self.JUMP_LEFT

        # inicializa a imagem atual com a primeira imagem da ação selecionada
        self.image = self.sprites[self.currentSequenceImage[0]]
        self.indexImage = self.currentSequenceImage[0]

        self.hasAnimation = True

    def update(self, deltaTime):
        # verifica se a imagem chegou ao fim e se é uma repetição
        if(self.indexImage >= self.currentSequenceImage[0] and self.indexImage <= self.currentSequenceImage[1] and self.hasAnimation):
            # adiciona ao index uma velocidade (troca de sprite)
            self.indexImage += deltaTime * self.spriteVelocity
        # verifica se é uma repetição, se for, reinicia o indexImage e começa tudo novamente
        elif(self.currentSequenceImage[2]):
            # verifica se a imagem chegou ao fim e reinicia (se for repeat)
            self.indexImage = (self.indexImage % self.currentSequenceImage[1]) + self.currentSequenceImage[0]
            self.hasAnimation = True
        # se não existir mais animação e não for repeat, seta a flag hasAnimation para indicar que não existe mais animação
        else:
            self.hasAnimation = False
            
        # coloca no currentImage a imagem atual a ser desenhada
        self.image = self.sprites[math.floor(self.indexImage)]

    def hasAnimation(self):
        return self.hasAnimation

    def lastAction(self):
        return self.lastAction

    def currentAction(self):
        return self.currentAction