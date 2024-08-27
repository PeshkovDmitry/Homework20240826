from random import randint


class Home:

    def __init__(self, food, money):
        self.__food = food
        self.__money = money

    @property
    def food(self):
        return self.__food

    @food.setter
    def food(self, value):
        self.__food = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value


class Man:

    def __init__(self, name, satiety, home):
        self.__name = name
        self.__satiety = satiety
        self.__home = home

    def __str__(self):
        return f"{self.__name}, сытость {self.__satiety}, денег {self.__home.money}, еды {self.__home.food}"

    def eat(self):
        self.__satiety += 1
        self.__home.food -= 1

    def work(self):
        self.__satiety -= 1
        self.__home.money += 1

    def play(self):
        self.__satiety -= 1

    def shop(self):
        self.__home.food += 1
        self.__home.money -= 1

    def live(self):
        if self.__satiety == 0:
            print("Человек помер")
        if self.__satiety < 20:
            self.eat()
            return
        if self.__home.food < 10:
            self.shop()
            return
        if self.__home.money < 50:
            self.work()
            return
        num = randint(1, 6)
        if num == 1:
            self.work()
            return
        elif num == 2:
            self.eat()
            return
        else:
            self.play()


home = Home(50, 0)
man = Man("Иван", 50, home)
for _ in range(365):
    man.live()
    print(man)



