import pygame


class SafetyDashboard:

    def __init__(self, screen):

        self.screen = screen

        self.width = screen.get_width()
        self.height = screen.get_height()

        # Fonts
        self.title_font = pygame.font.Font(None, 42)
        self.label_font = pygame.font.Font(None, 30)
        self.value_font = pygame.font.Font(None, 30)
        self.button_font = pygame.font.Font(None, 28)

        # Buttons
        self.confirm_button = pygame.Rect(
            200, 500, 220, 60
        )

        self.cancel_button = pygame.Rect(
            480, 500, 220, 60
        )

    def draw(
        self,
        risk_level="CRITICAL",
        risk_score=100,
        emergency_type="GENERAL_EMERGENCY",
        reason="Emergency detected",
        location=None
    ):

        # ======================================
        # BACKGROUND
        # ======================================

        self.screen.fill((10, 12, 18))

        # ======================================
        # TITLE
        # ======================================

        title = self.title_font.render(
            "🚨 OMNIAI SAFETY ALERT",
            True,
            (255, 255, 255)
        )

        self.screen.blit(
            title,
            (
                self.width // 2 - title.get_width() // 2,
                40
            )
        )

        # ======================================
        # RISK LEVEL
        # ======================================

        risk_text = self.label_font.render(
            f"RISK LEVEL: {risk_level}",
            True,
            (255, 80, 80)
        )

        self.screen.blit(
            risk_text,
            (100, 120)
        )

        # ======================================
        # RISK SCORE
        # ======================================

        score_text = self.value_font.render(
            f"RISK SCORE: {risk_score}/100",
            True,
            (255, 220, 80)
        )

        self.screen.blit(
            score_text,
            (100, 165)
        )

        # ======================================
        # EMERGENCY TYPE
        # ======================================

        emergency_text = self.value_font.render(
            f"TYPE: {emergency_type}",
            True,
            (255, 255, 255)
        )

        self.screen.blit(
            emergency_text,
            (100, 210)
        )

        # ======================================
        # REASON
        # ======================================

        reason_text = self.label_font.render(
            "REASON:",
            True,
            (200, 200, 200)
        )

        self.screen.blit(
            reason_text,
            (100, 260)
        )

        reason_value = self.value_font.render(
            str(reason)[:55],
            True,
            (255, 255, 255)
        )

        self.screen.blit(
            reason_value,
            (100, 295)
        )

        # ======================================
        # LOCATION
        # ======================================

        location_title = self.label_font.render(
            "📍 LOCATION:",
            True,
            (100, 220, 255)
        )

        self.screen.blit(
            location_title,
            (500, 120)
        )

        if location:

            latitude = location.get(
                "latitude",
                "Unknown"
            )

            longitude = location.get(
                "longitude",
                "Unknown"
            )

            lat_text = self.value_font.render(
                f"Latitude: {latitude}",
                True,
                (255, 255, 255)
            )

            lon_text = self.value_font.render(
                f"Longitude: {longitude}",
                True,
                (255, 255, 255)
            )

            self.screen.blit(
                lat_text,
                (500, 165)
            )

            self.screen.blit(
                lon_text,
                (500, 205)
            )

        else:

            no_location = self.value_font.render(
                "Location unavailable",
                True,
                (255, 150, 150)
            )

            self.screen.blit(
                no_location,
                (500, 165)
            )

        # ======================================
        # CONFIRM BUTTON
        # ======================================

        pygame.draw.rect(
            self.screen,
            (180, 30, 30),
            self.confirm_button,
            border_radius=12
        )

        confirm_text = self.button_font.render(
            "CONFIRM SOS",
            True,
            (255, 255, 255)
        )

        self.screen.blit(
            confirm_text,
            (
                self.confirm_button.centerx
                - confirm_text.get_width() // 2,

                self.confirm_button.centery
                - confirm_text.get_height() // 2
            )
        )

        # ======================================
        # CANCEL BUTTON
        # ======================================

        pygame.draw.rect(
            self.screen,
            (60, 60, 70),
            self.cancel_button,
            border_radius=12
        )

        cancel_text = self.button_font.render(
            "CANCEL",
            True,
            (255, 255, 255)
        )

        self.screen.blit(
            cancel_text,
            (
                self.cancel_button.centerx
                - cancel_text.get_width() // 2,

                self.cancel_button.centery
                - cancel_text.get_height() // 2
            )
        )

    def handle_click(self, position):

        if self.confirm_button.collidepoint(position):

            return "confirm"

        if self.cancel_button.collidepoint(position):

            return "cancel"

        return None