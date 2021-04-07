import random
import math
import arcade
import Tile
import Position
class World:

    def __init__(self, LENGTH, seed):
        self._possibleDirections = [Position.Position(-1,0),Position.Position(1,0),Position.Position(0,-1),Position.Position(0,1)]
        self._LENGTH = LENGTH
        self._tiles = [[Tile.Tile for i in range(self._LENGTH)] for j in range(self._LENGTH)]
        self._tilesVistited = []
        self._previousTiles = []
        self._builder = Position.Position(0,0)
        self._seed = seed
        random.seed(self._seed)

    def generateTiles(self):
        self._tiles = [[Tile.Tile for i in range(self._LENGTH)] for j in range(self._LENGTH)]
        for x in range(self._LENGTH):
            for y in range(self._LENGTH):
                self._tiles[y][x] = Tile.Tile(x,y)

    def checkAroundSquare(self, currentPos):
        if(self.checkMove(currentPos.getX() + 1, currentPos.getY())):
            return True
        if(self.checkMove(currentPos.getX() - 1, currentPos.getY())):
            return True
        if(self.checkMove(currentPos.getX(), currentPos.getY() + 1)):
            return True
        if(self.checkMove(currentPos.getX(), currentPos.getY() - 1)):
            return True
        return False

    def checkMove(self, x, y):
        if(x  < 0 or y < 0):
            return False
        elif(x >= self._LENGTH or y >= self._LENGTH):
            return False
        for i in range(len(self._tilesVistited)):
            if(self._tilesVistited[i].getX() == x and self._tilesVistited[i].getY() == y):
                return False
        return True

    def boardComplete(self):
        if(len(self._tilesVistited) == self._LENGTH*self._LENGTH):
            return True
        return False

    def backUp(self):
        counter = -1
        while(not self.checkAroundSquare(self._builder)):
            self._builder = self._previousTiles[-1]
            self._previousTiles.pop(-1)
            counter+=-1

    def walkThroughWorld(self):
        #print(str(self._builder.getX()) + " " + str(self._builder.getY()))
        if(self.boardComplete()):
            return True
        if(not self.checkAroundSquare(self._builder)):
            self.backUp()
        nextMove = self._possibleDirections[random.randint(0,3)]
        while(not self.checkMove(nextMove.getX() + self._builder.getX(), nextMove.getY() + self._builder.getY())):
            nextMove = self._possibleDirections[random.randint(0,3)]

        tile = Position.Position(self._builder.getX(), self._builder.getY())
        self._tilesVistited.append(tile)
        self._previousTiles.append(tile)
        self.crossTiles(self._builder, nextMove)
        self._builder.addPosition(nextMove)
        return False
            

    def crossTiles(self, pos, nextMove):
        self._tiles[pos.getY()][pos.getX()].removeWall(nextMove)
        invertedPos = Position.Position(nextMove.getX()*-1,nextMove.getY()*-1)
        self._tiles[pos.getY() + nextMove.getY()][pos.getX() + nextMove.getX()].removeWall(invertedPos)

    def setSeed(self, seed):
        self._seed = seed
        random.seed(self._seed)

    def getTiles(self):
        return self._tiles