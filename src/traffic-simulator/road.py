import pygame
from draw_dashed import *

def draw_road(screen, width, height, road_width):
    wc, hc = width/2, height/2
    zebra_crossing_dist = road_width/2*1.2
    zebra_crossing = {
        "left": ((wc - zebra_crossing_dist, hc - road_width/2), (wc - zebra_crossing_dist, hc+ road_width/2)),
        "right": ((wc + zebra_crossing_dist, hc - road_width/2), (wc + zebra_crossing_dist, hc+ road_width/2)),
        "top": ((wc - road_width/2, hc - zebra_crossing_dist), (wc + road_width/2, hc - zebra_crossing_dist)),
        "bottom": ((wc - road_width/2, hc + zebra_crossing_dist), (wc + road_width/2, hc + zebra_crossing_dist)),
    }


    pygame.draw.rect(screen, 'grey', (0, wc-road_width/2 - 5, height, road_width + 10))
    pygame.draw.rect(screen, 'grey', (hc-road_width/2 -5, 0, road_width + 10, width))
    pygame.draw.rect(screen, 'black', (0, wc-road_width/2, height, road_width))
    pygame.draw.rect(screen, 'black', (hc-road_width/2, 0, road_width, width))

    # median strip
    dashed_rect(screen, 'yellow', (0,hc,wc-zebra_crossing_dist,hc),width=3,dash_length=20)
    dashed_rect(screen, 'yellow', (wc+zebra_crossing_dist,hc,width,hc),width=3,dash_length=20)
    dashed_rect(screen, 'yellow', (wc,0,wc,hc-zebra_crossing_dist),width=3,dash_length=20)
    dashed_rect(screen, 'yellow', (wc,hc+zebra_crossing_dist,wc,height),width=3,dash_length=20)



    # pygame.draw.rect(screen, 'yellow', pygame.Rect(wc - road_width/2 - 20 , hc - road_width/2 - 20, road_width + 40, road_width + 40), 5)

    # zebra crossing line
    # pygame.draw.line(screen, 'white', zebra_crossing["left"][0], zebra_crossing["left"][1], 5)
    # pygame.draw.line(screen, 'white', zebra_crossing["right"][0], zebra_crossing["right"][1], 5)
    # pygame.draw.line(screen, 'white', zebra_crossing["top"][0], zebra_crossing["top"][1], 5)
    # pygame.draw.line(screen, 'white', zebra_crossing["bottom"][0], zebra_crossing["bottom"][1], 5)

    # zebra crossing
    dashed_zebra_line(screen, 'white', zebra_crossing["left"][0],zebra_crossing["left"][1],width=10,dash_length=1)
    dashed_zebra_line(screen, 'white', zebra_crossing["right"][0],zebra_crossing["right"][1],width=10,dash_length=1)
    dashed_zebra_line(screen, 'white', zebra_crossing["top"][0],zebra_crossing["top"][1],width=10,dash_length=1)
    dashed_zebra_line(screen, 'white', zebra_crossing["bottom"][0],zebra_crossing["bottom"][1],width=10,dash_length=1)
