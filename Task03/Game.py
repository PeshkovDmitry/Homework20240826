from Task03.Cell import Cell
from Task03.Board import Board
from Task03.Player import Player


class Game:

    def __init__(self, name_1: str, name_2: str):
        self.__board = Board()
        self.__player_1 = Player(name_1, Cell.CROSS_SYMBOL, self.__board)
        self.__player_2 = Player(name_2, Cell.ZERO_SYMBOL, self.__board)

    def __new_game(self):
        self.__board.clear()
        while True:
            if self.__make_step(self.__player_1) or self.__make_step(self.__player_2):
                break
        print(f"{self.__player_1.name} - {self.__player_1.count} побед")
        print(f"{self.__player_2.name} - {self.__player_2.count} побед")

    def __make_step(self, player: Player) -> bool:
        res = player.play()
        print(self.__board)
        return res

    def start(self):
        while True:
            self.__new_game()
            ans = input("Продолжаем (y/n)")
            if ans == "n":
                break
