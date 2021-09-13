import pygame

class GSprite(pygame.sprite.Sprite):
    '''
        Classe GSprite Genérica para criar sprites
        Use essa GSprite para sprites que não vão se movimentar (não tenha ação)
        Para usar sprites que contenha ação, crie uma particular para o que deseja
        OBS: Veja a classe GSpriteBat
    '''
    def __init__(self, spriteList, spriteVelocity, spritePosition = (0, 0)):
        '''
            Construtor da Classe GSprite, possui como parâmetro
                spriteList      ->  lista contendo todas as surfaces (imagens) da sua sprite
                                que corresponde a largura e altura, ex (800, 600)
                spriteVelocity  ->  velocidade em que a sprite irá ser executada
                spritePosition  ->  posição em que a sprite irá ser desenhada, por padrão é (0, 0)
        '''
        # Chama o construtor __init__ da classe superior
        pygame.sprite.Sprite.__init__(self)

        # initializa as váriaveis posição da sprite
        self.spritePosition = spritePosition

        # quantidade de imagens (sprites)
        self.numSprite = len(spriteList)

        # lista de sprites
        self.sprites = spriteList

        # initiliza na imagem (sprite) 0
        self.indexImage = 0.0

        # inicializa a imagem atual com a primeira imagem e a seleciona
        self.image = self.sprites[int(self.indexImage)]

        self.rect = self.image.get_rect()
        self.rect.move_ip(self.spritePosition)

        # velocidade da imagem
        self.spriteVelocity = spriteVelocity

    def update(self, deltaTime):
        self.rect.x = self.spritePosition[0]
        self.rect.y = self.spritePosition[1]

        # adiciona um tempo a indexImage com relação a velocidade e a váriavel de control de tempo (deltaTime)
        self.indexImage += deltaTime * self.spriteVelocity

        # verifica se a imagem chegou ao fim
        self.indexImage = self.indexImage % self.numSprite

        # coloca no currentImage a imagem atual a ser desenhada
        self.image = self.sprites[int(self.indexImage)]

    def getPosition(self):
        return self.spritePosition

    def setPosition(self, newPos):
        self.spritePosition = newPos



