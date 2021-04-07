import arcade
from random import randint
import constants


class Enemy(arcade.Sprite):
    def update(self):
        self.center_x = randint(5, constants.MAX_X - 5)
        self.center_y = constants.ENEMY_Y
        self.change_x = constants.ENEMY_SPEED
        self.change_y = constants.ENEMY_SPEED

    def move_horizontal(self):
        self.change_y *= -.01

    def move_vertical(self):
        self.change_x *= -.01
