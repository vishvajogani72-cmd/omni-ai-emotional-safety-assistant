import pygame
import random
import math
import time
import voice_assistance


# =========================================================
# SCREEN
# =========================================================

WIDTH = 900
HEIGHT = 600

BLACK = (3, 5, 8)
BLUE = (0, 230, 255)

# =========================================================
# EYE POSITIONS
# =========================================================

LEFT_EYE = (320, 250)
RIGHT_EYE = (580, 250)

EYE_RADIUS = 35
PUPIL_RADIUS = 11


# =========================================================
# CURRENT EMOTION
# =========================================================

current_emotion = "neutral"

def set_emotion(emotion):

    global current_emotion

    if emotion is None:
        current_emotion = "neutral"
        return

    # If your emotion model returns:
    # ("happy", 0.92)
    # take only the emotion name.

    if isinstance(emotion, tuple):
        emotion = emotion[0]

    current_emotion = str(emotion).lower()

    print("🎭 Avatar emotion:", current_emotion)
# =========================================================
# EYE MOVEMENT
# =========================================================

pupil_x = 0
pupil_y = 0

target_x = 0
target_y = 0


def update_eyes():
    global pupil_x
    global pupil_y
    global target_x
    global target_y

    mouse_x, mouse_y = pygame.mouse.get_pos()

    dx = mouse_x - WIDTH // 2
    dy = mouse_y - HEIGHT // 2

    distance = math.sqrt(
        dx * dx + dy * dy
    )

    max_distance = 18

    if distance > 0:
      target_x = (
            dx / distance
        ) * max_distance

      target_y = (
            dy / distance
        ) * max_distance

    # Smooth movement

    pupil_x += (
        target_x - pupil_x
    ) * 0.08

    pupil_y += (
        target_y - pupil_y
    ) * 0.08
# =========================================================
# BLINK
# =========================================================

blink = False
blink_timer = 0

next_blink = random.randint(
    180,
    350
)


def update_blink():

    global blink
    global blink_timer
    global next_blink
    blink_timer += 1

    if blink_timer >= next_blink:

        blink = True

    if blink_timer >= next_blink + 10:

        blink = False

        blink_timer = 0

        next_blink = random.randint(
            180,
            350
        )
# =========================================================
# DRAW EYE
# =========================================================

def draw_eye(
    screen,
    center,
    radius,
    pupil_radius
):

    # Bright blue eye

    pygame.draw.circle(
        screen,
        BLUE,
        center,
        radius
    )

# Pupil

    pupil_position = (
        center[0] + int(pupil_x),
        center[1] + int(pupil_y)
    )

    pygame.draw.circle(
        screen,
        BLACK,
        pupil_position,
        pupil_radius
    )


# =========================================================
# DRAW EMOTION EYES
# =========================================================
def draw_emotion_eyes(screen):

    global blink

    # -------------------------------------
    # BLINK
    # -------------------------------------

    if blink:

        pygame.draw.line(
            screen,
            BLUE,
            (295, 250),
            (345, 250),
            6
        )
        pygame.draw.line(
            screen,
            BLUE,
            (555, 250),
            (605, 250),
            6
        )

        return


    # -------------------------------------
    # HAPPY
    # -------------------------------------

    if current_emotion == "happy":

        pygame.draw.arc(
             screen,
            BLUE,
            (285, 225, 70, 50),
            0,
            math.pi,
            6
        )

        pygame.draw.arc(
            screen,
            BLUE,
            (545, 225, 70, 50),
            0,
            math.pi,
            6
        )
        return
        # -------------------------------------
    # SAD
    # -------------------------------------

    if current_emotion == "sad":

         draw_eye(
            screen,
            (320, 258),
            30,
            10
         )

         draw_eye(
            screen,
            (580, 258),
            30,
            10
         )
         # Sad eyebrows

         pygame.draw.line(
            screen,
            BLUE,
            (285, 210),
            (345, 220),
            6
        )

         pygame.draw.line(
            screen,
            BLUE,
            (555, 220),
            (615, 210),
            6
        )
         pygame.draw.line(
          screen,
            BLUE,
            (555, 220),
            (615, 210),
            6
        )

         return


    # -------------------------------------
    # ANGRY
    # -------------------------------------

    if current_emotion == "angry":

        draw_eye(
            screen,
            (320, 250),
            30,
            10
        )

        draw_eye(
            screen,
            (580, 250),
            30,
            10
        )

        # Angry eyebrows

        pygame.draw.line(
            screen,
            BLUE,
            (285, 215),
             (345, 230),
            8
        )

        pygame.draw.line(
            screen,
            BLUE,
            (555, 230),
            (615, 215),
            8
        )

        return
     # -------------------------------------
    # STRESSED
    # -------------------------------------

    if current_emotion == "stressed":

        draw_eye(
            screen,
            (320, 255),
            32,
            10
        )

        draw_eye(
            screen,
            (580, 255),
            32,
            10
        )

        # Worried eyebrows

        pygame.draw.line(
            screen,
            BLUE,
            (285, 215),
            (345, 205),
            6
        )

        pygame.draw.line(
            screen,
            BLUE,
            (555, 205),
            (615, 215),
            6
        )

        return


    # -------------------------------------
    # SURPRISED
    # -------------------------------------

    if current_emotion == "surprised":

        draw_eye(
            screen,
            (320, 245),
            42,
            13
        )

        draw_eye(
            screen,
            (580, 245),
            42,
            13
        )

        return


    # -------------------------------------
    # NEUTRAL
    # -------------------------------------

    draw_eye(
        screen,
        LEFT_EYE,
        EYE_RADIUS,
        PUPIL_RADIUS
    )

    draw_eye(
        screen,
        RIGHT_EYE,
        EYE_RADIUS,
        PUPIL_RADIUS
    )


