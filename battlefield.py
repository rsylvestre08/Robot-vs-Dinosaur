from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self) -> None:
        self.dinosaur = Dinosaur()
        self.robot = Robot()

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
    def display_welcome(self):
        print('Welcome the battle of the ages')
    def battle_phase(self):
        print("Let us begin..")   
        while self.robot.health > 0 and self.dinosaur.health > 0:

        
           self.robot.attack(self.dinosaur)
    def display_winner(self):    
        print("We have a Winner")