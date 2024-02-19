import sys
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QGridLayout, QFrame, QPushButton

class SudokuPuzzleCreator:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.generate_completed_grid()
        self.create_puzzle()

    def generate_completed_grid(self):
        def is_valid_move(grid, row, col, num):
            # Check row
            if num in grid[row]:
                return False
            # Check column
            if num in [grid[i][col] for i in range(9)]:
                return False
            # Check 3x3 subgrid
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if grid[i][j] == num:
                        return False
            return True

        def solve(grid):
            empty_cell = find_empty_cell(grid)
            if not empty_cell:
                return True
            row, col = empty_cell
            for num in range(1, 10):
                if is_valid_move(grid, row, col, num):
                    grid[row][col] = num
                    if solve(grid):
                        return True
                    grid[row][col] = 0
            return False

        def find_empty_cell(grid):
            for i in range(9):
                for j in range(9):
                    if grid[i][j] == 0:
                        return (i, j)
            return None

        solve(self.grid)

    def create_puzzle(self):
        puzzle = [[self.grid[i][j] for j in range(9)] for i in range(9)]
        cells = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(cells)
        for i, j in cells:
            temp = puzzle[i][j]
            puzzle[i][j] = 0
            if not self.is_unique_solution(puzzle):
                puzzle[i][j] = temp
        self.puzzle = puzzle

    def is_unique_solution(self, puzzle):
        def solve(grid):
            empty_cell = find_empty_cell(grid)
            if not empty_cell:
                return True
            row, col = empty_cell
            for num in range(1, 10):
                if is_valid_move(grid, row, col, num):
                    grid[row][col] = num
                    if solve(grid):
                        return True
            return False

        def find_empty_cell(grid):
            for i in range(9):
                for j in range(9):
                    if grid[i][j] == 0:
                        return (i, j)
            return None

        def is_valid_move(grid, row, col, num):
            # Check row
            if num in grid[row]:
                return False
            # Check column
            if num in [grid[i][col] for i in range(9)]:
                return False
            # Check 3x3 subgrid
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if grid[i][j] == num:
                        return False
            return True

        solved = solve(puzzle)
        if not solved:
            return False

        cells = [(i, j) for i in range(9) for j in range(9) if puzzle[i][j] == 0]
        random.shuffle(cells)
        for i, j in cells:
            temp = puzzle[i][j]
            puzzle[i][j] = 1
            if solve([row[:] for row in puzzle]):
                puzzle[i][j] = temp
                return False
            puzzle[i][j] = temp
        return True

class SudokuGrid(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        self.layout.setSpacing(0)  # No spacing between cells

        # 2D list to store the QLineEdit widgets and their positions
        self.cells = []
        for i in range(9):
            for j in range(9):
                cell = QLineEdit()
                cell.setFixedWidth(30)
                cell.setMaxLength(1)
                cell.setAlignment(Qt.AlignCenter)
                self.cells.append(cell)
                self.layout.addWidget(cell, i, j)
                # Add vertical and horizontal separators
                if (j + 1) % 3 == 0 and j != 8:
                    vline = QFrame()
                    vline.setFrameShape(QFrame.VLine)
                    vline.setFixedWidth(1)
                    vline.setStyleSheet("color: black")
                    self.layout.addWidget(vline, i, j + 1, 1, 1, Qt.AlignCenter)
                if (i + 1) % 3 == 0 and i != 8:
                    hline = QFrame()
                    hline.setFrameShape(QFrame.HLine)
                    hline.setFixedHeight(1)
                    hline.setStyleSheet("color: black")
                    self.layout.addWidget(hline, i + 1, j, 1, 9, Qt.AlignCenter)

        self.setLayout(self.layout)

    def set_puzzle(self, puzzle):
        for i in range(9):
            for j in range(9):
                self.cells[i * 9 + j].setText(str(puzzle[i][j]))
        
        check = 0
        while check != 13:
            x_rng = random.randint(0, 8)
            y_rng = random.randint(0, 8)
            self.cells[x_rng * 9 + y_rng].setText("")
            check += 1

    def is_valid_move(self, row, col, num):
        # Check row
        for i in range(9):
            if i != col and self.cells[row * 9 + i].text() == num:
                return False
        # Check column
        for i in range(9):
            if i != row and self.cells[i * 9 + col].text() == num:
                return False
        # Check 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if (i != row or j != col) and self.cells[i * 9 + j].text() == num:
                    return False
        return True

    def is_solved(self):
        for i in range(9):
            for j in range(9):
                if not self.cells[i * 9 + j].text().isdigit():
                    return False
        return True

class SudokuWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sudoku Solver")
        self.setGeometry(100, 100, 400, 400)

        # Layout for the Sudoku window
        self.layout = QVBoxLayout()

        # Sudoku grid subwidget
        self.grid = SudokuGrid()
        self.layout.addWidget(self.grid)

        # Create a Sudoku puzzle
        puzzle_creator = SudokuPuzzleCreator()
        self.grid.set_puzzle(puzzle_creator.puzzle)

        check_button = QPushButton("Check Solution")
        exit_button = QPushButton("Exit")
        check_button.clicked.connect(self.check_solution)
        exit_button.clicked.connect(self.exit)
        self.layout.addWidget(check_button)
        self.layout.addWidget(exit_button)

        self.setLayout(self.layout)
    
    def check_solution(self):
        if not self.grid.is_solved():
            print("Sudoku is not fully solved!")
            return
        for i in range(9):
            for j in range(9):
                num = self.grid.cells[i * 9 + j].text()
                if not self.grid.is_valid_move(i, j, num):
                    print("Invalid move at row:", i, "column:", j)
                    return
        print("Sudoku solution is valid!")

    def exit(self):
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SudokuWindow()
    window.show()
    sys.exit(app.exec_())