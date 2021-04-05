import arcade
import Maze.main
import constants

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.PLAYER_IMAGE)
        self.center_x = 0
        self.center_y = int(Maze.main.SCREEN_HEIGHT/2)