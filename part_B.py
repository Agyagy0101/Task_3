class LEDTV():
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = "Wide"
        self.backlight = "LED"

    def display_details(self):
        return (f"LED TV - {self.brand}, {self.inches} inches, Screen Thickness: {self.screen_thickness}, "
                f"Energy Usage: {self.energy_usage}W, Lifespan: {self.lifespan} hours, Refresh Rate: {self.refresh_rate}Hz, "
                f"Viewing Angle: {self.viewing_angle}, Backlight: {self.backlight}")


class PlasmaTV():
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = "Ultra-Wide"
        self.backlight = "Plasma Gas"

    def display_details(self):
        return (f"Plasma TV - {self.brand}, {self.inches} inches, Screen Thickness: {self.screen_thickness}, "
                f"Energy Usage: {self.energy_usage}W, Lifespan: {self.lifespan} hours, Refresh Rate: {self.refresh_rate}Hz, "
                f"Viewing Angle: {self.viewing_angle}, Backlight: {self.backlight}")
