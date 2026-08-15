import sys
import pygame
import threading
import emergency_history
import eyes_mouth
import voice_assistance
import omniai_brain
import emotion_ai
import reminder
import emergency
import location_ai
import sos_message
import intent_ai
import safety_engine
import emergency_type_ai
import safety_fusion
import emergency_response
import emergency_actions
import emergency_history

from silent_sos import SilentSOS
from safety_dashboard import SafetyDashboard



# ==========================================
# PYGAME INITIALIZATION
# ==========================================

pygame.init()

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Omni AI - Emotional AI")

clock = pygame.time.Clock()

BLACK = (3, 5, 8)
WHITE = (255, 255, 255)
SOS_RED = (180, 30, 30)
CONFIRM_GREEN = (25, 140, 75)
CANCEL_GRAY = (90, 90, 100)

font = pygame.font.Font(None, 32)
small_font = pygame.font.Font(None, 24)

SOS_BUTTON = pygame.Rect(350, 500, 200, 60)

CONFIRM_BUTTON = pygame.Rect(220, 510, 210, 55)
CANCEL_BUTTON = pygame.Rect(470, 510, 210, 55)


# ==========================================
# APPLICATION STATE
# ==========================================

running = True
emergency_screen = False
emergency_in_progress = False

state_lock = threading.Lock()

silent_sos = SilentSOS()
safety_dashboard = SafetyDashboard(screen)

emergency_location = location_ai.get_location()

current_risk_level = "CRITICAL"
current_risk_score = 100
current_emergency_type = "GENERAL_EMERGENCY"
current_risk_reason = "Emergency detected"

last_reminder_check = pygame.time.get_ticks()
REMINDER_CHECK_INTERVAL = 10000


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def draw_centered_text(text, rect, text_color=WHITE, text_font=font):
    rendered_text = text_font.render(text, True, text_color)

    screen.blit(
        rendered_text,
        (
            rect.centerx - rendered_text.get_width() // 2,
            rect.centery - rendered_text.get_height() // 2
        )
    )


def get_safety_state():
    """Safely read the values shared by voice and Pygame threads."""
    with state_lock:
        return (
            current_risk_level,
            current_risk_score,
            current_emergency_type,
            current_risk_reason
        )


def open_emergency_screen(source="manual"):
    global emergency_screen

    emergency_screen = True
    print(f"🚨 Emergency confirmation screen opened ({source}).")


def activate_sos():
    """
    Generates one SOS message, prepares actions for every contact,
    then activates the emergency system only once.
    """
    global emergency_in_progress
    global emergency_screen

    if emergency_in_progress:
        print("⚠️ Emergency action is already in progress.")
        return

    emergency_in_progress = True
    emergency_screen = False

    try:
        risk_level, risk_score, emergency_type, risk_reason = get_safety_state()

        print()
        print("================================")
        print("        🚨 SOS CONFIRMED")
        print("================================")

        message = sos_message.generate_sos_message(
            emergency_type=emergency_type,
            risk_level=risk_level,
            risk_score=risk_score,
            risk_reason=risk_reason
        )

        print()
        print("================================")
        print("         🚨 SOS MESSAGE")
        print("================================")
        print(message)
        print("================================")

        # Prepares call/message actions for all escalation contacts.
        # Keep DEMO_MODE = True inside emergency_actions.py while testing.
        action_result = emergency_actions.prepare_emergency_action(message)
        emergency_history.add_record(
        status="CONFIRMED",
        emergency_type=emergency_type,
        risk_level=risk_level,
        risk_score=risk_score,
        reason=risk_reason,
        action_status=action_result.get("status", "UNKNOWN")
)

        print()
        print("================================")
        print("    EMERGENCY ACTION RESULT")
        print("================================")
        print("Status:", action_result.get("status"))
        print("Message:", action_result.get("message"))

        for action in action_result.get("actions", []):
            print()
            print("👤 Contact:", action.get("contact"))
            print("📞 Call:", action.get("call", {}).get("status"))
            print("📨 Message:", action.get("message", {}).get("status"))

        print("================================")

        # This is intentionally outside the contact loop.
        # It must run only once for one confirmed SOS.
        emergency.activate_emergency()

        print("🚨 Emergency system activated.")

        voice_assistance.speak_async(
            "Emergency alert confirmed. Your emergency contacts are being notified."
        )

    except Exception as error:
        print("❌ Emergency activation error:", error)

    finally:
        emergency_in_progress = False


def start_sos_activation():
    """Run emergency work in a separate thread so the UI stays responsive."""
    thread = threading.Thread(
        target=activate_sos,
        daemon=True
    )
    thread.start()


# ==========================================
# VOICE / AI CONVERSATION THREAD
# ==========================================

