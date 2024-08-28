from Task03.Board import Board
from Task03.Cell import Cell
from random import randint

class Player:

    def __init__(self, name: str, symbol: str, board: Board):
        if symbol not in [Cell.CROSS_SYMBOL, Cell.ZERO_SYMBOL]:
            print(f"Для игрока {name} указан неверный символ - {symbol}")
        self.__name = name
        self.__count = 0
        self.__symbol = symbol
        self.__board = board

    @property
    def name(self):
        return self.__name

    @property
    def count(self):
        return self.__count

    def play(self) -> bool:
        while True:
            num = randint(0, 8)
            if self.__board.set(num, self.__symbol):
                break
        if self.__board.check_game_over():
            self.__count += 1
            print(f"{self.__name} победил!")
            return True
        return False
