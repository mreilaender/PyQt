

class CheckOrder(object):
    def __init__(self, start_value):
        self.start_value = start_value
        self.counter = None
        self.reset()

    def check_order(self, act):
        """
        bla

        :param act: Value that has been clicked
        """
        if act == self.counter:
            return True
        return False

    def reset(self):
        self.counter = self.start_value

    def increment(self):
        self.counter += 1
