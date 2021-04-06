import arcade
from random import randint
from game import constants


class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.ENEMY_IMAGE)
        self.center_x = randint(5, constants.MAX_X - 5)
        self.center_y = constants.ENEMY_Y
        self.change_x = constants.ENEMY_SPEED
        self.change_y = constants.ENEMY_SPEED

    def move_horizontal(self):
        self.change_y *= -1

    def move_vertical(self):
        self.change_x *= -1
