from Task04.Bird import Bird
from Task04.Mammal import Mammal
from Task04.Fish import Fish


class AnimalFactory:

    @staticmethod
    def create_animal(animal_type: str, *args):
        if animal_type not in ["Bird", "Fish", "Mammal"]:
            raise ValueError(f"Недопустимый тип животного - {animal_type}")
        name = None
        parameter = None
        if len(args) == 2:
            name = args[0]
            parameter = args[1]
        match animal_type:
            case "Bird":
                return Bird(name, parameter)
            case "Fish":
                return Fish(name, parameter)
            case "Mammal":
                return Mammal(name, parameter)
