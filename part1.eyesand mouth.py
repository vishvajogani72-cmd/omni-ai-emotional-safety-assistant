import pygame
import sys
# first of all create blue face of ai box
pygame.init()

width=900
height=600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Emotional AI")

clock=pygame.time.Clock()
#background and face colors

Black=(5,5,8)
Blue=(0,220,255)

LEFT_EYE=(320,250)
RIGHT_EYE=(580,250)
MOUTH=(450,380)

while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill(Black)
    #eyes shape
    pygame.draw.circle(screen,Blue,LEFT_EYE,28)
    pygame.draw.circle(screen,Blue,RIGHT_EYE,28)

    # mouth expresion
    pygame.draw.ellipse(screen,Blue,(410,360,80,35))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
