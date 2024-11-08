
#PyQt5 Introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont

# from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('thisbelarry GUI with PY')
        self.setGeometry(700, 300, 500, 500)
        # set.setWindowIcon(QIcon("myicon.png"))

        label = QLabel("Hello",self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(10, 10, 500, 500)
        label.setStyleSheet("background-color: rgb(255, 255, 255);"
                            "color:blue")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()




























































































































































