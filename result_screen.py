from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication

class ResultScreen(QWidget):
    def __init__(self, user_name = "user name", p1 = 0, p2 = 0, p3 = 0):
        super().__init__()

        self.user_name = user_name
        self.p1, self.p2, self.p3 = p1,p2,p3

        self.set_win()
        self.initUI()

        self.calc_index()
        self.show()


    def calc_index(self):
        

        result = (4 * (self.p1 + self.p2 + self.p3) - 200) / 10
        
        self.lbl_work.setText(f"Індекс Руф'є: {str(result)}")
    

    def set_win(self):
        self.resize(1280, 720)
        self.setWindowTitle(f"Результат для {self.user_name}")


    def initUI(self):
        self.lbl_work = QLabel("Індекс Руф'є: 0.0")
        self.lbl_index = QLabel("Тестування")
        

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lbl_index, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.lbl_work, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication([])
    t = ResultScreen()
    app.exec()