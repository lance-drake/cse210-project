class Tile:

    def __init__ (self, number):
        self._number = number
        self._visited = False
        self.walls = [True, True, True, True]#Left Right Top Bottom

    def getTileNumber(self):
        return self._number


    def isVisted(self):
        return self._visited

    def visit(self):
        self._visited = True

