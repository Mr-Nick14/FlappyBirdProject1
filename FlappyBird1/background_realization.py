import pygame
from constants import *

class BackGround(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        bg_image = pygame.image.load('graphics/background.png').convert()

        self.image = pygame.transform.scale(bg_image ,(constWindowWidth * constWindowWidthMultiplier ,constWindowHeight * constWindowHeightMultiplier))
        self.rect = self.image.get_rect(topleft = (0 ,0))
        self.pos = pygame.math.Vector2(self.rect.topleft)