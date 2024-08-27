from Task03.Cell import Cell


class Board:

    def __init__(self):
        self.__cells = []
        for i in range(9):
            self.__cells.append(Cell(i))

    def __str__(self):
        res = ""
        for i in range(9):
            if i % 3 == 0:
                res += "\n\r"
            res += self.__cells[i].__str__()
        return res

    def set(self, num: int, symbol: str) -> bool:
        if num not in range(9):
            return False
        if symbol not in [Cell.BLANK_SYMBOL, Cell.CROSS_SYMBOL, Cell.ZERO_SYMBOL]:
            return False
        c = self.__cells[num]
        if c.is_set:
            return False
        c.symbol = symbol

    def check(self):
        pass
