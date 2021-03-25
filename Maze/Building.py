class Building:
    def __init__(self, x ,y , width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y
    
    def setWidth(self, width):
        self._width = width

    def setHeight(self, height):
        self._heigt = height

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height