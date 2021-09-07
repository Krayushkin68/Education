import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class LabelTimer:
    def __init__(self, label_obj):
        # label
        self.label_obj = label_obj
        # label parent
        self.parent = self.label_obj.parent()

        # example data to show
        self.data = ["one", "two", "three", "four", "five", "six", "seven", "eight"]
        self.counter = 0

        # timer creation, init with label parent
        timer = QTimer(self.parent)
        timer.timeout.connect(self.on_timeout)
        timer.start(1000)

    def on_timeout(self):
        # function, executed by timer timeout
        if self.counter >= len(self.data):
            self.counter = 0

        self.label_obj.setText(str(self.data[self.counter]))
        self.counter += 1


class MyWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(150, 100)
        self.wordLabel = QLabel(self)
        self.wordLabel.setStyleSheet('font-size: 18pt; color: blue;')
        self.wordLabel.setText('Start Text')

        self.wordLabel2 = QLabel(self)
        self.wordLabel2.setStyleSheet('font-size: 18pt; color: blue;')
        self.wordLabel2.setText('Entry Text')

        # creating class object
        self.timer = LabelTimer(self.wordLabel)
        self.timer2 = LabelTimer(self.wordLabel2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWin()
    w.show()
    sys.exit(app.exec())
