import pygame
from color import Color

def draw_road(screen, length, breadth):
    lc, bc = length/2, breadth/2
    road_width = 120

    pygame.draw.rect(screen, Color.black.value, (0, lc-road_width/2, breadth, road_width))
    pygame.draw.rect(screen, Color.black.value, (bc-road_width/2, 0, road_width, length))