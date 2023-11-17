class Square:

    def __init__(self, square_id):
        self.square = []
        self.square_id = square_id

        self.createSquare()

    def createSquare(self):

        self.square = [['X', 'X', 'X'],
                       ['X', 'X', 'X'],
                       ['X', 'X', 'X']]

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