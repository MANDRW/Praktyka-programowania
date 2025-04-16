import os
import random
import time
class Cell:
    _x = 0
    _y = 0
    _isAlive = False
    _neighbors = []
    _numNeighbors = 0

    def __init__(self, x, y, isAlive=False):
        self._x = x
        self._y = y
        self._isAlive = False

    def checkNeighbors(self, board):
        """
        Check the neighbors of the cell and update the number of neighbors.
        """
        sumNeighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if self._x + i < 0 or self._y +j < 0:
                    continue
                if self._x + i > len(board)-1 or self._y +j > len(board[0])-1:
                    continue
                if board[self._x + i][self._y + j]._isAlive:
                    sumNeighbors += 1
        return sumNeighbors

    def setAlive(self):
        """
        Set the cell to be alive or dead.
        """
        self._isAlive = True
    def setDead(self):
        """
        Set the cell to be dead.
        """
        self._isAlive = False

class Board:
    _cells = []
    _width = 0
    _height = 0
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._cells = [[Cell(x, y) for y in range(height)] for x in range(width)]
        self.startingBoard()

    def startingBoard(self):
        random.seed(1234)
        maxCell = (self._width * self._height)*0.15
        for i in range(int(maxCell)):
            x = random.randint(0, self._width-1)
            y = random.randint(0, self._height-1)
            self._cells[x][y].setAlive()

    def printBoard(self):
        """
        Print the board.
        """
        for i in range(self._width):
            for j in range(self._height):
                if self._cells[i][j]._isAlive:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            print()

    def changeCellsStatus(self):
        """
        Change the status of the cells based on the number of neighbors.
        """
        for i in range(self._width):
            for j in range(self._height):
                numNeighbors = self._cells[i][j].checkNeighbors(self._cells)
                if self._cells[i][j]._isAlive:
                    if numNeighbors < 2 or numNeighbors > 3:
                        self._cells[i][j].setDead()
                else:
                    if numNeighbors == 3:
                        self._cells[i][j].setAlive()

    def startSim(self):
        """
        Start the simulation.
        """

        self.printBoard()
        while True:
            self.changeCellsStatus()
            os.system('clear' if os.name == 'posix' else 'cls')
            self.printBoard()
            time.sleep(0.1)



if __name__ == "__main__":
    board = Board(20, 20)
    board.startSim()