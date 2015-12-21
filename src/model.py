from src.ButtonHandler import ButtonHandler
from src.CheckOrder import CheckOrder
from src.PlayerStats import PlayerStats


class Model(object):
    """
    MVC - Pattern: Represents the model class

    """
    def __init__(self):
        self.check = CheckOrder(1)
        self.stats = None
        self.buttons = ButtonHandler()

    def on_button_pressed(self, button):
        # if self.check.check_order(1):
        #     return False
        if self.stats is None:
            print("Labels not set")
            return False
        else:
            self.stats.increase_total()
            if self.check.check_order(int(button.text())):
                self.stats.increase_correct()
                self.stats.decrease_left()
                button.setEnabled(False)
                self.buttons.add_button(button)
                self.check.increment()
            else:
                self.stats.increase_wrong()

    def set_labels(self, left, correct, wrong, total, games):
        self.stats = PlayerStats(left, correct, wrong, total, games)

    def set_default_values(self, left=None, correct=None, wrong=None, total=None):
        self.stats.set_default_values(left, correct, wrong, total)

    def reset(self):
        self.stats.reset()
        self.buttons.reset()
        self.check.reset()
