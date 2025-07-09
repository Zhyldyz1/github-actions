# app/main.py

class ColorToggler:
    def __init__(self):
        self.current_color = "red" # Initial state

    def click(self):
        """Simulates a click, toggling the color."""
        if self.current_color == "red":
            self.current_color = "green"
            print("Color changed to GREEN")
        else:
            self.current_color = "red"
            print("Color changed to RED")
        return self.current_color

if __name__ == "__main__":
    # Simulate a few clicks for demonstration in the workflow logs
    toggler = ColorToggler()
    print(f"Initial color: {toggler.current_color}")
    toggler.click() # First click: red -> green
    toggler.click() # Second click: green -> red
    toggler.click() # Third click: red -> green
