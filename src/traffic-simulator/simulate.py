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
                 WIDTH / 2 - ROAD_WIDTH / 2 * 1.4, 'L','red'),
    TrafficLight(HEIGHT / 2 - ROAD_WIDTH / 2 * 1.4,
                 WIDTH / 2 + ROAD_WIDTH / 2 * 1.4, 'B','red'),
    TrafficLight(HEIGHT / 2 + ROAD_WIDTH / 2 * 1.4,
                 WIDTH / 2 + ROAD_WIDTH / 2 * 1.4, 'R','red'),
    TrafficLight(HEIGHT / 2 + ROAD_WIDTH / 2 * 1.4,
                 WIDTH / 2 - ROAD_WIDTH / 2 * 1.4, 'T','red'),
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
vehicles_stopped = {
    Direction.left : [],
    Direction.down : [],
    Direction.right : [],
    Direction.up : [],
}
vehicles = []
vehicles_dict = {
    Direction.left: {
        # Direction.right: [],
        # Direction.up: [],
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
}

def find_associate_light(vehicle):
    if vehicle.direction == Direction.left:
        return traffic_lights[0]
    elif vehicle.direction == Direction.down:
        return traffic_lights[1]
    elif vehicle.direction == Direction.right:
        return traffic_lights[2]
    return traffic_lights[3]

def generate_vehicle():
    while True: 
        lane = Lane(random.randint(1, 2))
        direction = Direction(random.randint(1, 4))
        lst = list(range(1, 5))
        del lst[direction.value - 1]
        dest_direciton = Direction(random.choice(lst))
        vehicle = Vehicle(0.17, ROAD_WIDTH / 6, ROAD_WIDTH / 6, lane, direction, dest_direciton)
        vehicles.append(vehicle)
        vehicles_dict[direction][lane].append(vehicle)
        # print(vehicles_dict)
        sleep(0.5)

def initialize_lights(indexs):
    while True:
        if indexs == 10:
            for index, traffic in enumerate(traffic_lights):
                # print(traffic)
                traffic.changeLights(index)
        else:
            traffic_lights[indexs].changeLights(indexs)


traffic_light_thread = threading.Thread(name="initialization", target=initialize_lights, args=(10,))
traffic_light_thread.daemon = True
traffic_light_thread.start()

def lightsChange1():
    traffic_light_thread1 = threading.Thread(name="initialization1", target=initialize_lights, args=(0,))
    traffic_light_thread1.daemon = True
    traffic_light_thread1.start()

    traffic_light_thread2 = threading.Thread(name="initialization2", target=initialize_lights, args=(1,))
    traffic_light_thread2.daemon = True
    traffic_light_thread2.start()

    traffic_light_thread3 = threading.Thread(name="initialization3", target=initialize_lights, args=(2,))
    traffic_light_thread3.daemon = True
    traffic_light_thread3.start()

    traffic_light_thread4 = threading.Thread(name="initialization4", target=initialize_lights, args=(3,))
    traffic_light_thread4.daemon = True
    traffic_light_thread4.start()

traffic_lights[1].change_green_light_time(3)

def get_greenligth_time(no_of_vehicles):
    time = 2
    if no_of_vehicles == 0:
        return 0
    elif no_of_vehicles == 1:
        return time
    else:
        time += float(no_of_vehicles-1)*0.15
    return time

def get_yellowligth_time(no_of_vehicles):
    time = 1.5
    if no_of_vehicles == 0:
        return 0
    elif no_of_vehicles == 1:
        return time
    else:
        time += float(no_of_vehicles-1)*0.1
    return time

# lightsChange1()

# def lightsChange2():
#     traffic_light_thread1 = threading.Thread(name="initialization1", target=initialize_lights, args=(0,))
#     traffic_light_thread1.daemon = True
#     traffic_light_thread1.start()

#     traffic_light_thread2 = threading.Thread(name="initialization2", target=initialize_lights, args=(1,))
#     traffic_light_thread2.daemon = True
#     traffic_light_thread2.start()

#     traffic_light_thread3 = threading.Thread(name="initialization3", target=initialize_lights, args=(2,))
#     traffic_light_thread3.daemon = True
#     traffic_light_thread3.start()

#     traffic_light_thread4 = threading.Thread(name="initialization4", target=initialize_lights, args=(3,))
#     traffic_light_thread4.daemon = True
#     traffic_light_thread4.start()




# lightsChange2()

generate_vehicle_thread = threading.Thread(name="Initialization", target=generate_vehicle, args=())
generate_vehicle_thread.daemon = True
generate_vehicle_thread.start()


while 1:
    pygame.draw.rect(screen, pygame.Color(255, 0, 0), (0, 10, 10, 10))

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()

    # ballrect = ballrect.move(speed)


    screen.fill('brown')

    for i, traffic in enumerate(traffic_lights):
        count = len(vehicles_stopped[list(vehicles_stopped.keys())[i]])
        traffic.draw(screen, count)
    
    # print(vehicles_stopped[list(vehicles_stopped.keys())[0]])
    
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
    temp_vechiles = vehicles

    for vehicle in vehicles:
        vehicle.draw(screen)
        light = find_associate_light(vehicle)
        isMoving = vehicle.move(vehicles_dict, light)
        if not isMoving:
            if vehicle not in vehicles_stopped[vehicle.direction]:
                vehicles_stopped[vehicle.direction].append(vehicle)
        else:
            if vehicle in vehicles_stopped[vehicle.direction]: vehicles_stopped[vehicle.direction].remove(vehicle)

        if vehicle.pos[0] <= - 20 or vehicle.pos[0] >= WIDTH + 20 or vehicle.pos[1] <= -20 or vehicle.pos[1] >= WIDTH + 20:
            temp_vechiles.remove(vehicle)
            vehicles_dict[vehicle.direction][vehicle.lane].remove(vehicle)

    vehicles = temp_vechiles
    for i, light in enumerate(traffic_lights):
        no_of_vehicles = len(vehicles_stopped[list(vehicles_stopped.keys())[i]])
        greentime = get_greenligth_time(no_of_vehicles)
        light.change_green_light_time(greentime)
        yellowtime = get_yellowligth_time(no_of_vehicles)
        print(greentime)
        # light.change_yelow_light_time(yellowtime)

    # v1.move()
    # v2.move()
    # v3.move()
    # v4.move()
    # v5.move()
    # v6.move()
    # v7.move()
    # v8.move()

    pygame.display.flip()

