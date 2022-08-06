from fcntl import F_SEAL_SEAL
import pygame
from enum import Enum
from variables import *
from traffic_light import *

zebra_crossing_dist = ROAD_WIDTH/2*1.4
gap = 40

class Direction(Enum):
    up = 1
    down = 2
    left = 3
    right = 4


class Lane(Enum):
    right = 1
    left = 2


class Vehicle:
    def __init__(self, speed, width, height, lane, direction, dest_direction):
        self.lane = lane
        self.speed = speed
        self.width = width
        self.height = height
        self.direction = direction
        self.dest_direction = dest_direction
        self.crossed_zebra = 0
        self.pos = self._get_coordinate(direction, lane)

    def _get_coordinate(self, direction, lane):
        x = 0
        y = 0
        if direction == Direction.left:
            y = HEIGHT / 2
            if lane == Lane.right:
                y -= 3 / 4 * ROAD_WIDTH / 2
            else:
                y -= 1 / 4 * ROAD_WIDTH / 2 + 3
        elif direction == Direction.right:
            x = WIDTH
            y = HEIGHT / 2
            if lane == Lane.left:
                y += 3 / 4 * ROAD_WIDTH / 2
            else:
                y += 1 / 4 * ROAD_WIDTH / 2 + 3
        elif direction == Direction.up:
            x = WIDTH / 2
            if lane == Lane.left:
                x += 3 / 4 * ROAD_WIDTH / 2
            else:
                x += 1 / 4 * ROAD_WIDTH / 2 + 3
        else:
            x = WIDTH / 2
            y = HEIGHT
            if lane == Lane.right:
                x -= 3 / 4 * ROAD_WIDTH / 2
            else:
                x -= 1 / 4 * ROAD_WIDTH / 2 + 3
        return [x, y]

    def get_speed(self) -> int:
        return self.speed
    
    def check_bump(self, vehicle_dict):
        vehicles = vehicle_dict[self.direction][self.lane]
        for vehicle in vehicles:
            if self == vehicle:
                return False
            if self.direction == Direction.left or self.direction == Direction.right:
                if abs(vehicle.pos[0] - self.pos[0]) <= gap:
                    return True
            else:
                if abs(vehicle.pos[1] - self.pos[1]) <= gap:
                    return True
        return False

    def move(self, dict, light):
        status = self.check_bump(dict)
        traffic = light.get_status()
        if status == True:
            return False
        if self.direction == Direction.left:
            if not self.crossed_zebra and traffic == TrafficLightStatus.red and ((self.pos[0] + self.width / 2) >= (WIDTH_CENTRE - ZEBRA_CROSSING_DIST - 20)):
                return False
            if (not self.crossed_zebra and self.pos[0] + self.width / 2 > WIDTH_CENTRE - ZEBRA_CROSSING_DIST):
                self.crossed_zebra = 1
            # if (self.crossed_zebra == 0 and self.pos[0] - self.width / 2 < WIDTH/2+zebra_crossing_dist):
            if True:
                self.pos[0] += self.speed
            elif (self.dest_direction == Direction.right):
                # self.pos[0] += self.speed
                pass
            elif (self.dest_direction == Direction.up):
                pass
            elif (self.dest_direction == Direction.down):
                pass
            return True
        elif self.direction == Direction.right:
            # print(self.crossed_zebra, traffic, (self.pos[0] - self.width / 2) <= (WIDTH_CENTRE + ZEBRA_CROSSING_DIST + 14))
            # print(self.crossed_zebra)
            if (not self.crossed_zebra and (traffic == TrafficLightStatus.red) and self.pos[0] - self.width /2  <= (WIDTH_CENTRE + ZEBRA_CROSSING_DIST + 20) ):
                return False
            # if (self.crossed_zebra == 0 and self.pos[0] - self.width / 2 > WIDTH/2+zebra_crossing_dist):
            if (not self.crossed_zebra and self.pos[0] - self.width / 2 < WIDTH_CENTRE + ZEBRA_CROSSING_DIST):
                self.crossed_zebra = 1
            if True:
                self.pos[0] -= self.speed
            elif (self.dest_direction == Direction.left):
                self.pos[0] -= self.speed
            elif (self.dest_direction == Direction.up):
                pass
            elif (self.dest_direction == Direction.down):
                pass
            return True
        elif self.direction == Direction.up:
            if not self.crossed_zebra and traffic == TrafficLightStatus.red and (self.pos[1] + self.height / 2) >= (HEIGHT_CENTRE - ZEBRA_CROSSING_DIST - 20):
                return False
            if (not self.crossed_zebra and self.pos[1] + self.height / 2 > HEIGHT_CENTRE-zebra_crossing_dist):
                self.crossed_zebra = 1
            if True:
                self.pos[1] += self.speed
            elif (self.dest_direction == Direction.down):
                self.pos[1] += self.speed
            elif (self.dest_direction == Direction.left):
                pass
            elif (self.dest_direction == Direction.right):
                pass
            return True
        else:
            if not self.crossed_zebra and traffic == TrafficLightStatus.red and (self.pos[1] - self.height / 2) <= (HEIGHT_CENTRE + ZEBRA_CROSSING_DIST + 20):
                return False
            # if (self.crossed_zebra == 0 and self.pos[1] - self.height / 2 > HEIGHT/2+zebra_crossing_dist):
            if (not self.crossed_zebra and self.pos[1] - self.height / 2 < HEIGHT_CENTRE+zebra_crossing_dist):
                self.crossed_zebra = 1
            if True:
                self.pos[1] -= self.speed
            elif (self.dest_direction == Direction.up):
                self.pos[1] -= self.speed
            elif (self.dest_direction == Direction.left):
                self.pos[1] -= self.speed
            elif (self.dest_direction == Direction.right):
                pass
            return True
        pass

    def stop(self):
        pass

    def change_speed(self):
        pass

    def _get_rect_pos(self):
        x = (self.pos[0] - self.width / 2 , self.pos[1] - self.height / 2, self.width, self.height)
        return x

    # @abstractmethod
    def draw(self, screen):
        # print(self._get_rect_pos())
        pygame.draw.rect(screen, 'blue', self._get_rect_pos())
        pass


class Bus(Vehicle):
    def __init__(self, pos, speed, length, breadth) -> None:
        super().__init__(pos, speed, length, breadth)


class Car(Vehicle):
    def __init__(self, pos, speed, length, breadth) -> None:
        super().__init__(pos, speed, length, breadth)

    