class Dinosaur:
    def __init__(self):
        self.name = 'Adonomis'
        self.attack_power = 40
        self.health = 97
        

    def attack(self, robot):
        robot.health -= self.attack_power
        print (f'this is robot health {robot.health}')
        print(f"{self} attacks {robot} with {self.attack_power} damage.")
        print (f"{robot} has {robot.health} left.")