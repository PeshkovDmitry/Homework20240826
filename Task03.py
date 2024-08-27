from Task03.Cell import Cell
from Task03.Board import Board

c = Cell(1)
board = Board()
for i in range(9):
    board.set(i, Cell.CROSS_SYMBOL)
print(board)