from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout, QFrame

class Square:

    def __init__(self, square_id):
        self.square = []
        self.square_id = square_id

        cell = QLineEdit()
        cell.setFixedWidth(30)
        cell.setMaxLength(1)
        cell.setAlignment(Qt.AlignCenter)
        cell.textChanged.connect(self.check_input)

        self.createSquare(cell)

    def createSquare(self, cell):

        self.square = [[cell, cell, cell],
                       [cell, cell, cell],
                       [cell, cell, cell]]

    def printSquare(self):

        for i in range(0, len(self.square)):
            print(self.square[i])

    def getPos(self, x_pos, y_pos):

        return self.square[y_pos - 1][x_pos - 1]

    def insertNum(self, x_pos, y_pos, num):

        self.square[y_pos-1][x_pos-1] = num

    def check_input(self):
        sender = self.sender()
        text = sender.text()
        if not text.isdigit():
            sender.setText("")
        elif int(text) < 1 or int(text) > 9:
            sender.setText("")

    def checkSquareIllegalNum(self):

        num_count = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

        for num in num_count:
            for row in self.square:
                num_count[num] = num_count.get(num) + row.count(num)
            if num_count.get(num) > 1:
                return False

        return True