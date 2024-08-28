from Task03.Cell import Cell


class Board:

    def __init__(self):
        self.__cells = []
        for i in range(9):
            self.__cells.append(Cell(i))

    def __str__(self):
        res = f"┌───┬───┬───┐\n\r"
        res += f"│ {self.__cells[0].__str__()} │ {self.__cells[1].__str__()} │ {self.__cells[2].__str__()} │\n\r"
        res += f"├───┼───┼───┤\n\r"
        res += f"│ {self.__cells[3].__str__()} │ {self.__cells[4].__str__()} │ {self.__cells[5].__str__()} │\n\r"
        res += f"├───┼───┼───┤\n\r"
        res += f"│ {self.__cells[6].__str__()} │ {self.__cells[7].__str__()} │ {self.__cells[8].__str__()} │\n\r"
        res += f"└───┴───┴───┘\n\r"
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
        return True

    def check_game_over(self) -> bool:
        for i in range(3):
            if self.__cells[3 * i].symbol == self.__cells[3 * i + 1].symbol == self.__cells[3 * i + 2].symbol != Cell.BLANK_SYMBOL:
                return True
            if self.__cells[i].symbol == self.__cells[i + 3].symbol == self.__cells[i + 6].symbol != Cell.BLANK_SYMBOL:
                return True
        if self.__cells[0].symbol == self.__cells[4].symbol == self.__cells[8].symbol != Cell.BLANK_SYMBOL:
            return True
        if self.__cells[2].symbol == self.__cells[4].symbol == self.__cells[6].symbol != Cell.BLANK_SYMBOL:
            return True
        return False

    def reset_board(self):
        for i in range(9):
            self.__cells[i].is_set = False


