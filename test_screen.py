from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout, QVBoxLayout,
    QPushButton
)

from PyQt5.QtCore import Qt

from settings import *

class TestScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        
    def set_appear(self):
        self.resize(1280,720)
        self.setWindowTitle("Тестування")



    def initUI(self):
       pass
        


    def connects(self):
        pass

    def click_next(self):
        pass






