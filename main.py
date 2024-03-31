import random
class Human:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.satiety = 50
        self.sleep = 50
        self.health = 100
        self.water = 50
        self.alive = True
    def to_eat(self):
        print("Eating")
        self.satiety += 10
        self.gladness += 0.5
        self.sleep -= 1
        self.health += 20
        self.water += 1
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
        self.satiety -= 1
        self.sleep += 5
        self.health += 20
        self.water -= 1
    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.satiety -= 1.5
        self.sleep += 0.5
        self.health += 10
        self.water -= 1.5
    def to_sick(self):
        print("Got sick")
        self.gladness -= 10
        self.satiety -= 8
        self.sleep -= 5
        self.health -= 40
        self.water -= 10
    def to_drink(self):
        print("Drinking")
        self.satiety -= 1
        self.gladness += 0.5
        self.sleep -= 1
        self.health += 10
        self.water += 10
    def is_alive(self):
        if self.satiety <= -1:
            print("Not enough food…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.sleep <= -2:
            print("Not enough sleep…")
            self.alive = False
        elif self.health <= 0:
            print("Not enough health…")
            self.alive = False
        elif self.water <= -1:
            print("Not enough water…")
            self.alive = False
    def end_of_year(self):
        print(f"Gladness = {self.gladness}")
        print(f"Satiety = {round(self.satiety, 2)}")
        print(f"Sleep = {round(self.sleep, 2)}")
        print(f"Health = {round(self.health, 2)}")
        print(f"Water = {round(self.water, 2)}")
    def live(self, year):
        year = "Year" + str(year) + "of" + self.name + "life"
        print(f"{year:=^50}")
        live_cube = random.randint(1, 5)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_drink()
        elif live_cube == 5:
            self.to_sick()
        self.end_of_year()
        self.is_alive()
Bob = Human(name="Bob")
for year in range(111):
    if Bob.alive == False:
        break
    Bob.live(year)