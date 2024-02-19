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
    createRandomBoard()

if __name__ == '__main__':
    main()