import pygame
import random
import sys
import math
emotion="neutral"

def set_emotion(new_emotion):
    global emotion
    emotion=new_emotion

pygame.init()

width=900
height=600
set_emotion("happy")

screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Emotional AI")

clock=pygame.time.Clock()
Black=(3,5,8)
Blue=(0,220,255)

#eyes position
LEFT_EYE=(320,250)    
RIGHT_EYE=(580,250)

EYE_RADIUS=32
PUPTL_RADIUS=10

# Blinking line width
BLINK_LINE_WIDTH = 50

# Mouth
MOUTH_RECT = pygame.Rect(410, 360, 80, 35)
# PUPIL MOVEMENT

pupil_x=0
pupil_y=0

target_x=0
target_y=0

# blinking movements
blink=False
blink_timer=0
next_blink=random.randint(180,360)



def draw_glow_circle(surface,position,radius):
    glow=pygame.Surface((radius*6,radius*6),pygame.SRCALPHA)

    center=(radius*3,radius*3)

    for r in range(radius*3,radius,-5):
        alpha=int(40*(radius*3-r)/(radius*2))
        pygame.draw.circle(glow,(0,220,255,alpha),center,r)
    
    surface.blit(glow,(position[0]-radius*3,position[1]-radius*3))
    pygame.draw.circle(surface,Blue,position,radius)

def draw_pupil(eye_center):
    """Draws the pupil inside an eye."""
    # pupil movement
    pupil_position=(eye_center[0]+pupil_x,eye_center[1]+pupil_y)
    pygame.draw.circle(screen,Black,pupil_position,PUPTL_RADIUS)

mouth_open=False
mouth_timer=0
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    #mouse position
    mouse_x,mouse_y=pygame.mouse.get_pos()

    # distancefrom center of screen

    dx=mouse_x-width//2
    dy=mouse_y-height//2

    distance=math.sqrt(dx**2+dy**2)

    # limit pupil movement
    max_distance=18

    if distance>0:

        target_x=(dx/distance)*max_distance
        target_y=(dy/distance)*max_distance

    # smooth pupil movement
    pupil_x+=(target_x-pupil_x)*0.08
    pupil_y+=(target_y-pupil_y)*0.08

    blink_timer+=1
    if blink_timer >= next_blink:
        blink = True
        if blink_timer >= next_blink + 10:
            blink=False
            blink_timer=0
            next_blink=random.randint(180,360)
    mouth_timer+=1
    if mouth_timer>=8:
        mouth_open=not mouth_open
        mouth_timer=0
    screen.fill(Black) 

    #eyes
    if not blink:
        draw_glow_circle(screen,LEFT_EYE,EYE_RADIUS)
        draw_glow_circle(screen,RIGHT_EYE,EYE_RADIUS)

        draw_pupil(LEFT_EYE)
        draw_pupil(RIGHT_EYE)
    else:
        # draw horizontal lines for blinking eyes
        left_blink_start = (LEFT_EYE[0] - BLINK_LINE_WIDTH // 2, LEFT_EYE[1])
        left_blink_end = (LEFT_EYE[0] + BLINK_LINE_WIDTH // 2, LEFT_EYE[1])
        pygame.draw.line(screen, Blue, left_blink_start, left_blink_end, 6)

        right_blink_start = (RIGHT_EYE[0] - BLINK_LINE_WIDTH // 2, RIGHT_EYE[1])
        right_blink_end = (RIGHT_EYE[0] + BLINK_LINE_WIDTH // 2, RIGHT_EYE[1])
        pygame.draw.line(screen, Blue, right_blink_start, right_blink_end, 6)

    # Draw mouth
    if emotion == "happy":
        # Draw a smile (upward arc)
        smile_rect = MOUTH_RECT.move(0, -10) # Move rect up slightly for a better smile position
        pygame.draw.arc(screen, Blue, smile_rect, math.pi, 2 * math.pi, 6)
    elif emotion == "neutral":
        if mouth_open:
            # open mouth
            pygame.draw.ellipse(screen, Blue, MOUTH_RECT)
        else:
            # closed mouth line
            pygame.draw.line(screen, Blue, (MOUTH_RECT.left, MOUTH_RECT.centery), (MOUTH_RECT.right, MOUTH_RECT.centery), 6)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
