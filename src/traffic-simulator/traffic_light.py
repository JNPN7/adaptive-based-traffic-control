from enum import Enum
from time import sleep
import pygame

class TrafficLightStatus(Enum):
    red = pygame.Color(255, 0, 0)
    yellow = pygame.Color(255, 255, 0) 
    green = pygame.Color(0, 255, 0) 

class TrafficLight():

    def __init__(self, x, y, txt, color) -> None:
        pygame.font.get_init()
        self.text = txt   
        self.font1 = pygame.font.SysFont('freesanbold.ttf', 30)
        self.txt = self.font1.render(txt, True, (0, 0, 0))
        self.txt_rect = self.txt.get_rect()
        self.pos = (x, y)
        self.txt_rect.center = self.pos 
        self.status = TrafficLightStatus[color]
        self.radius = 15
    
    def alterLights(self, index):
        if index == 0 or index == 1:
            self.status = TrafficLightStatus.green
            sleep(5)
            self.status = TrafficLightStatus.yellow
            sleep(2)
            self.status = TrafficLightStatus.red
            sleep(7)
        else:
            self.status = TrafficLightStatus.red
            sleep(7)
            self.status = TrafficLightStatus.green
            sleep(5)
            self.status = TrafficLightStatus.yellow
            sleep(2)
        

    def toggleLightStatus(self) -> None:
        if self.status == TrafficLightStatus.red:
            self.status = TrafficLightStatus.green
        elif self.status == TrafficLightStatus.green:
            self.status = TrafficLightStatus.yellow
            # some delay
            sleep(2)
            self.status = TrafficLightStatus.red
    
    def get_status(self) -> TrafficLightStatus:
        return self.status
    
    def changeLights(self, index):
        # self.toggleLightStatus()
        # print(index)
        self.alterLights(index)
        # sleep(5)

    # def changeLights(self):
    #     self.toggleLightStatus()
    #     # self.alterLights()
    #     sleep(5)

    def draw(self, screen, count):
        count_txt = self.font1.render(str(count), True, (0, 0, 0)) 
        txt_rect = count_txt.get_rect()
        if self.text == 'L'  or self.text == 'B':
            pos = (self.pos[0]-25, self.pos[1])
        else:
            pos = (self.pos[0]+25, self.pos[1])
        txt_rect.center = pos

        pygame.draw.circle(screen, self.status.value, center=self.pos, radius=self.radius)
        screen.blit(self.txt, self.txt_rect)
        screen.blit(count_txt, txt_rect)