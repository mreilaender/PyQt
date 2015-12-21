from src.CheckOrder import CheckOrder
from src.PlayerStats import PlayerStats


class Model(object):
    """
    MVC - Pattern: Represents the model class

    """
    def __init__(self):
        self.check = CheckOrder(1)
        self.stats = None

    def on_button_pressed(self, button):
        # if self.check.check_order(1):
        #     return False
        if self.stats is None:
            print("Labens not set")
            return False
        else:
            if self.check.check_order(int(button.text())):
                print(self.stats.stats["left"])
                self.stats.decrease_left()
                self.check.increment()

    def set_labels(self, left, correct, wrong, total, games):
        self.stats = PlayerStats(left, correct, wrong, total, games)
