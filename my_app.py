from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from instr import*
from texts import*


class start_win(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(win_text)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        v_line = QVBoxLayout()
        self.label = QLabel(hello_text)
        self.button = QPushButton(start_text)
        self.setLayout(v_line)
        v_line.addWidget(self.label)
        v_line.addWidget(self.button)
    def next_click(self):
        self.hide()
        piska()
    def connects(self):
        self.button.clicked.connect(self.next_click)

app = QApplication([])
window_1 = start_win()
app.exec_()