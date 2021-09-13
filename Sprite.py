import pygame
import os

class SpriteBird(pygame.sprite.Sprite):
    def __init__(self, imagePath, imageName, numSprite, spriteSize:(int, int), spritePosition:(0, 0)):
        # Chama o construtor __init__ da classe superior
        super().__init__(self)

        # initializa as váriaveis posição e tamanho da sprite
        self.spriteSize = spriteSize
        self.spritePosition = spritePosition

        # quantidade de imagens (sprites)
        self.numSprite = numSprite

        # lista de sprites
        self.sprites = []

        # carrega as sprites para o buffer
        for n_sprite in range(0, numSprite):
            tempImageName += imageName + "_" + n_sprite
            self.sprites.append(pygame.image.load(os.path.join(imagePath, tempImageName)).convert())

        # inicializa a imagem atual com a primeira imagem e a seleciona
        self.indexImage = 0.0
        self.currentImage = self.sprites[int(self.indexImage)]

        # velocidade da imagem
        self.imageVelocity = 0.1

    def update(self, deltaTime):
        # adiciona um tempo a indexImage com relação a velocidade e a váriavel de control de tempo (deltaTime)
        self.indexImage += deltaTime * self.imageVelocity

        # verifica se a imagem chegou ao fim
        if(self.indexImage > numSprite):
            self.indexImage = 0

        # coloca no currentImage a imagem atual a ser desenhada
        self.currentImage = self.sprites[int(self.indexImage)]

    def draw(self, screen):
        # desenha a imagem atual do sprite
        screen.blit(self.currentImage, self.spritePosition)
        
        pass


