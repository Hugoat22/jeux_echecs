from pion import Pion
import pygame
from random import randint


class Partie:
    def __init__(self, info_pion):
        self.info = info_pion
        self.groupe_pion = pygame.sprite.Group()
        self.ApparitionPion(self.info)

    def ApparitionPion(self, info):
        for i in range(32):
            print(info[i])
            #pion = Pion(i,info[i])
        self.groupe_carte.add(pion)
