import sys
from src.view import Ui_view
from src.model import Model

from PyQt5.QtWidgets import *


class Controller(QWidget):
    """
    MVC Pattern: Represents the controller class

    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.view = Ui_view()
        self.tmp = QMainWindow()
        self.model = Model()

        self.view.setupUi(self.tmp)
        self.setup_signals()
        self.model.set_labels(self.view.left_value, self.view.correct_value, self.view.wrong_value,
                              self.view.total_value, self.view.games_value)

    def setup_signals(self):
        self.view.pushButton.clicked.connect(lambda: self.model.on_button_pressed(self.view.pushButton))
        self.view.pushButton_2.clicked.connect(lambda: self.model.on_button_pressed(self.view.pushButton_2))
        self.view.pushButton_3.clicked.connect(lambda: self.model.on_button_pressed(self.view.pushButton_3))
        self.view.pushButton_4.clicked.connect(lambda: self.model.on_button_pressed(self.view.pushButton_4))
        self.view.pushButton_5.clicked.connect(lambda: self.model.on_button_pressed(self.view.pushButton_5))
        self.view.pushButton_6.clicked.connect(lambda: self.model.on_button_pressed(self.view.pushButton_6))
        self.view.pushButton_7.clicked.connect(lambda: self.model.on_button_pressed(self.view.pushButton_7))
        self.view.pushButton_8.clicked.connect(lambda: self.model.on_button_pressed(self.view.pushButton_8))
        self.view.pushButton_9.clicked.connect(lambda: self.model.on_button_pressed(self.view.pushButton_9))
        self.view.pushButton_10.clicked.connect(lambda: self.model.on_button_pressed(self.view.pushButton_10))
        self.view.pushButton_11.clicked.connect(lambda: self.model.on_button_pressed(self.view.pushButton_11))
        self.view.pushButton_12.clicked.connect(lambda: self.model.on_button_pressed(self.view.pushButton_12))
        self.view.pushButton_13.clicked.connect(lambda: self.model.on_button_pressed(self.view.pushButton_13))
        self.view.pushButton_14.clicked.connect(lambda: self.model.on_button_pressed(self.view.pushButton_14))
        self.view.pushButton_15.clicked.connect(lambda: self.model.on_button_pressed(self.view.pushButton_15))

app = QApplication(sys.argv)
controller = Controller()
controller.tmp.show()
sys.exit(app.exec_())
