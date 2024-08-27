class Cell:

    BLANK_SYMBOL = " "
    CROSS_SYMBOL = "X"
    ZERO_SYMBOL = "O"

    def __init__(self, pos):
        self.__is_set = False
        self.__symbol = Cell.BLANK_SYMBOL
        self.__pos = pos

    def __str__(self):
        return self.__symbol

    @property
    def is_set(self):
        return self.__is_set

    @is_set.setter
    def is_set(self, value: bool):
        self.__is_set = value
        if not self.__is_set:
            self.__symbol = Cell.BLANK_SYMBOL

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, value):
        if value == Cell.BLANK_SYMBOL:
            self.__symbol = value
            self.__is_set = False
        if value == Cell.CROSS_SYMBOL or value == Cell.ZERO_SYMBOL:
            self.__symbol = value
            self.__is_set = True

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, value):
        if value in range(9):
            self.__pos = value
