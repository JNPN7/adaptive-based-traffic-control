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
        self.font2 = pygame.font.SysFont('freesanbold.ttf', 35)
        self.txt = self.font1.render(txt, True, (0, 0, 0))
        self.txt_rect = self.txt.get_rect()
        self.pos = (x, y)
        self.txt_rect.center = self.pos 
        self.status = TrafficLightStatus[color]
        self.radius = 15
        # self.RedTime = 9
        # self.GreenTime = 8
        self.RedTime = 8
        self.GreenTime = 7
        self.YellowTime = 1
    
    def alterLights1(self, index):
        if index == 0 or index == 1:
            self.status = TrafficLightStatus.green
            sleep(self.GreenTime)
            self.status = TrafficLightStatus.yellow
            sleep(self.YellowTime)
            self.status = TrafficLightStatus.red
            sleep(self.RedTime)
        else:
            self.status = TrafficLightStatus.red
            sleep(self.RedTime)
            self.status = TrafficLightStatus.green
            sleep(self.GreenTime)
            self.status = TrafficLightStatus.yellow
            sleep(self.YellowTime)
    

    def alterLights2(self, index):
        self.status = TrafficLightStatus.green
        sleep(self.GreenTime)
        self.status = TrafficLightStatus.yellow
        sleep(self.YellowTime)
        self.status = TrafficLightStatus.red

    def toggleLightStatus(self) -> None:
        if self.status == TrafficLightStatus.green:
            sleep(5)
            self.status = TrafficLightStatus.red
        # elif self.status == TrafficLightStatus.green:
        #     self.status = TrafficLightStatus.yellow
        #     # some delay
        #     sleep(2)
        #     self.status = TrafficLightStatus.red
    
    def get_status(self) -> TrafficLightStatus:
        return self.status
    
    def changeLights(self, index):
        # self.toggleLightStatus()
        # print(index)
        self.alterLights2(index)

        # self.alterLights1(index)

        # sleep(5)

    # def changeLights(self):
    #     self.toggleLightStatus()
    #     # self.alterLights()
    #     sleep(5)

    def change_green_light_time(self, time):
        self.GreenTime = time

    def change_red_light_time(self, time):
        self.RedTime = time

    def change_yelow_light_time(self, time):
        # print(time)
        self.YellowTime = time
        # print(self.YellowTime)

    def draw(self, screen, count):
        count_txt = self.font2.render(str(count), True, (0, 0, 0), (255, 255, 255)) 
        txt_rect = count_txt.get_rect()
        if self.text == 'L'  or self.text == 'B':
            pos = (self.pos[0]-25, self.pos[1])
        else:
            pos = (self.pos[0]+25, self.pos[1])
        txt_rect.center = pos

        pygame.draw.circle(screen, self.status.value, center=self.pos, radius=self.radius)
        screen.blit(self.txt, self.txt_rect)
        screen.blit(count_txt, txt_rect)