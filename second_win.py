# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QButtonGroup

app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle('Очередной тест?')

class Test1(Qwidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connets()
        self.show()