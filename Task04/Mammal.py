from Task04.Animal import Animal


class Mammal(Animal):

    def __init__(self, name: str, weight: float):
        super().__init__(name)
        self.__weight = weight

    def category(self) -> str:
        if self.__weight < 1:
            return "Малявка"
        elif self.__weight > 200:
            return "Гигант"
        else:
            return "Обычный"


