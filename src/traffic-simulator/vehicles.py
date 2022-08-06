import pygame
from enum import Enum
from variables import *


class Direction(Enum):
    up = 'up'
    down = 'down'
    left = 'left'
    right = 'right'


class Lane(Enum):
    right = 1,
    left = 2


class Vehicle:

    def __init__(self, speed, length, breadth, lane, direction,
                 dest_direction):
        self.lane = lane,
        self.dest_direction = dest_direction,
        self.speed = speed
        self.length = length
        self.breadth = breadth
        self.direction = direction
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

    def move(self):
        if self.direction == Direction.down:
            self.pos[1] -= self.speed
        elif self.direction == Direction.up:
            self.pos[1] += self.speed
        elif self.direction == Direction.left:
            self.pos[0] += self.speed
        else:
            self.pos[0] -= self.speed
        pass

    def stop(self):
        pass

    def change_speed(self):
        pass

    def _get_rect_pos(self):
        x = (self.pos[0] - self.length / 2, self.pos[1] - self.breadth / 2,
             self.length, self.breadth)
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