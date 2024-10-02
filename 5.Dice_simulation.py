import random

class Dice:
    def roll(self):
        return random.randint(1, 6)

class DiceSimulation:
    def __init__(self, num_dice, num_throws):
        self.num_dice = num_dice
        self.num_throws = num_throws
        #self.sides = sides
        self.results = []

    def run_simulation(self):
  
        for k in range(self.num_throws):
            throw_results = []
            dice = Dice()  # Create a new die for each throw
            for i in range(self.num_dice):
                throw_results.append(dice.roll())
            total = sum(throw_results)
            self.results.append(total)


#Usage
if __name__ == "__main__":
    num_dice = int(input("Enter the number of dice to roll: "))
    num_throws = int(input("Enter the number of times to roll the dice: "))

    simulation = DiceSimulation(num_dice, num_throws)
    simulation.run_simulation()
    simulation.results  





import matplotlib.pyplot as plt
import numpy


data = simulation.results
plt.hist(data, bins=11, edgecolor='black')
plt.show()
