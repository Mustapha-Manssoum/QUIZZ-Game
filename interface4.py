from PySide2.QtCore import QPoint
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton

from PySide2.QtWidgets import QMainWindow, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton

class Interface4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quizz ")
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

        # Create widgets
        self.question_label = QLabel("What is the capital of France?")
        self.answer_button_1 = QPushButton("Paris")
        self.answer_button_2 = QPushButton("London")
        self.answer_button_3 = QPushButton("New York")
        self.answer_button_4 = QPushButton("Tokyo")

        # Create layout and add widgets
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question_label)
        self.layout.addWidget(self.answer_button_1)
        self.layout.addWidget(self.answer_button_2)
        self.layout.addWidget(self.answer_button_3)
        self.layout.addWidget(self.answer_button_4)

        # Create a central widget and set the layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

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






