

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

    """
    Reset all labels and increse the total number of games by 1

    """
    def reset(self):
        self.stats["left"].setText("0")
        self.stats["correct"].setText("0")
        self.stats["wrong"].setText("0")
        self.stats["total"].setText("0")
        self.stats["games"].setText(str(int(self.stats["games"].text())+1))

    def decrease_left(self):
        self.stats["left"].setText(str(int(self.stats["left"].text())-1))
