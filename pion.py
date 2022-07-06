import pygame.sprite

class Pion(pygame.sprite.Sprite):

    def __init__(self, ID, TYPE, COLOR, IMAGE, POSITION):
        self.__init__()
        self.id = ID
        self.type = TYPE
        self.color = COLOR
        self.image = pygame.image.load(IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = POSITION[0]
        self.rect.x = POSITION[1]
        self.mort = False

