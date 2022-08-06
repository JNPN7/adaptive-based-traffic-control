import sys, pygame
from road import draw_road
from traffic_light import TrafficLight
from variables import *

from vehicles import *

pygame.init()



speed = [0, 0]

black = 0, 0, 0


screen = pygame.display.set_mode(size)


ball = pygame.image.load("img.jpg")
# ball = 
pygame.draw.rect(screen, pygame.Color(255, 0, 0), (0, 10, 10 , 10))

ballrect = ball.get_rect()

traffic_lights =  [
    TrafficLight(HEIGHT / 2 - ROAD_WIDTH / 2 * 1.4, WIDTH / 2 - ROAD_WIDTH /2 * 1.4, 'L'), 
    TrafficLight(HEIGHT / 2 + ROAD_WIDTH / 2 * 1.4, WIDTH / 2 + ROAD_WIDTH /2 * 1.4, 'R'), 
    TrafficLight(HEIGHT / 2 + ROAD_WIDTH / 2 * 1.4, WIDTH / 2 - ROAD_WIDTH /2 * 1.4, 'T'), 
    TrafficLight(HEIGHT / 2 - ROAD_WIDTH / 2 * 1.4, WIDTH / 2 + ROAD_WIDTH /2 * 1.4, 'B'), 
]

v1 = Vehicle(10, ROAD_WIDTH/6, ROAD_WIDTH/6, Lane.left, Direction.left, Direction.right)
v2 = Vehicle(10, ROAD_WIDTH/6, ROAD_WIDTH/6, Lane.right, Direction.left, Direction.right)
v3 = Vehicle(10, ROAD_WIDTH/6, ROAD_WIDTH/6, Lane.left, Direction.right, Direction.right)
v4 = Vehicle(10, ROAD_WIDTH/6, ROAD_WIDTH/6, Lane.right, Direction.right, Direction.right)
v5 = Vehicle(10, ROAD_WIDTH/6, ROAD_WIDTH/6, Lane.left, Direction.up, Direction.right)
v6 = Vehicle(10, ROAD_WIDTH/6, ROAD_WIDTH/6, Lane.right, Direction.up, Direction.right)
v7 = Vehicle(10, ROAD_WIDTH/6, ROAD_WIDTH/6, Lane.left, Direction.down, Direction.right)
v8 = Vehicle(10, ROAD_WIDTH/6, ROAD_WIDTH/6, Lane.right, Direction.down, Direction.right)


while 1:
    pygame.draw.rect(screen, pygame.Color(255, 0, 0), (0, 10, 10 , 10))

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()


    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > WIDTH:

        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > HEIGHT:

        speed[1] = -speed[1]


    screen.fill('green')

    # screen.blit(ball, ballrect)
    for traffic in traffic_lights:
        traffic.draw(screen)

    draw_road(screen, WIDTH, HEIGHT, ROAD_WIDTH)
    v1.draw(screen)
    v2.draw(screen)
    v3.draw(screen)
    v4.draw(screen)
    v5.draw(screen)
    v6.draw(screen)
    v7.draw(screen)
    v8.draw(screen)
    pygame.display.flip()