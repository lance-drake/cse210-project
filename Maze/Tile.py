import Position
class Tile:

    def __init__ (self, x, y):
        self.position = Position.Position(x,y)
        self.walls = [True, True, True, True]#Left Top Right Bottom

    def removeWall(self, nextPos):
        if(nextPos.getX() == 1):
            self.walls[2] = False
        elif(nextPos.getX() == -1):
            self.walls[0] = False
        elif(nextPos.getY() == 1):
            self.walls[1] = False
        elif(nextPos.getY() == -1):
            self.walls[3] = False

