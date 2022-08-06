import pygame
from math import hypot

class Point:

    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]

    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))

    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y))

    def __mul__(self, scalar):
        return Point((self.x * scalar, self.y * scalar))

    def __truediv__(self, scalar):
        return Point((self.x / scalar, self.y / scalar))

    def __len__(self):
        return int(hypot(self.x, self.y))

    def get(self):
        return (self.x, self.y)


def dashed_line(surface, color, start_pos, end_pos, width=1, dash_length=10):
    origin = Point(start_pos)
    target = Point(end_pos)
    displacement = target - origin
    length = len(displacement)
    slope = displacement / length

    for index in range(0, int(length / dash_length), 2):
        start = origin + (slope * index * dash_length)
        end = origin + (slope * (index + 1) * dash_length)
        # print(start.get())
        # print(end.get())
        pygame.draw.line(surface, color, start.get(), end.get(), width)


def dashed_zebra_line(surface, color, start_pos, end_pos, width=1, dash_length=10):
    origin = Point(start_pos)
    target = Point(end_pos)
    displacement = target - origin
    length = len(displacement)
    slope = displacement / length

    for index in range(0, int(length / dash_length), 10):
        start = origin + (slope * index * dash_length)
        end = origin + (slope * (index + 1) * dash_length)
        # print(start.get())
        # print(end.get())
        pygame.draw.line(surface, color, start.get(), end.get(), width)

def dashed_rect(surface, color, rect, width=1, dash_length=10):
    rect = pygame.Rect(rect)

    try: dashed_line(surface, color, (rect.x, rect.y), (rect.width, rect.y), width, dash_length)
    except Exception as e:
        if not isinstance(e, ZeroDivisionError): raise e

    try: dashed_line(surface, color, (rect.width, rect.y), (rect.width, rect.height), width, dash_length)
    except Exception as e:
        if not isinstance(e, ZeroDivisionError): raise e

    try: dashed_line(surface, color, (rect.width, rect.height), (rect.x, rect.height), width, dash_length)
    except Exception as e:
        if not isinstance(e, ZeroDivisionError): raise e

    try: dashed_line(surface, color, (rect.x, rect.height), (rect.x, rect.y), width, dash_length)
    except Exception as e:
        if not isinstance(e, ZeroDivisionError): raise e