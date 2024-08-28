from Task04.AnimalFactory import AnimalFactory


factory = AnimalFactory
fish = factory.create_animal("Fish", "Ponyo", 2.0)
bird = factory.create_animal("Bird", "Woody", 0.5)
mammal = factory.create_animal("Mammal", "Jerry", 0.1)

print(fish.depth())
print(bird.winglength())
print(mammal.category())