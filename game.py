class Square:

    def __init__(self, square_id):
        self.square = []

        self.square_id = square_id

        self.createSquare()

    def createSquare(self):

        self.square = [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]

        return self.square

    def printSquare(self):

        for i in range(0, len(self.square)):
            print(self.square[i])

    def getPos(self, x_pos, y_pos):

        return self.square[y_pos - 1][x_pos - 1]

    def insertNum(self, x_pos, y_pos, num):

        self.square[y_pos-1][x_pos-1] = num

    def checkSquareIllegalNum(self):

        num_count = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

        for num in num_count:
            for row in self.square:
                num_count[num] = num_count.get(num) + row.count(num)
            if num_count.get(num) > 1:
                return False

        return True

class Board:

    def __init__(self):
        self.board = []

        self.square_1 = Square(1)
        self.square_2 = Square(2)
        self.square_3 = Square(3)
        self.square_4 = Square(4)
        self.square_5 = Square(5)
        self.square_6 = Square(6)
        self.square_7 = Square(7)
        self.square_8 = Square(8)
        self.square_9 = Square(9)

        self.createBoard()

    def createBoard(self):

        self.board = [[self.square_1, self.square_2, self.square_3], [self.square_4, self.square_5, self.square_6], [self.square_7, self.square_8, self.square_9]]

        return self.board

    def insertToBoard(self, x_pos, y_pos, num):

        x_dict = {1:1, 2:2, 3:3, 4:1, 5:2, 6:3, 7:1, 8:2, 9:3}
        y_dict = {1:1, 2:2, 3:3, 4:1, 5:2, 6:3, 7:1, 8:2, 9:3}

        if y_pos <= 3:
            if x_pos <= 3:
                self.square_1.insertNum(x_dict.get(x_pos), y_dict.get(y_pos), num)
            elif x_pos > 3 and x_pos <= 6:
                self.square_2.insertNum(x_dict.get(x_pos), y_dict.get(y_pos), num)
            elif x_pos > 6 and x_pos <= 9:
                self.square_3.insertNum(x_dict.get(x_pos), y_dict.get(y_pos), num)
        elif y_pos > 3 and y_pos <= 6:
            if x_pos <= 3:
                self.square_4.insertNum(x_dict.get(x_pos), y_dict.get(y_pos), num)
            elif x_pos > 3 and x_pos <= 6:
                self.square_5.insertNum(x_dict.get(x_pos), y_dict.get(y_pos), num)
            elif x_pos > 6 and x_pos <= 9:
                self.square_6.insertNum(x_dict.get(x_pos), y_dict.get(y_pos), num)
        elif y_pos > 6 and y_pos <= 9:
            if x_pos <= 3:
                self.square_7.insertNum(x_dict.get(x_pos), y_dict.get(y_pos), num)
            elif x_pos > 3 and x_pos <= 6:
                self.square_8.insertNum(x_dict.get(x_pos), y_dict.get(y_pos), num)
            elif x_pos > 6 and x_pos <= 9:
                self.square_9.insertNum(x_dict.get(x_pos), y_dict.get(y_pos), num)

    def printBoard(self):

        for squares in range(0, len(self.board)):
            for row in range(0, 3):
                for square in range(0, len(self.board[squares])):
                    if square == 2:
                        print(*self.board[squares][square].square[row])
                    else:
                        print(*self.board[squares][square].square[row], end=' | ')
                if row == 2 and squares != 2:
                    print('- '*11)

        print('')
        print('- '*11)
        print('')

    def checkIllegalNum(self):

        if self.checkCol() and self.checkRow() and self.checkSquare():
            return True
        else:
            return False

    def checkSquare(self):
        for rows in self.board:
            for square in range(0, len(rows)):
                if rows[square].checkSquareIllegalNum() == False:
                    return False

        return True

    def checkRow(self):

        num_count = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

        row_count = 0
        for row_squares in range(0, len(self.board)):
            for row in range(0, 3):
                row_count +=1
                for square in range(0, len(self.board[row_squares])):
                    for num in num_count:
                        num_count[num] = num_count.get(num) + self.board[row_squares][square].square[row].count(num)
                for check_num in num_count:
                    if num_count.get(check_num) > 1:
                        return False
                num_count = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

        return True

    def checkCol(self):

        num_count = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

        col_count = 0
        for col in range(0, 3):
            for sq_col in range(0, 3):
                col_count += 1
                for row in range(0, len(self.board)):
                    for num in num_count:
                        count = 0
                        for sq in range(0, len(self.board[row][col].square)):
                            if num == self.board[row][col].square[sq][sq_col]:
                                count += 1
                        num_count[num] = num_count.get(num) + count
                for check_num in num_count:
                    if num_count.get(check_num) > 1:
                        return False
                num_count = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

        return True

    def checkWin(self):

        is_board_complete = True
        win = False

        for square_row in self.board:
            for squares in square_row:
                for rows in squares.square:
                    for x in rows:
                        if x == 'X':
                            is_board_complete = False

        if is_board_complete and self.checkIllegalNum() == True:
            win = True

        return win

    def getValueAtCoord(self, x_pos, y_pos):
        x_dict = {1:1, 2:2, 3:3, 4:1, 5:2, 6:3, 7:1, 8:2, 9:3}
        y_dict = {1:1, 2:2, 3:3, 4:1, 5:2, 6:3, 7:1, 8:2, 9:3}

        if y_pos <= 3:
            if x_pos <= 3:
                return self.square_1.getPos(x_dict.get(x_pos), y_dict.get(y_pos))
            elif x_pos > 3 and x_pos <= 6:
                return self.square_2.getPos(x_dict.get(x_pos), y_dict.get(y_pos))
            elif x_pos > 6 and x_pos <= 9:
                return self.square_3.getPos(x_dict.get(x_pos), y_dict.get(y_pos))
        elif y_pos > 3 and y_pos <= 6:
            if x_pos <= 3:
                return self.square_4.getPos(x_dict.get(x_pos), y_dict.get(y_pos))
            elif x_pos > 3 and x_pos <= 6:
                return self.square_5.getPos(x_dict.get(x_pos), y_dict.get(y_pos))
            elif x_pos > 6 and x_pos <= 9:
                return self.square_6.getPos(x_dict.get(x_pos), y_dict.get(y_pos))
        elif y_pos > 6 and y_pos <= 9:
            if x_pos <= 3:
                return self.square_7.getPos(x_dict.get(x_pos), y_dict.get(y_pos))
            elif x_pos > 3 and x_pos <= 6:
                return self.square_8.getPos(x_dict.get(x_pos), y_dict.get(y_pos))
            elif x_pos > 6 and x_pos <= 9:
                return self.square_9.getPos(x_dict.get(x_pos), y_dict.get(y_pos))

    def solve(self):
        for x in range(1, 10):
            for y in range(1, 10):
                if self.getValueAtCoord(x, y) == 'X':
                    for num in range(1, 10):
                        if self.checkIllegalNum():
                            self.insertToBoard(x, y, str(num))
                            if self.solve() and self.checkWin():
                                return True
                            self.insertToBoard(x, y, 'X')
                    return False

        return True


