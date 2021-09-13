from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set window title
        self.setWindowTitle("Calculator")
        # set window geometry
        self.setGeometry(400, 200, 320, 315)
        # call widgets method
        self.widgets()
        # show all widgets
        self.show()
    def widgets(self):
        # create a label
        self.label = QLabel(self)
        # set geometry to the label
        self.label.setGeometry(5, 5, 310, 55)
        # set wordwrap
        self.label.setWordWrap(True)
        # set the label style
        self.label.setStyleSheet("QLabel" "{" "border : 2px solid black;"
                                 "Background : white;" "}")
        # set alignment to the label
        self.label.setAlignment(Qt.AlignRight)
        # set font for label text
        self.label.setFont(QFont('Arial', 25))
        # create buttons 
        one = QPushButton("1", self)
        two = QPushButton("2", self)
        three = QPushButton("3", self)
        four = QPushButton("4", self)
        five = QPushButton("5", self)
        six = QPushButton("6", self)
        seven = QPushButton("7", self)
        eight = QPushButton("8", self)
        nine = QPushButton("9", self)
        zero = QPushButton("0", self)
        add = QPushButton("+", self)
        minus = QPushButton("-", self)
        product = QPushButton("*", self)
        div = QPushButton("/", self)
        point = QPushButton(".", self)
        clear = QPushButton("Clear", self)
        Back = QPushButton("Back", self)
        equal = QPushButton("=", self)
        # set fonts for all buttons
        one.setFont(QFont('Arial', 15))
        two.setFont(QFont('Arial', 15))
        three.setFont(QFont('Arial', 15))
        four.setFont(QFont('Arial', 15))
        five.setFont(QFont('Arial', 15))
        six.setFont(QFont('Arial', 15))
        seven.setFont(QFont('Arial', 15))
        eight.setFont(QFont('Arial', 15))
        nine.setFont(QFont('Arial', 15))
        zero.setFont(QFont('Arial', 15))
        add.setFont(QFont('Arial', 15))
        minus.setFont(QFont('Arial', 15))
        product.setFont(QFont('Arial', 15))
        div.setFont(QFont('Arial', 15))
        point.setFont(QFont('Arial', 15))
        clear.setFont(QFont('Arial', 15))
        Back.setFont(QFont('Arial', 15))
        equal.setFont(QFont('Arial', 15))
        
        # set geometry for all buttons
        one.setGeometry(5, 120, 70, 40)
        two.setGeometry(85, 120, 70, 40)
        three.setGeometry(165, 120, 70, 40)
        four.setGeometry(5, 170, 70, 40)
        five.setGeometry(85, 170, 70, 40)
        six.setGeometry(165, 170, 70, 40)
        seven.setGeometry(5, 220, 70, 40)
        eight.setGeometry(85, 220, 70, 40)
        nine.setGeometry(165, 220, 70, 40)
        zero.setGeometry(5, 270, 70, 40)
        add.setGeometry(245, 70, 70, 40)
        minus.setGeometry(245, 120, 70, 40)
        product.setGeometry(245, 170, 70, 40)
        div.setGeometry(245, 220, 70, 40)
        point.setGeometry(85, 270, 70, 40)
        clear.setGeometry(5, 70, 110, 40)
        Back.setGeometry(125, 70, 110, 40)
        equal.setGeometry(165, 270, 150, 40)
        # bind action for all buttons
        one.clicked.connect(self.action1)
        two.clicked.connect(self.action2)
        three.clicked.connect(self.action3)
        four.clicked.connect(self.action4)
        five.clicked.connect(self.action5)
        six.clicked.connect(self.action6)
        seven.clicked.connect(self.action7)
        eight.clicked.connect(self.action8)
        nine.clicked.connect(self.action9)
        zero.clicked.connect(self.action0)
        add.clicked.connect(self.action_plus)
        minus.clicked.connect(self.action_minus)
        product.clicked.connect(self.action_product)
        div.clicked.connect(self.action_div)
        point.clicked.connect(self.action_point)
        clear.clicked.connect(self.action_clear)
        Back.clicked.connect(self.action_back)
        equal.clicked.connect(self.action_equal)
    def action_equal(self):
        # get the label text
        expression = self.label.text()
        try:
            # evaluate expression
            ans = eval(expression)
            # set answer to the label
            self.label.setText(str(ans))
        except:
            # set text to the label
            self.label.setText("Error")
    def action_plus(self):
        # get previous label text
        expression = self.label.text()
        # set label text with '+' sign
        self.label.setText(expression + "+")
    def action_minus(self):
        # get previous label text
        expression = self.label.text()
        # set label text with '-' sign
        self.label.setText(expression + "-")
    def action_div(self):
        # get previous label text
        expression = self.label.text()
        # set label text with '/' sign
        self.label.setText(expression + "/")
    def action_product(self):
        # get previous label text
        expression = self.label.text()
        # set label text with '*' sign
        self.label.setText(expression + "*")
    def action_point(self):
        # get previous label text
        expression = self.label.text()
        # set label text with '.' 
        self.label.setText(expression + ".")
    def action0(self):
        # get previous label text
        expression = self.label.text()
        self.label.setText(expression + "0")
    def action1(self):
        # get previous label text
        expression = self.label.text()
        self.label.setText(expression + "1")
    def action2(self):
        # get previous label text
        expression = self.label.text()
        self.label.setText(expression + "2")
    def action3(self):
        # get previous label text
        expression = self.label.text()
        self.label.setText(expression + "3")
    def action4(self):
        # get previous label text
        expression = self.label.text()
        self.label.setText(expression + "4")
    def action5(self):
        # get previous label text
        expression = self.label.text()
        self.label.setText(expression + "5")
    def action6(self):
        # get previous label text
        expression = self.label.text()
        self.label.setText(expression + "6")
    def action7(self):
        # get previous label text
        expression = self.label.text()
        self.label.setText(expression + "7")
    def action8(self):
        # get previous label text
        expression = self.label.text()
        self.label.setText(expression + "8")
    def action9(self):
        # get previous label text
        expression = self.label.text()
        self.label.setText(expression + "9")
    def action_clear(self):
        # clear label text
        self.label.setText("")
    def action_back(self):
        # get previous label text
        expression = self.label.text()
        self.label.setText(expression[:-1])
CalculatorApp = QApplication(sys.argv)
window = Window()
sys.exit(CalculatorApp.exec())
