from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton

app = QApplication([])
window = QWidget()

window.resize(500,500)

window.show()
app.exec()