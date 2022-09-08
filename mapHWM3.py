import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, QButtonGroup
from PyQt6.QtGui import QPalette, QColor
from PyQt6 import QtCore

a = ["Ungovernable Steppe", "Eagle Nest", "Peaceful Camp", "Crystal Garden", "Fairy Trees", "-", "Sunny City", "Shining Spring", "Tiger Lake", "Rogues' Wood", "Bear Mountain", "Mithril Coast", "Sublime Arbor", "Green Wood", "Empire Capital", "East River", "Magma Mines", "Harbor City", "-", "Lizard Lowland", "Wolf Dale", "Dradons' Caves", "-", "-", "-", "The Wilderness", "Portal Ruins", "Great Wall", "-", "-", "-", "-", "-", "Titans' Valley", "Fishing village", "-", "-", "-", "-", "-", "Kindow Castle", "-"]
N = 7
M = 6
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        
        layout = QGridLayout()
        self.buttons = [[0, 0], [0, 0], [0, 0]]
        self.buttons = [[0 for i in range(6)] for j in range(7)]
        self.buttonGroup = QButtonGroup(self)

        for i in range(N):
            for j in range(M):
                self.buttons[i][j] = QPushButton(a[M * i + j])
                self.buttons[i][j].setCheckable(True)
                self.buttons[i][j].setStyleSheet("QPushButton {background-color: rgb(151,122,183); color: White; border-radius: 600px;}")
                self.buttons[i][j].clicked.connect(self.set_color_button)
                self.buttons[i][j].setMinimumSize(QtCore.QSize(150, 100))
                self.buttons[i][j].setMaximumSize(QtCore.QSize(150, 100))
                self.buttonGroup.addButton(self.buttons[i][j])
                layout.addWidget(self.buttons[i][j], i, j)

        self.buttonGroup.buttonClicked.connect(self.turn_off_buttons)
        # for w in self.buttons:
        #     for ww in w:
        #         ww.clicked.connect(self.turn_off_buttons)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def set_color_button(self, checked):
        print(checked)
        if checked == True:
            self.sender().setStyleSheet("QPushButton {background-color: rgb(251,122,183); color: White; border-radius: 600px;}")
        else:
            self.sender().setStyleSheet("QPushButton {background-color: rgb(151,122,183); color: White; border-radius: 600px;}")

    def turn_off_buttons(self, button):
        colorr = str(button.palette().button().color().name())
        print(colorr)
        n = a.index(str(button.text()))
        i = n//M
        j = n - n//M*M
        if str(button.text()) == "-":
             i, j = -1, -1
        for ii in range(N):
            for jj in range(M):
                if ii == i and jj == j:
                    pass
                else:
                    self.buttons[ii][jj].setChecked(False)
                    self.buttons[ii][jj].setStyleSheet("QPushButton {background-color: rgb(151,122,183); color: White; border-radius: 600px;}")

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class Button(QPushButton):
    
    def __init__(self, text):
        super(Button, self).__init__()
        self.setText(text)
        self.setCheckable(True)
        self.setStyleSheet("QPushButton {background-color: rgb(151,122,183); color: White; border-radius: 600px;}")
        self.clicked.connect(self.set_color_button)
        self.setMinimumSize(QtCore.QSize(150, 100))
        self.setMaximumSize(QtCore.QSize(150, 100))

    def set_color_button(self, checked):
        if checked == True:
            self.setStyleSheet("QPushButton {background-color: rgb(251,122,183); color: White; border-radius: 600px;}")
        else:
            self.setStyleSheet("QPushButton {background-color: rgb(151,122,183); color: White; border-radius: 600px;}")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()