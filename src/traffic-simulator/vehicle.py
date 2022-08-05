from abc import abstractmethod
from winreg import DisableReflectionKey
import pygame

class Vehicle:
    def __init__(self, pos, speed, length, breadth) -> None:
        self.lane = lane,
        self.direction = direction,
        
        self.speed = speed
        self.length = length
        self.breadth = breadth
        self.pos = pos
        pass

    def get_speed(self) -> int:
        return self.speed
    
    def move(self):
        pass
    
    def stop(self):
        pass

    def change_speed(self):
        pass

    @abstractmethod
    def draw(self, screen):
        pass
    


class Bus(Vehicle):
    def __init__(self, pos, speed, length, breadth) -> None:
        super().__init__(pos, speed, length, breadth)
    

class Car(Vehicle):
    def __init__(self, pos, speed, length, breadth) -> None:
        super().__init__(pos, speed, length, breadth)