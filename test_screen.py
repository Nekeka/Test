from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout, QVBoxLayout,
    QPushButton
)

from PyQt5.QtCore import Qt




class TestScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.set_appear()
        self.initUI()

        self.show()
        
    def set_appear(self):
        self.resize(1280,720)
        self.setWindowTitle("Тест")



    def initUI(self):
        self.lb_text = QLabel("ТЕСТ")
        self.v_main = QVBoxLayout()
        self.v_main.addWidget(self.lb_text)

        self.setLayout(self.v_main)





