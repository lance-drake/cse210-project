from game import constants

import arcade

class Hand(arcade.Sprite):
    def __init__(self, image, direction, attacker):
        super().__init__(image)
        self._direction = direction
        self._key_down = False
        self._min_x = 0
        self._max_x = 0
        self.resetPosition(attacker)
        self.passedLine = False
        invert = 1
        if(attacker):
            invert = -1
        self.change_x = -self._direction * constants.SLAP_SPEED * invert
        

    def resetPosition(self, attacker):
        if(self._direction == -1):
            if(attacker):
                self._min_x = (constants.MAX_X/2)+40
                self._max_x = constants.MAX_X-112
                self.left = self._min_x
            else:
                self._min_x = (constants.MAX_X/2)-80
                self._max_x = constants.MAX_X-112
                self.right = self._max_x
            
        elif(self._direction == 1):
            if(attacker):
                self._min_x = 112
                self._max_x = (constants.MAX_X/2)-40
                self.right = self._max_x
            else:
                self._min_x = 112
                self._max_x = (constants.MAX_X/2)+80
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
            if((self.left < (constants.MAX_X/2))):
                    self.passedLine = True
            else:
                self.passedLine = False
        elif(not attacker):
            if((self.right > (constants.MAX_X/2))):
                    self.passedLine = True
            else:
                self.passedLine = False