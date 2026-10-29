from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QLineEdit,
    QApplication,
)

from PyQt5.QtCore import Qt, QTimer

from settings import *


class TestScreen(QWidget):
    def __init__(self):
            super().__init__()


            self.counter = TIMER_FOR_FIRST_TEST # рахунок
            self.timer = QTimer(self)
    
            self.set_appear()

            self.initUI()

            self.connects()
    


            self.show()
    
            
    def set_appear(self):
        self.resize(720,720)
        self.setWindowTitle("Тестування")



    def initUI(self):

        self.lb_timer = QLabel(f"Залишилось секунд: {str(self.counter)}")
        self.lb_timer.setStyleSheet("font-size: 45px;") # НАКЛАСТИ СТИЛІ

        lb_name = QLabel("введіть ПІБ")
        le_name = QLineEdit()
        le_name.setPlaceholderText("ПІБ")

        lb_age = QLabel("Повних років:")
        le_age = QLineEdit()
        le_age.setPlaceholderText("введіть вік (число)")

        self.btn_start_first_test = QPushButton("Почати перший тест")
  

        V_main = QVBoxLayout()

        h_row1 = QHBoxLayout()
        h_row2 = QHBoxLayout()
        h_upper = QHBoxLayout()

        h_upper.addWidget(self.lb_timer, alignment = Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop )



        h_row1.addWidget(lb_name)
        h_row1.addWidget(le_name)

        h_row2.addWidget(lb_age)
        h_row2.addWidget(le_age)

        V_main.addLayout(h_upper)
        V_main.addLayout(h_row1)
        V_main.addLayout(h_row2)
        V_main.addWidget(self.btn_start_first_test)


        self.setLayout(V_main)
       

    def connects(self):
        self.btn_start_first_test.clicked.connect(self.start_timer)
        self.timer.timeout.connect(self.update_counter)

    def next_click(self):
        self.hide()
   
    def start_timer(self):
        self.timer.start(1000)
        

    def update_counter(self):
       self.counter -= 1
       self.lb_timer.setText(f"Залишилось секунд: {str(self.counter)}"  )

       if self.counter <= 0:
           self.timer.stop()
    



from PyQt5.QtWidgets import QApplication


app = QApplication([])



test_screen = TestScreen()



app.exec()