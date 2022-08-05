import sys, pygame
from color import Color 
from road import draw_road

pygame.init()


size = width, height = 650, 650

speed = [0, 0]

black = 0, 0, 0


screen = pygame.display.set_mode(size)


ball = pygame.image.load("img.jpg")
# ball = 
pygame.draw.rect(screen, pygame.Color(255, 0, 0), (0, 10, 10 , 10))

ballrect = ball.get_rect()


while 1:
    pygame.draw.rect(screen, pygame.Color(255, 0, 0), (0, 10, 10 , 10))

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()


    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > width:

        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > height:

        speed[1] = -speed[1]


    screen.fill(Color.green.value)

    # screen.blit(ball, ballrect)

    draw_road(screen, width, height)
    pygame.display.flip()