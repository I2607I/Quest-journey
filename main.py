import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, QLabel, QVBoxLayout, QStackedLayout
from PyQt6.QtGui import QPalette, QColor, QPixmap, QIcon, QCursor, QPainter, QFont, QPolygonF
from PyQt6 import QtCore
from PyQt6.QtMultimedia import QSoundEffect
from random import randint


a = []
N = 10
M = 10

class MainWidget(QWidget):
    def __init__(self, backcol, characters, coordinates, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sky_image = QPixmap(f'images/sky.png').scaled(750, 225)

        layout = QGridLayout()
        self.buttons = [[0 for i in range(M)] for j in range(N)]
        for i in range(N):
            for j in range(M):
                self.buttons[i][j] = QPushButton()
                self.buttons[i][j].setStyleSheet(f'background-color: rgb{backcol[i]}; color: White; border-radius: 600px;')
                self.buttons[i][j].setMinimumSize(QtCore.QSize(100, 67))
                self.buttons[i][j].setMaximumSize(QtCore.QSize(100, 67))
                a.append(self.buttons[i][j])
                layout.addWidget(self.buttons[i][j], i+1, j)
        
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.characters = characters
        self.coordinates1 = coordinates
        self.sound_characters1 = {}

        # звуки основные
        for item in self.characters:
            mass = []
            files = os.listdir(path=f'sounds/characters/{item}')
            for j in range(len(files)):
                current_sound = QSoundEffect()
                current_sound.setSource(QtCore.QUrl.fromLocalFile(f'sounds/characters/{item}/{j+1}.wav'))
                mass.append(current_sound)
            self.sound_characters1[item] = mass

        # установка картинок и вызов сигнала
        for item in self.characters:
            coor = self.coordinates1[item]
            self.buttons[coor[0]][coor[1]].setIcon(QIcon(f'images/{item}.png'))
            self.buttons[coor[0]][coor[1]].setIconSize(QtCore.QSize(100, 67))
            self.buttons[coor[0]][coor[1]].setObjectName(item)
            self.buttons[coor[0]][coor[1]].clicked.connect(self.play_sound_characters) 
        
        # курсор для дома
        # cur = QPixmap('images/curhouse.png').scaledToWidth(30)
        # self.buttons[self.coordinates1["house"][0]][self.coordinates1["house"][1]].setCursor(QCursor(cur))

        # флаги еды
        self.flag_eat = 0
        self.pig_eat = 0
        self.crabHands = True
        self.snowmanHands = True

        # звуки дополнительные
        self.sound_go = QSoundEffect()
        self.sound_go.setSource(QtCore.QUrl.fromLocalFile(f'sounds/characters/go.wav'))
        self.sound_money = QSoundEffect()
        self.sound_money.setSource(QtCore.QUrl.fromLocalFile(f'sounds/characters/money.wav'))
        self.sound_delicious = []
        self.sound_delicious.append(QSoundEffect())
        self.sound_delicious.append(QSoundEffect())
        self.sound_delicious.append(QSoundEffect())
        self.sound_delicious[0].setSource(QtCore.QUrl.fromLocalFile(f'sounds/characters/delicious1.wav'))
        self.sound_delicious[1].setSource(QtCore.QUrl.fromLocalFile(f'sounds/characters/delicious2.wav'))
        self.sound_delicious[2].setSource(QtCore.QUrl.fromLocalFile(f'sounds/characters/delicious3.wav'))

        self.setLayout(layout)

    def play_sound_characters(self):
        ob = self.sender().objectName()
        print(ob)
        if self.flag_eat == 1 and ob=="Liza":
            self.sound_go.play()
        elif (self.flag_eat == 2 or self.flag_eat == 3 or self.flag_eat == 4) and ob=="Liza":
            m = randint(0, len(self.sound_delicious) - 1)
            self.sound_delicious[m].play()
        elif ob=="pig" and self.flag_eat != 0:
            self.pig_eat +=1
            if self.pig_eat >= 5:
                self.buttons[self.coordinates1[ob][0]][self.coordinates1[ob][1]].setIcon(QIcon(f'images/pig2.png'))
                self.pig_eat = 5
            current_sound = randint(0, len(self.sound_characters1[ob]) - 1)
            self.sound_characters1[ob][current_sound].play()
        elif ob=="bottle":
            m = randint(0, 3)
            self.buttons[self.coordinates1[ob][0]][self.coordinates1[ob][1]].setIcon(QIcon(f'images/bottle{m + 1}.png'))
        elif ob=="crab" and self.flag_eat !=9:
            if self.crabHands == True:
                self.buttons[self.coordinates1[ob][0]][self.coordinates1[ob][1]].setIcon(QIcon(f'images/crab2.png'))
                self.crabHands = False
            else:
                self.buttons[self.coordinates1[ob][0]][self.coordinates1[ob][1]].setIcon(QIcon(f'images/crab.png'))
                self.crabHands = True
            current_sound = randint(0, len(self.sound_characters1[ob]) - 1)
            self.sound_characters1[ob][current_sound].play()
        elif ob=="crab" and self.flag_eat == 9:
            self.sound_money.play()
        elif ob=="snowman":
            if self.snowmanHands == True:
                self.buttons[self.coordinates1[ob][0]][self.coordinates1[ob][1]].setIcon(QIcon(f'images/snowman2.png'))
                self.snowmanHands = False
            else:
                self.buttons[self.coordinates1[ob][0]][self.coordinates1[ob][1]].setIcon(QIcon(f'images/snowman.png'))
                self.snowmanHands = True
            current_sound = randint(0, len(self.sound_characters1[ob]) - 1)
            self.sound_characters1[ob][current_sound].play()
        elif ob=="chebyrashka" and self.flag_eat != 5 and self.flag_eat !=0:
            self.buttons[self.coordinates1[ob][0]][self.coordinates1[ob][1]].setIcon(QIcon(f'images/chebyrashka.png'))
            current_sound = randint(0, len(self.sound_characters1[ob]) - 1)
            self.sound_characters1[ob][current_sound].play()
        elif ob=="chebyrashka" and self.flag_eat == 5:
            self.buttons[self.coordinates1[ob][0]][self.coordinates1[ob][1]].setIcon(QIcon(f'images/chebyrashka2.png'))
            current_sound = randint(0, len(self.sound_characters1[ob]) - 1)
            self.sound_characters1[ob][current_sound].play()
        else:
            current_sound = randint(0, len(self.sound_characters1[ob]) - 1)
            self.sound_characters1[ob][current_sound].play()
        if ob=="stock1" and self.flag_eat == 0:
            cur = QCursor(QPixmap('images/stock2.png').scaledToWidth(50))
            QApplication.setOverrideCursor(cur)
            self.flag_eat = 1
        elif ob=="strawberry1" and self.flag_eat == 0:
            cur = QCursor(QPixmap('images/strawberry2.png').scaledToWidth(50))
            QApplication.setOverrideCursor(cur)
            self.flag_eat = 2
        elif ob=="apple1" and self.flag_eat == 0:
            cur = QCursor(QPixmap('images/apple2.png'))
            QApplication.setOverrideCursor(cur)
            self.flag_eat = 3
        elif ob=="pear1" and self.flag_eat == 0:
            cur = QCursor(QPixmap('images/pear2.png').scaled(30, 40))
            QApplication.setOverrideCursor(cur)
            self.flag_eat = 4
        elif ob=="mandarine1" and self.flag_eat == 0:
            cur = QCursor(QPixmap('images/mandarine2.png').scaled(60, 40))
            QApplication.setOverrideCursor(cur)
            self.flag_eat = 5
        elif ob=="pineapple1" and self.flag_eat == 0:
            cur = QCursor(QPixmap('images/pineapple2.png').scaled(100, 100))
            QApplication.setOverrideCursor(cur)
            self.flag_eat = 6
        elif ob=="coconut1" and self.flag_eat == 0:
            cur = QCursor(QPixmap('images/coconut2.png').scaled(60, 60))
            QApplication.setOverrideCursor(cur)
            self.flag_eat = 7
        elif ob=="banana1" and self.flag_eat == 0:
            cur = QCursor(QPixmap('images/banana2.png').scaled(80, 50))
            QApplication.setOverrideCursor(cur)
            self.flag_eat = 8
        elif ob=="coin1" and self.flag_eat == 0:
            cur = QCursor(QPixmap('images/coin2.png').scaled(80, 50))
            QApplication.setOverrideCursor(cur)
            self.flag_eat = 9
        elif ob=="gift" and self.flag_eat == 0:
            cur = QCursor(QPixmap('images/gift2.png').scaled(50, 50))
            QApplication.setOverrideCursor(cur)
            self.flag_eat = 10
        else:
            QApplication.restoreOverrideCursor()
            self.flag_eat = 0

LOCATIONS = 3
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        
        characters1 = ["pig", "cow", "cat", "Liza", "sheep", "stock1", "strawberry1", "apple1", "kuku", "bottle", "house", "pear1"]
        coordinates1 = {
            "pig": (7, 1), 
            "cow": (2, 7), 
            "cat": (8, 8), 
            "Liza": (3, 2), 
            "sheep": (5, 9), 
            "stock1": (6, 5), 
            "strawberry1": (3, 5), 
            "apple1": (1, 1), 
            "kuku": (5, 3), 
            "bottle": (9, 5), 
            "house": (0, 4), 
            "pear1": (0, 5)
            }
        backcolor1= [
            (137, 160, 32),
            (137, 160, 32),
            (137, 160, 32),
            (137, 160, 32),
            (137, 160, 32),
            (137, 160, 32),
            (137, 160, 32),
            (137, 160, 32),
            (137, 160, 32),
            (137, 160, 32)
        ]
        backcolor2= [
            (252, 221, 118),
            (252, 221, 118),
            (252, 221, 118),
            (252, 221, 118),
            (252, 221, 118),
            (252, 221, 118),
            (252, 221, 118),
            (28,163,236),
            (28,163,236),
            (28,163,236)
        ]
        characters2 = ["pineapple1", "banana1", "coconut1", "crab", "coin1", "mandarine1", "elephant", "chebyrashka", "Liza"]
        coordinates2 = {"pineapple1": (1, 3), "banana1": (2, 7), "coconut1": (3, 4), "crab": (6, 2), "coin1": (6, 9), "mandarine1": (3, 8), "elephant": (5, 4), "chebyrashka": (4, 2), "Liza": (6, 5)}

        backcolor3 = [
            (255, 250, 250),
            (255, 250, 250),
            (255, 250, 250),
            (255, 250, 250),
            (255, 250, 250),
            (255, 250, 250),
            (255, 250, 250),
            (255, 250, 250),
            (255, 250, 250),
            (255, 250, 250)
        ]
        characters3 = ["elka", "gift", "snowman", "catMat", "champagne", "rabbit", "salad"]
        coordinates3 = {"elka": (4, 4), "gift": (4, 5), "snowman": (8, 3), "catMat": (3, 2), "champagne": (9, 6), "rabbit": (6, 7), "salad": (7, 9)}
        for i in range(1, 11):
            characters3.append(f'bells{i}')
            coordinates3[f'bells{i}'] = (0, i-1)
        self.location1 = MainWidget(backcolor1, characters1, coordinates1)
        self.location2 = MainWidget(backcolor2, characters2, coordinates2)
        self.location3 = MainWidget(backcolor3, characters3, coordinates3)
        self.location1.setContentsMargins(0, 0, 0, 0)
        self.location2.setContentsMargins(0, 0, 0, 0)

        mainWidget = QWidget()
        self.stack_location = QStackedLayout(mainWidget)

        menu = QWidget()
        menu.setStyleSheet("border-image: url(images/menu.jpeg);")
        self.stack_location.addWidget(menu)

        self.stack_location.addWidget(self.location1)
        self.stack_location.addWidget(self.location2)
        self.stack_location.addWidget(self.location3)
        self.stack_location.setCurrentIndex(0)

        leftRightWidget = QWidget()
        leftRightLayout = QGridLayout(leftRightWidget)

        button_left = QPushButton()
        button_left.setIcon(QIcon(f'images/left.png'))
        button_left.setIconSize(QtCore.QSize(75, 50))
        button_left.setMinimumSize(QtCore.QSize(75, 50))
        button_left.setMaximumSize(QtCore.QSize(75, 50))
        button_left.setStyleSheet("background-color: #4d8fac; color: White; border-radius: 600px;")
        button_left.clicked.connect(self.leftRight) 
        button_left.setObjectName("left")
        leftRightLayout.addWidget(button_left, 0, 0, 0, 0)

        button_right = QPushButton()
        button_right.setIcon(QIcon(f'images/right.png'))
        button_right.setIconSize(QtCore.QSize(75, 50))
        button_right.setMinimumSize(QtCore.QSize(75, 50))
        button_right.setMaximumSize(QtCore.QSize(75, 50))
        button_right.setStyleSheet("background-color: #4d8fac; color: White; border-radius: 600px;")
        button_right.clicked.connect(self.leftRight) 
        button_right.setObjectName("right")
        leftRightLayout.addWidget(button_right, 0, N - 1)
        
        leftRightLayout.setSpacing(0)
        leftRightLayout.setContentsMargins(0, 0, 0, 0)

        verticalWidget = QWidget()
        verticalLayout = QVBoxLayout(verticalWidget)

        leftRightWidget.setContentsMargins(0, 0, 0, 0)
        mainWidget.setContentsMargins(0, 0, 0, 0)

        verticalLayout.addWidget(leftRightWidget)
        verticalLayout.addWidget(mainWidget)
        verticalLayout.setSpacing(0)
        verticalWidget.setContentsMargins(0,0,0,0)

        self.setCentralWidget(verticalWidget)

    def leftRight(self):
        c = self.stack_location.currentIndex()
        if self.sender().objectName() == 'left':
            c-=1
            if c < 1:
                c = LOCATIONS
        else:
            c+=1
            if c > LOCATIONS:
                c = 1
        self.stack_location.setCurrentIndex(c)

    def mousePressEvent(self, event):
        print(self.stack_location.currentIndex())
        if self.stack_location.currentIndex() == 0:
            self.stack_location.setCurrentIndex(1)

    def paintEvent(self, paintEvent):
        paint = QPainter(self)
        paint.setPen(QColor("#000000"))
        p = QtCore.QPoint( 13, 7)
        p1 = QtCore.QPoint(20, 20)
        p2 = QtCore.QPoint(60, 60)
        sky_image = QPixmap(f'images/sky.png').scaled(750, 225)
        paint.drawPixmap(self.rect(), sky_image)
        paint.drawPoint(p)
        paint.drawLine(p1, p2)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()