import pygame

class GSprite(pygame.sprite.Sprite):
    def __init__(self, spriteList, spriteVelocity, spritePosition = (0, 0)):
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
        # adiciona um tempo a indexImage com relação a velocidade e a váriavel de control de tempo (deltaTime)
        self.indexImage += deltaTime * self.spriteVelocity

        # verifica se a imagem chegou ao fim
        self.indexImage = self.indexImage % self.numSprite

        # coloca no currentImage a imagem atual a ser desenhada
        self.image = self.sprites[int(self.indexImage)]


