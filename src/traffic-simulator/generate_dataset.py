from fileinput import close
from xml.dom.minidom import TypeInfo
from variables import ROAD_WIDTH
from vehicles import Lane, Direction, Vehicle
import random
import json
# import ast

# data = {}
with open('dataset.txt', 'w') as file:
    pass
file.close()

for i in range(50):
    lane = Lane(random.randint(1, 2))
    direction = Direction(random.randint(1, 4))
    lst = list(range(1, 5))
    del lst[direction.value - 1]
    dest_direciton = Direction(random.choice(lst))
    data = {
        'speed': 0.17,
        'width': ROAD_WIDTH/6,
        'height': ROAD_WIDTH/6,
        'lane': random.randint(1, 2),
        'direction': random.randint(1, 4),
        'dest_direction': random.choice(lst)
    }
    # print(data)
    # vehicle = Vehicle(0.17, ROAD_WIDTH / 6, ROAD_WIDTH /
    #   6, lane, direction, dest_direciton)
    # print(type(vehicle.dict))
    # data = json.dumps(vehicle.dict)
    # print(data['lane'])
    with open('dataset.txt', 'a') as file:
        #     file.write(str(data)+'\n')
        json.dump(data, file)
    # print(vehicle.direction)
    file.close()

with open('dataset.txt', 'r') as file:
    # data = json.load(file)
    data = data[0].split('\n')[0]
    print(data)
file.close()