def createBoard():

    board = Board()
    board.insertToBoard(4, 1, '8')
    board.insertToBoard(5, 1, '3')
    board.insertToBoard(6, 1, '1')
    board.insertToBoard(7, 1, '5')
    board.insertToBoard(8, 1, '6')
    board.insertToBoard(2, 2, '3')
    board.insertToBoard(4, 2, '9')
    board.insertToBoard(1, 3, '8')
    board.insertToBoard(2, 3, '6')
    board.insertToBoard(5, 3, '7')
    board.insertToBoard(6, 3, '4')
    board.insertToBoard(8, 3, '2')
    board.insertToBoard(1, 4, '7')
    board.insertToBoard(3, 4, '8')
    board.insertToBoard(4, 4, '6')
    board.insertToBoard(5, 4, '4')
    board.insertToBoard(6, 4, '3')
    board.insertToBoard(7, 4, '2')
    board.insertToBoard(8, 4, '1')
    board.insertToBoard(9, 4, '9')
    board.insertToBoard(3, 5, '4')
    board.insertToBoard(7, 5, '3')
    board.insertToBoard(2, 6, '1')
    board.insertToBoard(3, 6, '2')
    board.insertToBoard(6, 6, '9')
    board.insertToBoard(5, 7, '8')
    board.insertToBoard(7, 7, '7')
    board.insertToBoard(8, 7, '9')
    board.insertToBoard(2, 8, '7')
    board.insertToBoard(3, 8, '6')
    board.insertToBoard(5, 8, '1')
    board.insertToBoard(7, 8, '8')
    board.insertToBoard(8, 8, '3')
    board.insertToBoard(1, 9, '4')
    board.insertToBoard(2, 9, '8')
    board.insertToBoard(5, 9, '9')
    board.insertToBoard(7, 9, '6')
    board.insertToBoard(9, 9, '1')

    #print(board.getValueAtCoord(8, 7))
    board.printBoard()

    board.solve()

    board.printBoard()

    print(board.checkWin())

if __name__ == '__main__':
    createBoard()