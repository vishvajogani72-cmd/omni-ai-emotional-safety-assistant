# ==========================================
# OMNIAI SILENT SOS
# ==========================================

import time


class SilentSOS:

    def __init__(self):

        self.click_times = []

        self.required_clicks = 3

        self.time_window = 2.0

    def register_click(self):

        current_time = time.time()

        # Remove clicks older than 2 seconds
        self.click_times = [
            click
            for click in self.click_times
            if current_time - click <= self.time_window
        ]

        # Add current click
        self.click_times.append(current_time)

        # Check trigger
        if len(self.click_times) >= self.required_clicks:

            self.click_times.clear()

            print("🤫 SILENT SOS TRIGGERED!")

            return True

        return False