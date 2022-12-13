from random import randint


class Person:
    count = 0

    def __init__(self, c):
        self.id = Person.count
        Person.count += 1
        self.command = c


class Soldier(Person):
    def __init__(self, c):
        Person.__init__(self, c)
        self.hero = None

    def follow(self, hero):
        self.hero = hero.id


class Hero(Person):
    def __init__(self, c):
        Person.__init__(self, c)
        self.level = 1

    def next_level(self):
        self.level += 1


class soldier:
    def __init__(self, name='Name', health=100):
        self.name = name
        self.health = health

    def make_kick(self, enemy):
        enemy.health -= 15
        if enemy.health < 0:
            enemy.health = 0
        print(self.name, 'бьёт', enemy.name)
        print(f'{enemy.name} = {enemy.health}')


class Battle:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        self.result = "Сражения не было... Компании объединились в Intel+AMD Tech"

    def battle(self):
        while self.s1.health > 0 and self.s2.health > 0:
            n = randint(1, 2)
            if n == 1:
                self.s1.make_kick(self.s2)
            else:
                self.s2.make_kick(self.s1)
        if self.s1.health > self.s2.health:
            self.result = self.s1.name + " ПОБЕДИЛ!"
        elif self.s2.health > self.s1.health:
            self.result = self.s2.name + " ПОБЕДИЛ!"

    def who_win(self):
        print(self.result)


s1 = soldier("Intel", 160)
s2 = soldier("AMD", 170)
b = Battle(s1, s2)
b.battle()
b.who_win()
