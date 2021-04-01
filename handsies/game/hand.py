from game import constants

import arcade

class Hand(arcade.Sprite):
    def __init__(self, image, direction, start_x, min_x, max_x):
        super().__init__(image)
        self._direction = direction
        self._is_moving = False
        self._min_x = min_x
        self._max_x = max_x
        self._center_x = start_x

    def move(self):
        if not self._is_moving:
            self._is_moving = True
            self.change_x = self._direction * constants.SLAP_SPEED
    
    def update(self):
        if self._is_moving:

            if self._direction == 1 and self.right >= self._max_x:
                self.change_x = -self.change_x
                # self.right = self._max_x
                if self.left <= self._min_x:
                    self.change_x = 0
                    self._is_moving = False

            elif self._direction == -1 and self.left <= self._min_x:
                self.change_x = -self.change_x
                # self.left = self._min_x
                if self.right >= self._max_x:
                    self.change_x = 0
                    self._is_moving = False
            self.center_x += self.change_x

        # if self._is_slapping:
        #     if self._direction == 1 and self.center_x >= constants.CENTER_X:
        #         self.change_x = -(constants.SLAP_SPEED / 2)
        #     if self._direction == -1 and self.center_x <= constants.CENTER_X:
        #         self.change_x = (constants.SLAP_SPEED / 2)
        # self.center_x += self.change_x
        
        # if self.left <= self._min_x:
        #     self.left = self._min_x
        #     self.change_x = 0
        #     self._is_moving = False
        # elif self.right >= self._max_x:
        #     self.right = self._max_x
        #     self.change_x = 0
        #     self._is_moving = False