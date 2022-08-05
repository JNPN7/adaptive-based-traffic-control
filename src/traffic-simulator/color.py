from enum import Enum
import pygame

class Color(Enum):
    black = pygame.Color(0, 0, 0)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)
    white = pygame.Color(255, 255, 255)