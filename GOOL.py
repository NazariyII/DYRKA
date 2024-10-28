import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladnes = 50
        self.money = 500
        self.progress = 0
        self.alive = True
    def to_study(self):
        print("time to study")
        self.gladnes -= 5
        self.progress += 0.12
        self.money -= 15
    def to_chill(self):
        print("time to chill")
        self.gladnes += 5
        self.progress -= 0.07
        self.money -= 30
    def to_sleep(self):
        print("time to sleep")
        self.gladnes += 3
        self.money -= 20
    def to_work(self):
        print("time to work")
        self.money =+ 100
        self.gladnes -= 3
    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out")
            self.alive = False
        elif self.gladnes <= 0:
            print("GOOOLLL")
            self.alive = False
        elif self.money <= 0:
            print("BOMGHARA!")
            self.alive = False
        elif self.progress > 5:
            print("Passed")
            self.alive = False
    def end_of_day(self):
        print(f'gladnes = {self.gladnes}')
        print(f'progres = {round(self.progress, 2)}')
        print(f'money = {self.money}')
    def live(self, day):
        day = f'Day {day} of {self.name} life'
        print(f'{day:=^50}')

        LiveCube = random.randint(1, 4)
        if LiveCube == 1:
                self.to_study()
        elif LiveCube == 2:
                self.to_sleep()
        elif LiveCube == 3:
                self.to_chill()
        elif LiveCube == 4:
                self.to_work()
                self.end_of_day()
                self.is_alive()

human = Student(input('Enter your name: '))
for i in range(1, 366):
    if human.alive == False:
        break
    human.live(i)