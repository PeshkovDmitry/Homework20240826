from Task04.Animal import Animal


class Bird(Animal):

    def __init__(self, name: str, wingspan: float):
        super().__init__(name)
        self.__wingspan = wingspan

    def winglength(self) -> float:
        return self.__wingspan
