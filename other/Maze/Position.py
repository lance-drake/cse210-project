class Position:

    def __init__(self, x ,y):
        self._x = x
        self._y = y

    def setPosition(self, x , y):
        self._x = x
        self._y = y

    def addPosition(self, pos):
        self._x += pos.getX()
        self._y += pos.getY()

    def subtractPostion(self, pos):
        self._x -= pos.getX()
        self._y -= pos.getY()
    
    def invertPos(self):
        self._x *= -1
        self._y *= -1

    def getX(self):
        return self._x

    def setX(self, x):
        self._x = x

    def getY(self):
        return self._y

    def setY(self, y):
        self._y = y