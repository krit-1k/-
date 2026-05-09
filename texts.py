from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from instr import*

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Тест руфье")

text1 = QLabel(T_text1)
text2 = QLabel(T_text2)
text3 = QLabel(T_text3)
text4= QLabel(T_text4)
text5= QLabel(T_text5)

but1 = QPushButton('начать первый тест')
but2 = QPushButton('Начать делать приседания')
but3 = QPushButton("начать финальный тест")
but4 = QPushButton('отправить результаты')

wr1 = QLineEdit('')
wr2 = QLineEdit('')
wr3 = QLineEdit('')
wr4 = QLineEdit('')
wr5 = QLineEdit('')

Vmain = QHBoxLayout()
H1 = QVBoxLayout()
H2 =QVBoxLayout()

Vmain.addLayout(H1)
Vmain.addLayout(H2)
H1.addWidget(text1, alignment=Qt.AlignLeft)
H1.addWidget(wr1, alignment=Qt.AlignLeft)
H1.addWidget(text2, alignment=Qt.AlignLeft)
H1.addWidget(wr2, alignment=Qt.AlignLeft)
H1.addWidget(text3, alignment=Qt.AlignLeft)
H1.addWidget(but1, alignment=Qt.AlignLeft)
H1.addWidget(wr3, alignment=Qt.AlignLeft)
H1.addWidget(text4, alignment=Qt.AlignLeft)
H1.addWidget(but2, alignment=Qt.AlignLeft)
H1.addWidget(text5, alignment=Qt.AlignLeft)
H1.addWidget(but3, alignment=Qt.AlignLeft)
H1.addWidget(wr4, alignment=Qt.AlignLeft)
H1.addWidget(wr5, alignment=Qt.AlignLeft)
H1.addWidget(but4, alignment=Qt.AlignCenter)

var1 = wr1.text()
var2 = wr2.text()
var3 = wr3.text()
var4 = wr4.text()
var5 = wr5.text()

main_win.setLayout(Vmain)
main_win.show()
app.exec_()



















