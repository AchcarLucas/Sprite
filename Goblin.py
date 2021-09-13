import pygame
from enum import Enum

class ActionGoblin(Enum):
    IDLE_UP         = 0
    IDLE_DOWN       = 1
    IDLE_LEFT       = 2
    IDLE_RIGHT      = 3

    ATTACK_UP       = 4
    ATTACK_DOWN     = 5
    ATTACK_LEFT     = 6
    ATTACK_RIGHT    = 7

    MOVE_UP         = 8
    MOVE_DOWN       = 9
    MOVE_LEFT       = 10
    MOVE_RIGHT      = 11

    DIE             = 12
    HAS_DIED        = 13

class Goblin(pygame.sprite.Sprite):
    '''
        Class de Controle do Goblin
    '''
    def __init__(self, spriteList, actionGoblin : ActionGoblin, spriteVelocity, spritePosition = (0, 0)):
        '''
            Construtor da Classe GSprite, possui como parâmetro
                ActionGoblin    -> define a ação do Goblin definida com o Enum ActionGoblin
                spriteList      ->  lista contendo todas as surfaces (imagens) da sua sprite
                                que corresponde a largura e altura, ex (800, 600)
                spriteVelocity  ->  velocidade em que a sprite irá ser executada
                spritePosition  ->  posição em que a sprite irá ser desenhada, por padrão é (0, 0)
        '''
         # Chama o construtor __init__ da classe superior
        pygame.sprite.Sprite.__init__(self)

        # initializa as váriaveis posição e action da sprite
        self.spritePosition = spritePosition
        self.actionGoblin = actionGoblin

        # range das animações na lista de sprite [inicio da animação, fim da animação, repeat]

        # IDLE
        self.IDLE_DOWN  = (6, 6, True)
        self.IDLE_RIGHT = (self.IDLE_DOWN[0] + 11, self.IDLE_DOWN[1] + 11, True)
        self.IDLE_UP    = (self.IDLE_DOWN[0] + 22, self.IDLE_DOWN[1] + 11, True)
        self.IDLE_LEFT  = (self.IDLE_DOWN[0] + 33, self.IDLE_DOWN[1] + 11, True)

        # ATTACK
        self.ATTACK_DOWN    = (6, 10, False)
        self.ATTACK_RIGHT   = (self.ATTACK_DOWN[0] + 11, self.ATTACK_DOWN[1] + 11, False)
        self.ATTACK_UP      = (self.ATTACK_DOWN[0] + 11, self.ATTACK_DOWN[1] + 11, False)
        self.ATTACK_LEFT    = (self.ATTACK_DOWN[0] + 11, self.ATTACK_DOWN[1] + 11, False)
        

        # MOVE
        self.MOVE_DOWN    = (0, 6, True)
        self.MOVE_RIGHT   = (self.ATTACK_DOWN[0] + 11, self.ATTACK_DOWN[1] + 11, True)
        self.MOVE_UP      = (self.ATTACK_DOWN[0] + 11, self.ATTACK_DOWN[1] + 11, True)
        self.MOVE_LEFT    = (self.ATTACK_DOWN[0] + 11, self.ATTACK_DOWN[1] + 11, True)

        # DIE AND HAS_DIED
        self.DIE = ((4 * 11) + 1, (4 * 11) + 5, True)
        self.HAS_DIED = ((4 * 11) + 5, (4 * 11) + 5, True)

        # quantidade de imagens (sprites)
        self.numSprite = len(spriteList)

        # lista de sprites
        self.sprites = spriteList

        self.currentAction = self.lastAction = self.IDLE_DOWN
        self.setAction(actionGoblin)

        self.rect = self.image.get_rect()
        self.rect.move_ip(self.spritePosition)

        # velocidade da imagem
        self.spriteVelocity = spriteVelocity

    def setAction(self, actionGoblin):
        self.lastAction = self.currentAction
        self.currentAction = actionGoblin

        if(actionGoblin == ActionGoblin.IDLE_DOWN):
            self.currentSequenceImage = self.IDLE_DOWN
        elif(actionGoblin == ActionGoblin.IDLE_LEFT):
            self.currentSequenceImage = self.IDLE_LEFT
        elif(actionGoblin == ActionGoblin.IDLE_RIGHT):
            self.currentSequenceImage = self.IDLE_RIGHT
        elif(actionGoblin == ActionGoblin.IDLE_UP):
            self.currentSequenceImage = self.IDLE_UP

        # inicializa a imagem atual com a primeira imagem da ação selecionada
        self.image = self.sprites[self.currentSequenceImage[0]]
        self.imageIndex = self.currentSequenceImage[0]


    def update(self, deltaTime):
        self.rect.x = self.spritePosition[0]
        self.rect.y = self.spritePosition[1]

        # adiciona um tempo a indexImage com relação a velocidade e a váriavel de control de tempo (deltaTime)
        self.indexImage += deltaTime * self.spriteVelocity

        # verifica se a imagem chegou ao fim
        self.indexImage = self.indexImage % self.numSprite

        # coloca no currentImage a imagem atual a ser desenhada
        self.image = self.sprites[int(self.indexImage)]