import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, QLabel, QVBoxLayout, QStackedLayout
from PyQt6.QtGui import QPalette, QColor, QPixmap, QIcon
from PyQt6 import QtCore

a = ["Ungovernable Steppe", "Eagle Nest", "Peaceful Camp", "Crystal Garden", "Fairy Trees", "-", "Sunny City", "Shining Spring", "Tiger Lake", "Rogues' Wood", "Bear Mountain", "Mithril Coast", "Sublime Arbor", "Green Wood", "Empire Capital", "East River", "Magma Mines", "Harbor City", "-", "Lizard Lowland", "Wolf Dale", "Dradons' Caves", "-", "-", "-", "The Wilderness", "Portal Ruins", "Great Wall", "-", "-", "-", "-", "-", "Titans' Valley", "Fishing village", "-", "-", "-", "-", "-", "Kindow Castle", "-"]
N = 7
M = 6
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout1 = QHBoxLayout()

        layout = QGridLayout()
        #layout.setVerticalSpacing(0)
        self.buttons = [[0, 0], [0, 0], [0, 0]]
        self.buttons = [[0 for i in range(M)] for j in range(N)]
        for i in range(N):
            for j in range(M):
                self.buttons[i][j] = QPushButton(a[M * i + j])
                self.buttons[i][j].setCheckable(True)
                self.buttons[i][j].setStyleSheet("QPushButton {background-color: rgb(151,122,183); color: White; border-radius: 600px;}")
                self.buttons[i][j].clicked.connect(self.set_color_button)
                self.buttons[i][j].setMinimumSize(QtCore.QSize(150, 100))
                self.buttons[i][j].setMaximumSize(QtCore.QSize(150, 100))
                layout.addWidget(self.buttons[i][j], i, j)

        self.text_sector = QLabel();
        self.text_sector.setStyleSheet("QLabel {background-color: rgb(255,255,255); font-size: 26px}")
        self.text_sector.setStyleSheet("QLabel {font-size: 28px; color: #b07d2b; font-family: Times, serif; position: relative; text-transform: uppercase; font-size: 9vw; letter-spacing: 1vw; line-height: 1; font-weight: 300;}")
        layout.addWidget(self.text_sector, N+1, 0, -1, -1)
        #layout.setVerticalSpacing(0)
        #layout.setSpacing(0)
        layout.setColumnStretch(5)
        layout.setFixedSize(QSize(200, 200))
        

        for w in self.buttons:
            for ww in w:
                ww.clicked.connect(self.turn_off_buttons)


        button_layout = QHBoxLayout()
        self.buttons_fractions = [0 for i in range(10)]
        for i in range(10):
            self.buttons_fractions[i] = QPushButton()
            self.buttons_fractions[i].setIcon(QIcon(f'images/HWMfractions/r{i + 1}'))
            button_layout.addWidget(self.buttons_fractions[i])
        

        for w in self.buttons_fractions:
            w.clicked.connect(self.active_kukla)

        self.stacklayout = QStackedLayout()
        for i in range(10):
            image_sector = QLabel("q");
            mpixmap = QPixmap(f'images/HWMkukla/kukla{i + 1}.png')
            image_sector.setPixmap(mpixmap)
            #image_sector.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
            self.stacklayout.addWidget(image_sector)

        self.stacklayout.setCurrentIndex(1)

        layout_right = QVBoxLayout()

        layout_right.addLayout(button_layout)
        layout_right.addLayout(self.stacklayout)

        layout1.addLayout(layout)
        layout1.addLayout(layout_right)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

    def set_color_button(self, checked):
        print(checked)
        if checked == True:
            self.text_sector.setText(self.sender().text())
            self.sender().setStyleSheet("QPushButton {background-color: rgb(251,122,183); color: White; border-radius: 600px;}")
        else:
            self.text_sector.setText("")
            self.sender().setStyleSheet("QPushButton {background-color: rgb(151,122,183); color: White; border-radius: 600px;}")

    def turn_off_buttons(self):
        n = a.index(str(self.sender().text()))
        i = n//M
        j = n - n//M*M
        if str(self.sender().text()) == "-":
             i, j = -1, -1
        for ii in range(N):
            for jj in range(M):
                if ii == i and jj == j:
                    pass
                else:
                    self.buttons[ii][jj].setChecked(False)
                    self.buttons[ii][jj].setStyleSheet("QPushButton {background-color: rgb(151,122,183); color: White; border-radius: 600px;}")


    def active_kukla(self):
        n = self.buttons_fractions.index(self.sender())
        self.stacklayout.setCurrentIndex(n)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()