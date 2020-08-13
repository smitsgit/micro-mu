import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello World')
        button = QPushButton("Push me")
        self.setFixedSize(QSize(200, 200))
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
