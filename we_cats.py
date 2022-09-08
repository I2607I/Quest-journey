import sys
from turtle import showturtle
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QVBoxLayout, QWidget, QPushButton
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

from random import choice
from random import randint

we = ["Это ты", "Это я", "Это ти", "Это я"]
cats1 = ["cat1", "cat2", "cat3", "cat4", "cat5", "cat6", "cat7", "cat8", "tigr", "pantera"]
cats2 = ["cats1", "cats2", "cats3", "cats4", "cats5", "cats6", "cats7", "cats8", "cats9", "cats10"]

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Igor and Liza")

        button = QPushButton("press me")
        button.clicked.connect(self.set_image)


        self.widget = QLabel("Hello")
        self.widget.setText("Hello, world")
        font = self.widget.font()
        font.setPointSize(30)
        self.widget.setFont(font)
        self.widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.widget2 = QLabel()
        mpixmap = QPixmap('cat.jpg')
        self.widget2.setPixmap(mpixmap)
        self.widget2.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.widget)
        layout.addWidget(self.widget2)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def set_image(self):
        if randint(0,1) == 0:
            showText = choice(cats1)
            if showText == "pantera":
                self.widget.setText("Это ты")
            elif showText == "tigr":
                self.widget.setText("Это я")
            else:
                self.widget.setText(choice(we))
            self.widget2.setPixmap(QPixmap("images/one/"+showText+".jpg"))
        else:
            self.widget.setText("Это мы")
            self.widget2.setPixmap(QPixmap("images/two/"+choice(cats2)+".jpg"))





app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()