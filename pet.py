import math
import random


class Pet:
    __food: int = 100
    __water: int = 100
    __pee: int = 100
    __poo: int = 100

    def feed(self):
        self.__food = 100

    def water(self):
        self.__water = 100

    def pee(self):
        self.__pee = 100

    def poo(self):
        self.__poo = 100

    def spend(self):
        self.__food -= random.randint(0, 20)
        self.__water -= random.randint(0, 20)
        self.__pee -= random.randint(0, 20)
        self.__poo -= random.randint(0, 20)

    def get_health(self):
        if self.__food <= 0 or self.__water <= 0 or self.__pee <= 0 or self.__poo <= 0:
            return 0
        else:
            return (self.__food + self.__water + self.__pee + self.__poo) / 4

    def get_food(self):
        return self.__food

    def get_water(self):
        return self.__water

    def get_pee(self):
        return self.__pee

    def get_poo(self):
        return self.__poo

    def __str__(self):
        return (
            f'Food: {self.__food} points over 100:\n'
            f'{"=" * math.ceil(self.__food / 5)}\n\n'
            f'Water: {self.__water} points over 100:\n'
            f'{"=" * math.ceil(self.__water / 5)}\n\n'
            f'Pee: {self.__pee} points over 100:\n'
            f'{"=" * math.ceil(self.__pee / 5)}\n\n'
            f'Poo: {self.__poo} points over 100:\n'
            f'{"=" * math.ceil(self.__poo / 5)}\n\n'
        )
