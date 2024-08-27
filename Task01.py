class Parent:

    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
        self.__children = []

    def __str__(self):
        info = f"{self.__name}, {self.__age} лет, дети: "
        for child in self.__children:
            info += child.name + ", "
        return info

    def add_child(self, child):
        if self.__age - child.age > 16:
            self.__children.append(child)

    def feed(self, child):
        if child in self.__children:
            child.is_hungry = False

    def calm(self, child):
        if child in self.__children:
            child.is_calm = True


class Child:

    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
        self.__is_calm = False
        self.__is_hungry = True

    def __str__(self):
        info = f"{self.__name}, {self.__age} лет, "
        info += f"{'голоден' if self.__is_hungry else 'не голоден'} и "
        info += f"{'спокоен' if self.__is_calm else 'не спокоен'}"
        return info

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def is_calm(self):
        return self.__is_calm

    @is_calm.setter
    def is_calm(self, value):
        self.__is_calm = value

    @property
    def is_hungry(self):
        return self.__is_hungry

    @is_hungry.setter
    def is_hungry(self, value):
        self.__is_hungry = value


p = Parent("Иван", 33)
с_1 = Child("Андрей", 15)
с_2 = Child("Ирина", 13)
с_3 = Child("Ольга", 30)
p.add_child(с_1)
p.add_child(с_2)
print(p)
