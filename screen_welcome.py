from PyQt5.QtWidgets import (
    QLabel, 
    QApplication,                   #QApplication 
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout
)
from PyQt5.QtCore import Qt
from settings import *

app = QApplication([])

class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.setWindowTitle("Здоров'я")

        self.initUi()
        self.show()

    def initUi(self):
        '''cтворення віджетів'''
        self.label_hello = QLabel("Ласкаво просимо до програми визначення здоров'я")
        self.label_info = QLabel(TEST_INFO_TEXT)
        self.btn_start = QPushButton("Почати")

        self.h_1 = QHBoxLayout()
        self.h_2 = QHBoxLayout()
        self.h_3 = QHBoxLayout()

        self.v_main = QVBoxLayout()
        # 3 розміщення віджетів по лініях

        self.h_1.addWidget(self.label_info)
        self.h_2.addWidget(self.label_hello)
        self.h_3.addWidget(self.btn_start, alignment= Qt.AlignmentFlag.AlignCenter)


        self.v_main.addLayout(self.h_2)
        self.v_main.addLayout(self.h_1)
        self.v_main.addLayout(self.h_3)

        # 4 розміщення лінії у вікні

        self.setLayout(self.v_main)





welcome_screen =  WelcomeScreen()

app.exec()