from game import constants

import arcade

class Hand(arcade.Sprite):
    def __init__(self, image, direction, min_x, max_x, attacker):
        super().__init__(image)
        self._direction = direction
        self.left = min_x
        self._key_down = False
        self._min_x = min_x
        self._max_x = max_x
        self.center_x = (min_x + max_x)/2
        self.passedLine = False
        invert = 1
        if(attacker):
            invert = -1
        self.change_x = -self._direction * constants.SLAP_SPEED * invert
        

    def resetPosition(self, attacker):
        if(self._direction == -1):
            if(attacker):
                self.left = self._min_x
            else:
                self.right = self._max_x
            
        elif(self._direction == 1):
            if(attacker):
                self.right = self._max_x
            else:
                self.left = self._min_x
        invert = 1
        if(attacker):
            invert = -1
        self.change_x = -self._direction * constants.SLAP_SPEED * invert

    def move(self, attacker):
        self._key_down = True
        invert = 1
        if(attacker):
            invert = -1

        self.change_x = self._direction * constants.SLAP_SPEED * invert
    
    def stop(self, attacker):
        self._key_down = False
        invert = 1
        if(attacker):
            invert = -1
        self.change_x = -self._direction * constants.SLAP_SPEED * invert

    def update(self, attacker):
        if ((self.right + self.change_x) <= self._max_x) and ((self.left + self.change_x) >= self._min_x):
            self.center_x += self.change_x
        
        if((self._direction == -1) and not attacker):
            if((self.left < (constants.MAX_X/2) + 206)):
                    self.passedLine = True
            else:
                self.passedLine = False
        elif(not attacker):
            if((self.right > (constants.MAX_X/2) - 206)):
                    self.passedLine = True
            else:
                self.passedLine = False