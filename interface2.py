from PySide2.QtCore import QPoint
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton

from PySide2.QtWidgets import QMainWindow, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton
from interface4 import Interface4
class SecondInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign In ")
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




        # Create widgets for the interface
        label1 = QLabel("Enter your E-mail:")
        self.name_input1 = QLineEdit()

        label2 = QLabel("Passworld :")
        self.name_input2 = QLineEdit()

        button = QPushButton("Sign In ")
        button.clicked.connect(self.on_button_clicked)

        # Create layout for the widgets
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(self.name_input1)
        layout.addWidget(self.name_input2)
        layout.addWidget(button)

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
        self.third_interface = Interface4()
        self.third_interface.show()

