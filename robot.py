from weapon import Weapon

class Robot:
    def __init__(self):
        self.name = 'zordon'
        self.health = 98    
        self.active_weapon = Weapon('rocket blaster', 20)


    def attack(self,dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print (f'this is dinosaur health {dinosaur.health}')
        print(f"{self}) attacks {dinosaur} with {self.active.weapon.name}.")
        print(f"{dinosaur} has {dinosaur}")