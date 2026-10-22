from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout, QVBoxLayout,
    QPushButton
)

from PyQt5.QtCore import Qt

from test_screen import TestScreen ## ПІДКЛЮЧАЄТЬСЯ ДРУГИЙ ЕКРАН

from settings import *

class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        
    def set_appear(self):
        self.resize(1280,720)
        self.setWindowTitle("Початок")



    def initUI(self):
        self.lb_text = QLabel("Ласкаво просимо до програми визначення стану здоров'я!")
        self.lb_text2 = QLabel(TEST_INFO_TEXT)
        self.btn_start = QPushButton("Почати!")

        self.v_main = QVBoxLayout()
        self.v_main.addWidget(self.lb_text, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v_main2 = QVBoxLayout()
        self.v_main2.addWidget(self.lb_text2, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v_main3 = QVBoxLayout()
        self.v_main3.addWidget(self.btn_start, alignment=Qt.AlignmentFlag.AlignBottom)
        self.v_main.addLayout(self.v_main2)
        self.v_main.addLayout(self.v_main3)

        self.setLayout(self.v_main)


    def connects(self):
        self.btn_start.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.test_screen = TestScreen()




