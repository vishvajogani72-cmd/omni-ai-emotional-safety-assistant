import pygame
import random
import sys

pygame.init()
width=900
height=600
screen=pygame.display.set_mode((900,600))
pygame.display.set_caption("Emotional AI")

clock=pygame.time.Clock()
Black=(3,5,8)
Blue=(0,220,255)

LEFT_EYE=(320,250)
RIGHT_EYE=(580,250)

#binking movements
blink=False
blink_timer=0
next_blink=random.randint(120,300)

def draw_glow_circle(surface,position,radius):
    """Create a simple neon glow"""

    glow=pygame.Surface((radius*6,radius*6),pygame.SRCALPHA)

    center=(radius*3,radius*3)

    for r in range(radius * 3, radius, -5):
        alpha=int(40*(radius*3-r)/(radius * 2))
        pygame.draw.circle(glow,(0,220,255,alpha),center,r)

    surface.blit(glow,(position[0]-radius*3,position[1]-radius*3))
    pygame.draw.circle(surface,Blue,position,radius)

running = True
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    blink_timer+=1
    if blink_timer>=next_blink:
        blink=True

        #Blink lasts a short time
        if blink_timer >= next_blink + 10:
            blink=False
            blink_timer=0
            next_blink=random.randint(120,300)

    screen.fill(Black)
    if not blink:
        draw_glow_circle(screen,LEFT_EYE,28)
        draw_glow_circle(screen,RIGHT_EYE,28)
    else:
        # Draw horizontal lines for blinking eyes
        pygame.draw.line(screen,Blue,(295,250),(345,250),6)
        pygame.draw.line(screen,Blue,(555,250),(605,250),6)

    # Draw mouth
    pygame.draw.ellipse(screen,Blue,(410,360,80,35))

    pygame.display.flip()
    clock.tick(60)