def conversation_loop():
    global running
    global emergency_screen
    global current_risk_level
    global current_risk_score
    global current_emergency_type
    global current_risk_reason

    while running:
        try:
            user_text = voice_assistance.listen()

            if not user_text:
                continue

            print("🎤 User:", user_text)

            # Emotion analysis
            emotion, confidence = emotion_ai.detect_emotion(user_text)

            print("😊 Emotion:", emotion)
            print("📊 Confidence:", confidence)

            eyes_mouth.set_emotion(emotion)

            # OmniAI response: called only once.
            response = omniai_brain.process(
                user_text,
                (emotion, confidence)
            )

            if response:
                print("🤖 OmniAI:", response)
                voice_assistance.speak_async(response)

            # Intent analysis
            intent = intent_ai.detect_intent(user_text)
            print("🎯 Intent:", intent)

            # Safety analysis
            risk = safety_engine.assess_risk(
                user_text,
                emotion,
                intent
            )

            emergency_type = emergency_type_ai.detect_emergency_type(
                user_text
            )

            final_safety = safety_fusion.analyze_safety(
                user_text,
                risk,
                emergency_type,
                emotion,
                intent
            )

            response_decision = emergency_response.get_response(
                final_safety["type"],
                final_safety["level"],
                final_safety["score"]
            )

            print("🛡️ FINAL RISK:", final_safety["level"])
            print("📊 FINAL SCORE:", final_safety["score"])
            print("🚨 FINAL TYPE:", final_safety["type"])
            print("⚠️ SEVERITY:", final_safety["severity"])
            print("📝 FINAL REASON:", final_safety["reason"])

            print("🤖 RESPONSE ACTION:", response_decision["action"])
            print("🚨 RESPONSE PRIORITY:", response_decision["priority"])
            print("📝 RESPONSE:", response_decision["message"])

            # Update dashboard information.
            with state_lock:
                current_risk_level = final_safety["level"]
                current_risk_score = final_safety["score"]
                current_emergency_type = final_safety["type"]
                current_risk_reason = final_safety["reason"]

            # Speak safety warning when needed.
            if response_decision["action"] != "NO_ACTION":
                voice_assistance.speak_async(
                    response_decision["message"]
                )

            # Voice emergency opens confirmation screen.
            if intent == "emergency":
                open_emergency_screen("voice")

            # Exit voice command
            exit_words = ["bye", "exit", "stop", "close", "meet again"]

            if any(word in user_text.lower() for word in exit_words):
                running = False
                break

        except Exception as error:
            print("❌ Conversation error:", error)


# ==========================================
# DRAW FUNCTIONS
# ==========================================

def draw_normal_screen():
    screen.fill(BLACK)

    eyes_mouth.draw_avatar(screen)

    pygame.draw.rect(
        screen,
        SOS_RED,
        SOS_BUTTON,
        border_radius=15
    )

    draw_centered_text("SOS", SOS_BUTTON)


def draw_emergency_screen():
    screen.fill(BLACK)

    risk_level, risk_score, emergency_type, risk_reason = get_safety_state()

    # Dashboard remains responsible for showing safety details.
    safety_dashboard.draw(
        risk_level=risk_level,
        risk_score=risk_score,
        emergency_type=emergency_type,
        reason=risk_reason,
        location=emergency_location
    )

    # pygame.draw.rect(
    #     screen,
    #     CONFIRM_GREEN,
    #     CONFIRM_BUTTON,
    #     border_radius=12
    # )

    # pygame.draw.rect(
    #     screen,
    #     CANCEL_GRAY,
    #     CANCEL_BUTTON,
    #     border_radius=12
    # )

    # draw_centered_text("CONFIRM SOS", CONFIRM_BUTTON)
    # draw_centered_text("CANCEL", CANCEL_BUTTON)

    warning_text = small_font.render(
        "Confirm only for a real emergency.",
        True,
        WHITE
    )

    screen.blit(
        warning_text,
        (
            WIDTH // 2 - warning_text.get_width() // 2,
            480
        )
    )


# ==========================================
# START APPLICATION
# ==========================================

voice_assistance.speak_async(
    "Hello Owner! Welcome to OmniAI. How can I help you today?"
)

conversation_thread = threading.Thread(
    target=conversation_loop,
    daemon=True
)

conversation_thread.start()


# ==========================================
# MAIN PYGAME LOOP
# ==========================================

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_F1:
                    print("🚨 F1 emergency shortcut pressed.")
                    open_emergency_screen("F1 shortcut")
            
                elif event.key == pygame.K_ESCAPE:
            
                    if emergency_screen:
                        print("❌ Emergency screen closed with Escape.")
                        emergency.cancel_emergency()
                        emergency_screen = False

        # event.pos is used only inside this mouse-event block.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos

            print("🖱️ Mouse clicked:", mouse_position)

            # Normal avatar screen
            if not emergency_screen:

                if SOS_BUTTON.collidepoint(mouse_position):
                    print("🚨 SOS BUTTON PRESSED")

                    triggered = silent_sos.register_click()

                    if triggered:
                        print("🤫 SILENT SOS ACTIVATED")
                        start_sos_activation()
                    else:
                        open_emergency_screen("SOS button")

            # Emergency confirmation screen
            else:

                if CONFIRM_BUTTON.collidepoint(mouse_position):
                    print("🚨 CONFIRM BUTTON CLICKED")
                    start_sos_activation()

                elif CANCEL_BUTTON.collidepoint(mouse_position):
                    print("❌ CANCEL BUTTON CLICKED")

                    emergency.cancel_emergency()
                    risk_level, risk_score, emergency_type, risk_reason = get_safety_state()
                    
                    emergency_history.add_record(
                        status="CANCELLED",
                        emergency_type=emergency_type,
                        risk_level=risk_level,
                        risk_score=risk_score,
                        reason=risk_reason,
                        action_status="CANCELLED_BY_USER"
                    )
                    emergency_screen = False

                    print("✅ SOS cancelled.")

    # Reminder check
    current_time = pygame.time.get_ticks()

    if current_time - last_reminder_check >= REMINDER_CHECK_INTERVAL:
        last_reminder_check = current_time

        try:
            due_reminders = reminder.get_due_reminders()

            for item in due_reminders:
                message = f"Owner, it's time to {item['message']}."
                print("⏰ REMINDER:", message)
                voice_assistance.speak_async(message)

        except Exception as error:
            print("❌ Reminder error:", error)

    # Draw exactly one screen each frame.
    if emergency_screen:
        draw_emergency_screen()
    else:
        draw_normal_screen()

    pygame.display.flip()
    clock.tick(60)


# ==========================================
# CLEAN SHUTDOWN
# ==========================================

pygame.quit()
sys.exit()