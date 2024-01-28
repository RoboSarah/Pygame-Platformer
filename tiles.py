import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__() #WARUUUUM
        self.image = pygame.Surface((size,size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)

# Bewegung der Kamera
    def update(self, x_shift):
        self.rect.x += x_shift