from PySide2.QtCore import QPoint
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QMainWindow, QToolBar, QPushButton
from PySide2.QtGui import QFont

from interface2 import SecondInterface
from interface3 import ThirdInterface


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quiz App")
        self.setGeometry(400, 300, 1000, 500)
        self.centralWidget = QWidget(self)
        self.centralWidget.setGeometry(0, 0, 1280, 832)

        self.setCentralWidget(self.centralWidget)

        # creating a label widget for app title
        self.labelTitle = QLabel(self)
        self.labelTitle.setText('Let’s Quiz')
        self.labelTitle.setStyleSheet("""color: #0A6A5F;
                                    font: italic;
                                    text-align:center;
                                    font-size: 64px;
                                    """)
        self.labelTitle.setGeometry(0, 50, 1000, 100)
        self.labelTitle.setAlignment(Qt.AlignCenter | Qt.AlignCenter)

        # --------

        self.labelTitle2 = QLabel(self)
        self.labelTitle2.setText('Test your skills and become a master')
        self.labelTitle2.setStyleSheet("""color: #000000;
                                     font: italic;
                                     text-align:center;
                                     font-size: 32px;
                                     """)
        self.labelTitle2.setGeometry(0, 150, 1000, 50)
        self.labelTitle2.setAlignment(Qt.AlignCenter | Qt.AlignCenter)

        # ------------------------------

        self.labelTitle3 = QLabel(self)
        self.labelTitle3.setText('We organize quizzes on various topics')

        self.labelTitle3.setStyleSheet("""color: #000000;
                                             font: italic;
                                             text-align:center;
                                             font-size: 16px;
                                             """)
        self.labelTitle3.setGeometry(200, 180, 800, 50)
        self.labelTitle3.setAlignment(Qt.AlignCenter | Qt.AlignCenter)

        self.Button = QWidget(self)

        self.btnSignUp = QPushButton("Sign up", self.Button)
        self.btnSignIn = QPushButton("Sign in", self.Button)

        self.Button.setGeometry(0, 250, 1000, 100)

        def func1(event):
            self.third_interface = ThirdInterface()
            self.third_interface.show()

        def func2(event):
            self.second_interface = SecondInterface()
            self.second_interface.show()

        self.btnSignUp.setStyleSheet(
            "background-color : #178174; color: black; font-size: 20px; border-radius: 20px;")
        self.btnSignUp.setGeometry(250, 25, 200, 50)
        self.btnSignUp.mousePressEvent = func1

        self.btnSignIn.setStyleSheet(
            "background-color : #178174; color: black; font-size: 20px; border-radius: 20px;")
        self.btnSignIn.setGeometry(550, 25, 200, 50)
        self.btnSignIn.mousePressEvent = func2

        # Create ToolBar

        toolbar = QToolBar()
        super().addToolBar(toolbar)
        # set style sheet to the toolbar
        toolbar.setStyleSheet("QToolBar{ background-color : black; }")

        # Create Buttons
        button1 = QPushButton("home")
        font = QFont("Italic", 10)
        button1.setFont(font)
        toolbar.addWidget(button1)
        button1.setStyleSheet("background-color : black; color: white;")

        button2 = QPushButton("About Us")
        toolbar.addWidget(button2)
        button2.setStyleSheet("background-color : black; color: white;")
        font = QFont("Italic", 10)
        button2.setFont(font)

        current_position = button2.pos()
        new_position = current_position + QPoint(1000, 0)
        button2.move(new_position)

        button3 = QPushButton("Contact Us")
        toolbar.addWidget(button3)
        button3.setStyleSheet("background-color : black; color: white;")
        font = QFont("Italic", 10)
        button3.setFont(font)

