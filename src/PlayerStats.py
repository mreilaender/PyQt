

class PlayerStats(object):
    """
    This class ... TODO

    """
    def __init__(self, left, correct, wrong, total, games):
        self.stats = {
            "left": left,
            "correct": correct,
            "wrong": wrong,
            "total": total,
            "games": games
        }
        self.defaults = {
            "left": 0,
            "correct": 0,
            "wrong": 0,
            "total": 0,
        }

    """
    Reset all labels and increse the total number of games by 1

    """
    def reset(self):
        self.stats["left"].setText(self.defaults["left"])
        self.stats["correct"].setText(str(self.defaults["correct"]))
        self.stats["wrong"].setText(str(self.defaults["wrong"]))
        self.stats["total"].setText(str(self.defaults["total"]))
        self.stats["games"].setText(str(int(self.stats["games"].text())+1))

    def set_default_values(self, left=None, correct=None, wrong=None, total=None):
        if left is not None:
            self.defaults["left"] = left
        if correct is not None:
            self.defaults["correct"] = correct
        if wrong is not None:
            self.defaults["wrong"] = wrong
        if total is not None:
            self.defaults["total"] = total

    def decrease_left(self):
        self.stats["left"].setText(str(int(self.stats["left"].text())-1))

    def increase_correct(self):
        self.stats["correct"].setText(str(int(self.stats["correct"].text())+1))

    def increase_wrong(self):
        self.stats["wrong"].setText(str(int(self.stats["wrong"].text())+1))

    def increase_total(self):
        self.stats["total"].setText(str(int(self.stats["total"].text())+1))
