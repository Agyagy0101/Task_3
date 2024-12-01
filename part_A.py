class TV:
    def __init__(self, brand, price, inches):
        self.brand = brand
        self.channel = 1
        self.volume = 50
        self.price = price
        self.inches = inches
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} TV is now ON")

    def turn_off(self):
        self.is_on = False
        print(f"{self.brand} TV is now OFF")

    def increase_volume(self):
        if self.is_on:
            if self.volume < 100:
                self.volume += 1
                print(f"Volume increased to {self.volume}")
            else:
                print("Volume is already at maximum")
        else:
            print("TV is OFF")

    def decrease_volume(self):
        if self.is_on:
            if self.volume > 0:
                self.volume -= 1
                print(f"Volume decreased to {self.volume}")
            else:
                print("Volume is already at minimum")
        else:
            print("TV is OFF")

    def set_channel(self, new_channel):
        if self.is_on:
            if 1 <= new_channel <= 50:
                self.channel = new_channel
                print(f"Channel set to {self.channel}")
            else:
                print("Invalid channel. TV stays at current channel.")
        else:
            print("TV is OFF")

    def reset(self):
        self.channel = 1
        self.volume = 50
        print(f"TV reset: Channel {self.channel}, Volume {self.volume}")

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}, ON: {self.is_on}"
    

    #part B

    class LEDTV(TV):
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


class PlasmaTV(TV):
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

