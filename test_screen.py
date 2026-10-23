from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QLineEdit,
    QApplication,
)

from PyQt5.QtCore import Qt, QTimer




class TestScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        
    def set_appear(self):
        self.resize(800,600)
        self.setWindowTitle("Тест")



    def initUI(self):
        self.counter = 3

        self.lb_name = QLabel("ПІБ")
        self.lb_timer = QLabel(str(self.counter))

        self.le_name = QLineEdit()
        
        self.btn_first_test = QPushButton("Почати перший тест")
        self.timer = QTimer(self)

        self.v_main = QVBoxLayout()
        self.v_main.addWidget(self.lb_name,alignment=Qt.AlignmentFlag.AlignLeft)
        self.v_main.addWidget(self.le_name,alignment=Qt.AlignmentFlag.AlignLeft)
        self.v_main.addWidget(self.btn_first_test, alignment=Qt.AlignmentFlag.AlignLeft)
        self.v_main.addWidget(self.lb_timer)

        self.setLayout(self.v_main)


    def connects(self):
        self.btn_first_test.clicked.connect(self.start_timer)
        self.timer.timeout.connect(self.update_counter)
        

    def start_timer(self):
        self.timer.start(1000)

    def update_counter(self):
        self.counter -= 1
        self.lb_timer.setText(str(self.counter))

        if self.counter <= 0:
            self.timer.stop()




a = QApplication([])

w = TestScreen()

a.exec()

