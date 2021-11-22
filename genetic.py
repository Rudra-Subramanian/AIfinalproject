import sys
import numpy as np
import minimax
import game1
import math
from random import randrange

#which user does the genetic algorithm control (player 1 or player 2)
class organism:
    def __init__(self, player,heuristic):
        self.player = player
        self.heuristic = heuristic



    #mutates a given heuristic (will have small functions to do each type)
    def mutateHeuristic(self):
        random = randrange(100)
        if random < 40:
            newHeuristic = basicmutation(self.heuristic)
        elif random < 60:
            newHeuristic = crossover(self.heuristic)
        elif random < 95:
            newHeuristic = swaporder(self.heuristic)
        else:
            newHeuristic = self.heuristic #the do nothing mutation
        return(newHeuristic)






    #given a state will analyse how good the win of the state was.


    def createOffspring(self):
        return(self)

def evolve(organisms):
    return(newOrganisms)

def analyzeState(state):
    return(score)




if __name__ == "__main__":
    startingHeuristic = [["*",0.015, "x"], ["+",0, "y"], ["-",0, "z"], ["+",00, "v"]]
    playingAgainst = organism(1, startingHeuristic)
    organisms = []
    for i in range(50):
        value = math.pow(-1,i)
        organisms.append(organism(value, startingHeuristic))
    
