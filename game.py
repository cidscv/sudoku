import random
from board import Board

def createRandomBoard():
    board = Board()

    check = 0

    while check != 13:
        x_rng = random.randint(1, 9)
        y_rng = random.randint(1, 9)
        num_rng = random.randint(1, 9)

        board.insertToBoard(x_rng, y_rng, str(num_rng))

        if board.checkIllegalNum() == False:
            board.insertToBoard(x_rng, y_rng, 'X')
        else:
            check += 1

    board.printBoard()
    print(board.solve())
    board.printBoard()

def main():
    """
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
    board.printBoard()

    board.solve()
    board.printBoard()
    """

    createRandomBoard()

if __name__ == '__main__':
    main()