# =========================================================
# MOUTH
# =========================================================

mouth_open = False
mouth_timer = 0


def draw_mouth(screen):

    global mouth_open
    global mouth_timer

    # -------------------------------------
    # SPEAKING
    # -------------------------------------

    if voice_assistance.is_speaking:

        mouth_timer += 1

        if mouth_timer >= 5:

            mouth_open = not mouth_open

            mouth_timer = 0


        # -------------------------------
        # OPEN MOUTH
        # -------------------------------

        if mouth_open:

            # Surprised / excited mouth

            if current_emotion == "surprised":

                pygame.draw.ellipse(
                    screen,
                    BLUE,
                    (415, 350, 70, 70)
                )

            else:

                pygame.draw.ellipse(
                    screen,
                    BLUE,
                    (405, 345, 90, 65)
                )


        # -------------------------------
        # SMALL OPEN MOUTH
        # -------------------------------

        else:

            pygame.draw.ellipse(
                screen,
                BLUE,
                (410, 365, 80, 25)
            )

        return


    # -------------------------------------
    # NOT SPEAKING
    # -------------------------------------

    mouth_open = False
    mouth_timer = 0


    # -------------------------------------
    # HAPPY MOUTH
    # -------------------------------------

    if current_emotion == "happy":

        pygame.draw.arc(
            screen,
            BLUE,
            (390, 350, 120, 70),
            math.pi,
            2 * math.pi,
            7
        )

        return


    # -------------------------------------
    # SAD MOUTH
    # -------------------------------------

    if current_emotion == "sad":

        pygame.draw.arc(
            screen,
            BLUE,
            (395, 375, 110, 50),
            0,
            math.pi,
            7
        )

        return


    # -------------------------------------
    # ANGRY MOUTH
    # -------------------------------------

    if current_emotion == "angry":

        pygame.draw.line(
            screen,
            BLUE,
            (405, 380),
            (495, 380),
            7
        )

        return


    # -------------------------------------
    # STRESSED MOUTH
    # -------------------------------------

    if current_emotion == "stressed":

        pygame.draw.arc(
            screen,
            BLUE,
            (405, 365, 90, 35),
            0,
            math.pi,
            6
        )

        return


    # -------------------------------------
    # SURPRISED MOUTH
    # -------------------------------------

    if current_emotion == "surprised":

        pygame.draw.ellipse(
            screen,
            BLUE,
            (420, 350, 60, 65)
        )

        return


    # -------------------------------------
    # NEUTRAL MOUTH
    # -------------------------------------

    pygame.draw.line(
        screen,
        BLUE,
        (410, 375),
        (490, 375),
        6
    )


# =========================================================
# MAIN AVATAR DRAW FUNCTION
# =========================================================

def draw_avatar(screen):

    update_eyes()

    update_blink()

    draw_emotion_eyes(screen)

    draw_mouth(screen)
