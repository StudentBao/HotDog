from abc import ABC, abstractmethod


class Output(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def display(self):
        pass


class Bread:
    count = 10

    def __init__(self):
        self.bread = "Хлеб"
        self.count -= 1


class Sausage:
    count = 10

    def __init__(self):
        self.sausage = "Сосиска"
        self.count -= 1


class Ketchup:
    count = 10

    def __init__(self):
        self.ketchup = "Кетчуп"
        self.count -= 1


class Mustard:
    count = 10

    def __init__(self):
        self.mustard = "Горчица"
        self.count -= 1


class Mayonnaise:
    count = 10

    def __init__(self):
        self.mayonnaise = "Майонез"
        self.count -= 1


class CheeseSauce:
    count = 10

    def __init__(self):
        self.cheeseSauce = "Сырный соус"
        self.count -= 1


class Onion:
    count = 10

    def __init__(self):
        self.onion = "Лук"
        self.count -= 1


class Cabbage:
    count = 10

    def __init__(self):
        self.cabbage = "Капуста"
        self.count -= 1


class Jalapeno:
    count = 10

    def __init__(self):
        self.jalapeno = "Халапеньо"
        self.count -= 1


class Bacon:
    count = 10

    def __init__(self):
        self.bacon = "Бекон"
        self.count -= 1


class Cheese:
    count = 10

    def __init__(self):
        self.cheese = "Сыр"
        self.count -= 1


class Tomato:
    count = 10

    def __init__(self):
        self.tomato = "Помидоры"
        self.count -= 1


class Carrot:
    count = 10

    def __init__(self):
        self.carrot = "Морковь"
        self.count -= 1


class Classic(Bread, Sausage, Mustard, Carrot):
    def __init__(self):
        self.classic = "Классический хот-дог"


class Memfis(Bread, Sausage, Bacon, Onion, Ketchup):
    def __init__(self):
        self.memfis = "Мемфис хот-дог"


class Hawaiian(Bread, Sausage, Ketchup, Mustard):
    def __init__(self):
        self.hawaiian = "Гавайский хот-дог"


class Menu(ABC):
    @abstractmethod
    def men(self): pass


class Mine:
    def __init__(self):
        self.create = "Создать свой хот-дог "


class choice1(Menu):
    def __init__(self):
        self.choice1 = "Выберите хот дог "


class choice2(Menu):
    def __init__(self):
        self.choice2 = "Выберите добавку "


class choice3(Menu):
    def __init__(self):
        self.choice3 = "Выберите количество хот-догов "


class choice4(Menu):
    def __init__(self):
        self.choice4 = "Выберите способ оплаты "
