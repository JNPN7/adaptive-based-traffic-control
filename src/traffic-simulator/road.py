import pygame
from color import Color

def draw_road(screen, length, breadth):
    lc, bc = length/2, breadth/2
    road_width = 120
    zebra_crossing_dist = road_width/2*1.2
    zebra_crossing = {
        "left": ((lc - zebra_crossing_dist, bc - road_width/2), (lc - zebra_crossing_dist, bc+ road_width/2)),
        "right": ((lc + zebra_crossing_dist, bc - road_width/2), (lc + zebra_crossing_dist, bc+ road_width/2)),
        "top": ((lc - road_width/2, bc - zebra_crossing_dist), (lc + road_width/2, bc - zebra_crossing_dist)),
        "bottom": ((lc - road_width/2, bc + zebra_crossing_dist), (lc + road_width/2, bc + zebra_crossing_dist)),
    }


    pygame.draw.rect(screen, 'grey', (0, lc-road_width/2 - 5, breadth, road_width + 10))
    pygame.draw.rect(screen, 'grey', (bc-road_width/2 -5, 0, road_width + 10, length))
    pygame.draw.rect(screen, 'black', (0, lc-road_width/2, breadth, road_width))
    pygame.draw.rect(screen, 'black', (bc-road_width/2, 0, road_width, length))

    # pygame.draw.rect(screen, 'yellow', pygame.Rect(lc - road_width/2 - 20 , bc - road_width/2 - 20, road_width + 40, road_width + 40), 5)

    pygame.draw.line(screen, 'yellow', zebra_crossing["left"][0], zebra_crossing["left"][1], 5)
    pygame.draw.line(screen, 'yellow', zebra_crossing["right"][0], zebra_crossing["right"][1], 5)
    pygame.draw.line(screen, 'yellow', zebra_crossing["top"][0], zebra_crossing["top"][1], 5)
    pygame.draw.line(screen, 'yellow', zebra_crossing["bottom"][0], zebra_crossing["bottom"][1], 5)