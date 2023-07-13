from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton

app = QApplication([])
window = QWidget()

window.resize(500,500)

button1 = QPushButton('1')
button2 = QPushButton('2')
button3 = QPushButton('3')
button4 = QPushButton('4')
button5 = QPushButton('5')

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
lineV = QVBoxLayout()

line1.addWidget(button1, alignment=Qt.AlignLeft)
line1.addWidget(button2, alignment=Qt.AlignRight)
line2.addWidget(button3, alignment=Qt.AlignCenter)
line3.addWidget(button4, alignment=Qt.AlignLeft)
line3.addWidget(button5, alignment=Qt.AlignRight)

lineV.addLayout(line1)
lineV.addLayout(line2)
lineV.addLayout(line3)

window.setLayout(lineV)

window.show()
app.exec()
