SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
HAND_TEXTURE = arcade.load_texture("hand-keyframe 1.png")


class WrappingInt():
    def __init__(self, value, limit):
        self._value = value
        self.limit = limit

    @property
    def value(self):
        return self._value
    
    # Sets the value to the opposite end.
    @value.setter
    def value(self, value):
        self._value = value
        if self._value > self.limit:
            self._value -= self.limit
        elif self._value < 0:
            self._value += self.limit

    # Discovered __iadd__ method
    def __iadd__(self, value):
        self.value = self.value + value
        return self

# Defines an angle
class Angle():
    def __init__(self):
        self._degrees = WrappingInt(0, 360)
    
    @property
    def degrees(self):
        return self._degrees.value
    
    @property
    def radians(self):
        return math.radians(self._degrees.value)
    
    # Returns a new angle
    def __iadd__(self, angle):
        self._degrees += angle
        return self
    
    # Copies angle to another object
    def clone(self):
        return copy.deepcopy(self)

class Hand():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 0
        self.angle = Angle()
        self.texture = HAND_TEXTURE
    
    def draw(self):
        arcade.draw_texture_rectangle(self.center.x,self.center.y,self.radius*2,self.radius*2,self.texture,self.angle.degrees)
    
    @abstractmethod
    def attack(self):
        pass
    
    @abstractmethod
    def push(self):
        pass

    @abstractmethod
    def hit(self):
        pass
    
    @abstractmethod
    def ispushing(self):
        pass

class HandOne(hand):
    def __init__(self):
        super().__init__()
        self.x =  50
        self.y = 100

    def attack(self):
        self.angle += 75
        while self.angle >= 0 :
            self.angle -= 19
        self.angle = 0
        self.hit()

    
    
    def hit(self):
        if handtwo.ispushing

class HandTwo(hand):
    def __init__(self):
        super().__init__()
        self.x = SCREEN_WIDTH - 50
        self.y = 100

    def attack(self):
        self.angle += 75
        while self.angle >= 0 :
            self.angle -= 19
        self.angle = 0
        self.hit()
    
    def hit(self):
        if handtwo.ispushing