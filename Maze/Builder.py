import random
class Builder:
    def __init__(self, length):
        self._possibleDirections = [-1,-length,1,length]
        self._number = 0
        self.direction = []
        self.direction.append(1)

    def moveDirection(self):
        self._number += self.direction[-1]
    
    def getNextDirection(self, seed):
        random.seed(seed)
        running = True
        nextDir = -1
        while(running):
            random.shuffle(self._possibleDirections)
            nextDir = self._possibleDirections[0]
            if nextDir == -1 and self.direction[-1] == 1:
                continue
            elif nextDir == 1 and self.direction[-1] == -1:
                continue
            elif nextDir == -10 and self.direction[-1] == 10:
                continue
            elif nextDir == 10 and self.direction[-1] == -10:
                continue
            running = False
        return nextDir