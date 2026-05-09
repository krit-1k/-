from time import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

class TimerApp(QWidget):
    def __init__(self, cek_time):
        super().__init__()
        self.counter = cek_time  # Начальное значение
        self.initUI()

    def initUI(self):
        self.label = QLabel(str(self.counter), self)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Настройка таймера
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)  # Срабатывает каждые 1000 мс (1 сек)

        self.show()

    def showTime(self):
        self.counter -= 1
        if self.counter >= 0:
            self.label.setText(str(self.counter))
        else:
            self.timer.stop()
            self.label.setText("Время вышло!")

def start_chet():
    ex = TimerApp(15)

stage1_button = QPushButton
stage1_button.clicked.connect(start_chet)

app = QApplication(sys.argv)

sys.exit(app.exec_())