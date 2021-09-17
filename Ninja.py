import pygame
import math
from enum import Enum

class ActionNinja(Enum):
    IDLE_FRONT              =   0
    IDLE_RIGHT              =   1
    IDLE_LEFT               =   2
    IDLE_CLIMB              =   3

    JUMP_RIGHT              =   4
    JUMP_LEFT               =   5

    ATTACK_RIGHT            =   6
    ATTACK_LEFT             =   7

    CLIMB                   =   8

    DANCE                   =   9

    WALK_RIGHT              =   10
    WALK_LEFT               =   11


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

        # velocidade da imagem
        self.spriteVelocity = spriteVelocity

        # range das animações na lista de sprite [inicio da animação, fim da animação, repeat, velocity]

        # IDLE
        self.IDLE_FRONT     = (0, 0, False, 0)
        self.IDLE_LEFT      = ((8 * 1), (8 * 1), False, 0)
        self.IDLE_RIGHT     = ((8 * 2), (8 * 2), False, 0)
        self.IDLE_CLIMB     = (7, 7, False, 0)

        # JUMP
        self.JUMP_LEFT = ((8 * 4), (8 * 4) + 3, False, self.spriteVelocity * 0.8)
        self.JUMP_RIGHT = ((8 * 4) + 4, (8 * 4) + 7, False, self.spriteVelocity * 0.8)

        # ATTACK
        self.ATTACK_RIGHT = ((8 * 3), (8 * 3) + 3, False, self.spriteVelocity * 1.0)
        self.ATTACK_LEFT = ((8 * 3) + 4, (8 * 3) + 7, False, self.spriteVelocity * 1.0)

        # CLIMB
        self.CLIMB = (4, 7, False, self.spriteVelocity * 0.5)

        # DANCE
        self.DANCE = ((8 * 3), (8 * 3) + 7, False, self.spriteVelocity * 0.5)

        # WALK
        self.WALK_RIGHT = ((8 * 2), (8 * 2) + 7, True, self.spriteVelocity * 0.6)
        self.WALK_LEFT = ((8 * 1), (8 * 1) + 7, True, self.spriteVelocity * 0.6)

        # quantidade de imagens (sprites)
        self.numSprite = len(spriteList)

        # lista de sprites
        self.sprites = spriteList

        self.currentAction = actionNinja
        self.setAction(self.currentAction)

        self.rect = self.image.get_rect()
        self.rect.move_ip(self.spritePosition)

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
        elif(actionNinja == ActionNinja.IDLE_CLIMB):
            self.currentSequenceImage = self.IDLE_CLIMB
           
        # JUMP
        if(actionNinja == ActionNinja.JUMP_RIGHT):
            self.currentSequenceImage = self.JUMP_RIGHT
        elif(actionNinja == ActionNinja.JUMP_LEFT):
            self.currentSequenceImage = self.JUMP_LEFT

        # ATTACK
        if(actionNinja == ActionNinja.ATTACK_LEFT):
            self.currentSequenceImage = self.ATTACK_LEFT
        elif(actionNinja == ActionNinja.ATTACK_RIGHT):
            self.currentSequenceImage = self.ATTACK_RIGHT

        # CLIMB
        if(actionNinja == ActionNinja.CLIMB):
            self.currentSequenceImage = self.CLIMB

        # DANCE
        if(actionNinja == ActionNinja.DANCE):
            self.currentSequenceImage = self.DANCE

        # WALK
        if(actionNinja == ActionNinja.WALK_RIGHT):
            self.currentSequenceImage = self.WALK_RIGHT
        elif(actionNinja == ActionNinja.WALK_LEFT):
            self.currentSequenceImage = self.WALK_LEFT

        # inicializa a imagem atual com a primeira imagem da ação selecionada
        self.image = self.sprites[self.currentSequenceImage[0]]
        self.indexImage = self.currentSequenceImage[0]
        self.spriteVelocity = self.currentSequenceImage[3]

        self.hasAnimation = False

        # verifica se é uma animação, se sim, seta hasAnimation
        if(self.currentSequenceImage[0] != self.currentSequenceImage[1]):
            self.hasAnimation = True

    def update(self, deltaTime):
        # verifica se a imagem chegou ao fim e se é uma repetição
        if(self.indexImage >= self.currentSequenceImage[0] and self.indexImage <= self.currentSequenceImage[1] and self.hasAnimation):
            # adiciona ao index uma velocidade (troca de sprite)
            self.indexImage += deltaTime * self.spriteVelocity
        # verifica se é uma repetição, se for, reinicia o indexImage e começa tudo novamente
        elif(self.currentSequenceImage[2] and self.hasAnimation):
            # verifica se a imagem chegou ao fim e reinicia (se for repeat)
            self.indexImage = (self.indexImage % self.currentSequenceImage[1]) + self.currentSequenceImage[0]
            self.hasAnimation = True
        # se não existir mais animação e não for repeat, seta a flag hasAnimation para indicar que não existe mais animação
        else:
            self.hasAnimation = False
            
        # coloca no currentImage a imagem atual a ser desenhada
        self.image = self.sprites[math.floor(self.indexImage)]

    def getHasAnimation(self):
        return self.hasAnimation

    def getLastAction(self):
        return self.lastAction

    def getCurrentAction(self):
        return self.currentAction
