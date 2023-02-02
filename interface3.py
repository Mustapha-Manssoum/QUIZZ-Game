from PySide2 import QtWidgets
from PySide2.QtCore import QPoint
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton

from PySide2.QtWidgets import QMainWindow, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton

class ThirdInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign Up ")
        self.setGeometry(400, 300, 1000, 500)



        #create Title
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

        #---------------------------------#

        # Create widgets for the interface
        label1 = QLabel("Email", self)
        label1.setGeometry(100, 200, 200, 50)  # Ajuster les coordonnées X, Y et la taille de la police ici
        # label1.setFixedSize(200, 50)  # Définir la taille fixe pour la taille de la police
        label1.setStyleSheet("font-size: 20px; color: black;width: 999px;color: rgba(0,0,0,1);position: absolute; top: 191px;"
                             "left: 196px; font-family: Inria Serif; font-weight: Italic; font-size: 36px; opacity: 1; text-align: center; ")

        self.name_input1 = QLineEdit(self)
        self.name_input1.setGeometry(300, 50, 500, 50)  # Ajuster les coordonnées X, Y et la taille de la police ici
        self.name_input1.setFixedSize(200, 50)  # Définir la taille fixe pour la taille de la police

        label2 = QLabel("Passworld :")
        label2.setGeometry(100, 300, 200, 50)  # Ajuster les coordonnées X, Y et la taille de la police ici
        label2.setFixedSize(200, 50)  # Définir la taille fixe pour la taille de la police
        label2.setStyleSheet("font-size: 20px; color: black; width: 999px;"
                             "color: rgba(0,0,0,1); position: relative; top: 150px;"
                             " left: 15%; font-family: Inria Serif;"
                             "font-weight: Italic; font-size: 36px;opacity: 1; text-align: center;")
        # Déplacer le label vers la droite de 100 pixels
        new_x = label2.x() + 300
        label2.setGeometry(new_x, label2.y(), label2.width(), label2.height())

        self.name_input2 = QLineEdit()
        self.name_input2.setGeometry(300, 300, 500, 50)  # Ajuster les coordonnées X, Y et la taille de la police ici
        self.name_input2.setFixedSize(100, 20)  # Définir la taille fixe pour la taille de la police

        label3 = QLabel("Confirm PassWorld  :")
        label3.setGeometry(100, 350, 200, 50)  # Ajuster les coordonnées X, Y et la taille de la police ici
        label3.setFixedSize(200, 50)  # Définir la taille fixe pour la taille de la police
        label3.setStyleSheet("QLabel { font-size: 20px; color: black; }")


        self.name_input3 = QLineEdit()
        self.name_input3.setGeometry(300, 350, 500, 50)  # Ajuster les coordonnées X, Y et la taille de la police ici
        self.name_input3.setFixedSize(500, 50)  # Définir la taille fixe pour la taille de la police

        self.Button = QWidget(self)

        self.button1 = QPushButton("Sign up", self.Button)
        self.Button.setGeometry(0, 250, 1000, 100)
        self.button1.clicked.connect(self.on_button_clicked)
        self.button1.setStyleSheet(
            "background-color : #178174; color: black; font-size: 20px; border-radius: 20px;")
        self.button1.setGeometry(250, 25, 200, 50)
        #self.btnSignUp.mousePressEvent = func1


        # Create layout for the widgets
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(self.name_input1)
        layout.addWidget(self.name_input2)
        layout.addWidget(self.name_input3)
        #layout.addWidget(button1)

        # Set the layout for the main window
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)





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

    def on_button_clicked(self):
        name = self.name_input1.text()




