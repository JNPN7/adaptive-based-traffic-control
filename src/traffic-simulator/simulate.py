from filecmp import dircmp
import sys, pygame
from xml.etree.ElementPath import find
from road import draw_road
from traffic_light import TrafficLight
import random
import threading
from vehicles import *
from variables import *
from time import sleep

pygame.init()

speed = [0, 0]

black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("img.jpg")
# ball =
pygame.draw.rect(screen, pygame.Color(255, 0, 0), (0, 10, 10, 10))

ballrect = ball.get_rect()

traffic_lights = [
    TrafficLight(HEIGHT / 2 - ROAD_WIDTH / 2 * 1.4,
                 WIDTH / 2 - ROAD_WIDTH / 2 * 1.4, 'L'),
    TrafficLight(HEIGHT / 2 + ROAD_WIDTH / 2 * 1.4,
                 WIDTH / 2 + ROAD_WIDTH / 2 * 1.4, 'R'),
    TrafficLight(HEIGHT / 2 + ROAD_WIDTH / 2 * 1.4,
                 WIDTH / 2 - ROAD_WIDTH / 2 * 1.4, 'T'),
    TrafficLight(HEIGHT / 2 - ROAD_WIDTH / 2 * 1.4,
                 WIDTH / 2 + ROAD_WIDTH / 2 * 1.4, 'B'),
]

# v1 = Vehicle(0.1, ROAD_WIDTH / 6, ROAD_WIDTH / 6, Lane.left, Direction.left, 
#              Direction.left)
# v2 = Vehicle(0.1, ROAD_WIDTH / 6, ROAD_WIDTH / 6, Lane.right, Direction.left,
#              Direction.right)
# v3 = Vehicle(0.1, ROAD_WIDTH / 6, ROAD_WIDTH / 6, Lane.left, Direction.right,
#              Direction.right)
# v4 = Vehicle(0.1, ROAD_WIDTH / 6, ROAD_WIDTH / 6, Lane.right, Direction.right,
#              Direction.up)
# v5 = Vehicle(0.1, ROAD_WIDTH / 6, ROAD_WIDTH / 6, Lane.left, Direction.up,
#              Direction.up)
# v6 = Vehicle(0.1, ROAD_WIDTH / 6, ROAD_WIDTH / 6, Lane.right, Direction.up,
#              Direction.down)
# v7 = Vehicle(0.1, ROAD_WIDTH / 6, ROAD_WIDTH / 6, Lane.left, Direction.down,
#              Direction.down)
# v8 = Vehicle(0.1, ROAD_WIDTH / 6, ROAD_WIDTH / 6, Lane.right, Direction.down,
#              Direction.right)
vehicles = []
vehicles_dict = {
    Direction.left: {
        # Direction.right: [],
        # Direction.up: [],
        # Direction.down: []
        Lane.left: [],
        Lane.right: []
    },
    Direction.right: {
        # Direction.left: [],
        # Direction.up: [],
        # Direction.down: []
        Lane.left: [],
        Lane.right: []
    },
    Direction.up: {
        # Direction.left: [],
        # Direction.right: [],
        # Direction.down: []
        Lane.left: [],
        Lane.right: []
    },
    Direction.down: {
        # Direction.left: [],
        # Direction.right: [],
        # Direction.up: []
        Lane.left: [],
        Lane.right: []
    }
}

def find_associate_light(vehicle):
    if vehicle.direction == Direction.left:
        return traffic_lights[0]
    elif vehicle.direction == Direction.right:
        return traffic_lights[1]
    elif vehicle.direction == Direction.up:
        return traffic_lights[2]
    return traffic_lights[3]

def generate_vehicle():
    while True: 
        lane = Lane(random.randint(1, 2))
        direction = Direction(random.randint(1, 4))
        lst = list(range(1, 5))
        del lst[direction.value - 1]
        dest_direciton = Direction(random.choice(lst))
        vehicle = Vehicle(0.2, ROAD_WIDTH / 6, ROAD_WIDTH / 6, lane, direction, dest_direciton)
        vehicles.append(vehicle)
        vehicles_dict[direction][lane].append(vehicle)
        # print(vehicles_dict)
        sleep(1)

def initialize_lights():
    while True:
        for traffic in traffic_lights:
            traffic.chageLights()

traffic_light_thread = threading.Thread(name="initialization", target=initialize_lights, args=())
traffic_light_thread.daemon = True
traffic_light_thread.start()

generate_vehicle_thread = threading.Thread(name="Initialization", target=generate_vehicle, args=())
generate_vehicle_thread.daemon = True
generate_vehicle_thread.start()


while 1:
    pygame.draw.rect(screen, pygame.Color(255, 0, 0), (0, 10, 10, 10))

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()

    # ballrect = ballrect.move(speed)


    screen.fill('brown')

    for traffic in traffic_lights:
        traffic.draw(screen)
    # print(f'left light status: {traffic_lights[0].get_status()}')
    # print(f'right light status: {traffic_lights[1].get_status()}')
    # print(f'top light status: {traffic_lights[2].get_status()}')
    # print(f'bottom light status: {traffic_lights[3].get_status()}')

    draw_road(screen, WIDTH, HEIGHT, ROAD_WIDTH)
    # v1.draw(screen)
    # v2.draw(screen)
    # v3.draw(screen)
    # v4.draw(screen)
    # v5.draw(screen)
    # v6.draw(screen)
    # v7.draw(screen)
    # v8.draw(screen)

    for vehicle in vehicles:
        vehicle.draw(screen)
        light = find_associate_light(vehicle)
        vehicle.move(vehicles_dict, light)
        # if vehicle.pos[0]

    # v1.move()
    # v2.move()
    # v3.move()
    # v4.move()
    # v5.move()
    # v6.move()
    # v7.move()
    # v8.move()

    pygame.display.flip()

