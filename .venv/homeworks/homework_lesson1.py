class Superhero:
    def __init__(self, name, nickname, superpower, healthpoints, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.healthpoints = healthpoints
        self.catchphrase = catchphrase
        
    def print_name(self):
        print(f'Имя героя: {self.name}')

    def double_health(self):
        self.healthpoints *= 2
        print(f'Здоровье удвоено: {self.healthpoints}')

    def __str__(self):
        return f'Прозвище: {self.nickname}, Суперсила: {self.superpower}, Здоровье: {self.healthpoints}'

hero = Superhero(name="Брюс Уэйн", nickname="Бэтмен", superpower="Интеллект и техника", healthpoints=100, catchphrase="Я — Бэтмен!")

hero.print_name()
hero.double_health()
print(hero)              
