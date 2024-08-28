from Task04.Animal import Animal


class Fish(Animal):

    def __init__(self, name: str, max_depth: float):
        super().__init__(name)
        self.__max_depth = max_depth

    def depth(self) -> str:
        if self.__max_depth < 10:
            return "Мелководная рыба"
        elif self.__max_depth > 100:
            return "Глубоководная рыба"
        else:
            return "Средневодная рыба"

