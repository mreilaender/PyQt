

class ButtonHandler(object):
    def __init__(self):
        self.buttons = {}

    def add_button(self, button):
        self.buttons[button.text()] = button

    def reset(self):
        for name in self.buttons:
            self.buttons[name].setEnabled(True)
        self.buttons = {}
