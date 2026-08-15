import pygame
from safety_dashboard import SafetyDashboard


pygame.init()

screen = pygame.display.set_mode(
    (900, 600)
)

pygame.display.set_caption(
    "OmniAI Safety Dashboard Test"
)

dashboard = SafetyDashboard(screen)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            result = dashboard.handle_click(
                event.pos
            )

            if result == "confirm":

                print("🚨 CONFIRM SOS CLICKED")

            elif result == "cancel":

                print("✅ CANCEL CLICKED")

    dashboard.draw(
        risk_level="CRITICAL",
        risk_score=100,
        emergency_type="FOLLOWING",
        reason="Someone is following me",
        location={
            "latitude": 23.0225,
            "longitude": 72.5714
        }
    )

    pygame.display.flip()


pygame.quit()