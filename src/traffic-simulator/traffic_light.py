from enum import Enum
class TrafficLightStatus(Enum):
    red = 1
    yellow = 2
    green = 3

class TrafficLight():
    def __init__(self) -> None:
        self.status = TrafficLightStatus.red
    
    def toggleLightStatus(self) -> None:
        if self.status == TrafficLightStatus.red:
            self.status = TrafficLightStatus.yellow
            # some delay
            self.status = TrafficLightStatus.green
        elif self.status == TrafficLightStatus.green:
            self.status = TrafficLightStatus.yellow
            # some delay
            self.status = TrafficLightStatus.red
    
    def get_status(self) -> TrafficLightStatus:
        return self.status
