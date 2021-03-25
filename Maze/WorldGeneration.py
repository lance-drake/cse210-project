import random
import math
import arcade
import Building
import Tile
import Builder
class World:

    def __init__(self):
        self._LENGTH = 10
        self._buildings = []
        self._tiles = [0]*(self._LENGTH)
        self._tilesVistited = []
        self._builder = Builder.Builder(self._LENGTH)

    def generateTiles(self):
        for x in range(self._LENGTH):
                self._tiles[x] = Tile.Tile(x)

    def walkThroughWorld(self):
        nextDir = self._builder.getNextDirection
        movesafe = True
        for x in range(len(self._tilesVistited)):
            if(nextDir+self._builder._number == self._tilesVistited[x]):
                movesafe = False
                break
        if movesafe:
            self._tilesVistited.append(nextDir+self._builder._number)
            self._builder.direction = nextDir
            self._builder.moveDirection(self._LENGTH)
            if(nextDir == -1):
                self._builder.walls[]
            elif(nextDir == -10):
                self._builder.walls[] 
            elif(nextDir == 1):
                self._builder.walls[]
            elif(nextDir == 10):
                self._builder.walls[]


    def generateWhiteNoise(self, number):
        noise = [0] * number

        for i in range(0,number):
                noise[i] = random.randint(0,1)

        return noise
    
    def create_building(self, number):
        noise = self.generateWhiteNoise(number)
        for _ in noise:
            building = Building.Building(
                random.randint(0,900),
                random.randint(0,700),
                random.randint(20,200), 
                random.randint(20,200))
            self._buildings.append(building)

    def getBuildings(self):
        return self._buildings