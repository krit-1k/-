from texts import text1, text2, text3, text4, text5
from PyQt5.Widgets import QWidget

class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appeаг()
        self.initUI() 
        self.connects() 
        self.show() 
    def initUI(self):
        self.wr1 = QLineEdit('')
        self.wr2 = QLineEdit('')
        self.wr3 = QLineEdit('')
        self.wr4 = QLineEdit('')
        self.wr5 = QLineEdit('')
    def set_appear(self):
        self.setWindowTitle(win_text)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)





        
        self.Vmain = QHBoxLayout()
        self.H1 = QVBoxLayout()
        self.H2 =QVBoxLayout()
        