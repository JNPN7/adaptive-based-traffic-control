import sys, pygame
from road import draw_road
from traffic_light import TrafficLight
import threading
from vehicles import *

pygame.init()


size = WIDTH, HEIGHT = 700, 700
ROAD_WIDTH = 150

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

v1 = Vehicle(1, ROAD_WIDTH/6, ROAD_WIDTH/6, Lane.left, Direction.left, Direction.right)
v2 = Vehicle(1, ROAD_WIDTH/6, ROAD_WIDTH/6, Lane.right, Direction.left, Direction.right)
v3 = Vehicle(1, ROAD_WIDTH/6, ROAD_WIDTH/6, Lane.left, Direction.right, Direction.right)
v4 = Vehicle(1, ROAD_WIDTH/6, ROAD_WIDTH/6, Lane.right, Direction.right, Direction.right)
v5 = Vehicle(1, ROAD_WIDTH/6, ROAD_WIDTH/6, Lane.left, Direction.up, Direction.right)
v6 = Vehicle(1, ROAD_WIDTH/6, ROAD_WIDTH/6, Lane.right, Direction.up, Direction.right)
v7 = Vehicle(1, ROAD_WIDTH/6, ROAD_WIDTH/6, Lane.left, Direction.down, Direction.right)
v8 = Vehicle(1, ROAD_WIDTH/6, ROAD_WIDTH/6, Lane.right, Direction.down, Direction.right)

def initialize_lights():
    while True:
        for traffic in traffic_lights:
            traffic.chageLights()

traffic_light_thread = threading.Thread(name="initialization", target=initialize_lights, args=())
traffic_light_thread.daemon = True
traffic_light_thread.start()

while 1:
    pygame.draw.rect(screen, pygame.Color(255, 0, 0), (0, 10, 10 , 10))

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()



    screen.fill('brown')

    for traffic in traffic_lights:
        traffic.draw(screen)
    # print(f'left light status: {traffic_lights[0].get_status()}')
    # print(f'right light status: {traffic_lights[1].get_status()}')
    # print(f'top light status: {traffic_lights[2].get_status()}')
    # print(f'bottom light status: {traffic_lights[3].get_status()}')

    draw_road(screen, WIDTH, HEIGHT, ROAD_WIDTH)
    v1.draw(screen)
    v2.draw(screen)
    v3.draw(screen)
    v4.draw(screen)
    v5.draw(screen)
    v6.draw(screen)
    v7.draw(screen)
    v8.draw(screen)

    v1.move()
    v2.move()
    v3.move()
    v4.move()
    v5.move()
    v6.move()
    v7.move()
    v8.move()
    pygame.display.flip()